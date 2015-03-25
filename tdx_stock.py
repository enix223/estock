# -*- coding: utf-8 -*-
# System module
import time
import re
import os
import urllib2
import shutil
from zipfile import ZipFile
from bs4 import BeautifulSoup
from struct import unpack
from base import Base

# User module
from settings import config
from utils.single_thread import SingleThread
from utils.db_import import MySQLDB

class TdxStockWorker(Base):

    __SHENZHEN__ = 'sz'
    __SHANGHAI__ = 'sh'
    __BUFFER_SIZE__ = 1024
    __TMP_DIR__ = 'tmp'
    
    def __init__(self):
        self.mysql_db = MySQLDB(config['DB_HOST'], config['DB_DATABASE'], config['DB_USER'], config['DB_PASSWORD'])
        super(TdxStockWorker, self).__init__()

    '''
    Clear tmp dir
    '''
    def house_keeping(self):    
        # Clear temp folder
        shutil.rmtree(self.__TMP_DIR__, ignore_errors=True)
        os.mkdir(self.__TMP_DIR__)

        # Clear table
        self.mysql_db.execute('truncate table {t}'.format(t=config[self.__SHANGHAI__]))
        self.mysql_db.execute('truncate table {t}'.format(t=config[self.__SHENZHEN__]))

    '''
    Extract the daily data from TDX uri, and load them to database
    '''
    def daily(self):        
        
        # Call house keeping func
        self.house_keeping()

        for uri in config['tdx_daily_uri']:
            r = urllib2.Request(uri)
            d = urllib2.urlopen(r)
            stamp = long(time.time()*1000)
            filename = 'tmp_{stamp}'.format(stamp=stamp)
            tmpfile = '{tmpdir}/{filename}.zip'.format(tmpdir=self.__TMP_DIR__, filename=filename)
            
            # Download the zip file
            with(open(tmpfile, 'wb')) as z:
                data = d.read(self.__BUFFER_SIZE__)                
                while(data):            
                    z.write(data)
                    data = d.read(self.__BUFFER_SIZE__)

            # Open and unzip the file
            with(ZipFile(tmpfile, 'r')) as tmpzip:
                tmpdir = os.path.join(self.__TMP_DIR__, filename)
                tmpzip.extractall(tmpdir)
                self.get((tmpdir,))
                
    '''
    Extract the history data from binary file and load it to database
    @param hist : flag to indicate history data or not
    '''
    def run(self, hist):
        if(hist): # Extract history data
            runner = SingleThread(self.get, config['tdx_hist_dirs'], max_retry=1)
            runner.run()
        else: # Extract daily data
            runner = SingleThread(self.daily, max_retry=1)
            runner.run()

    def get(self, dirs):   
        # Connect to the DB
        self.mysql_db.connect()

        # Close auto commit mode
        self.mysql_db.execute('SET autocommit=0')

        for directory in dirs:                
                self.logger.debug(('Processing directory: {d}'.format(d=directory)))

                for file_name in os.listdir(directory):

                    # Skip un-related files or dir
                    if(file_name[:2] not in (self.__SHENZHEN__, self.__SHANGHAI__) or 
                        not os.path.isfile(os.path.join(directory, file_name))):
                        continue

                    self.logger.debug('Processing: {code}...'.format(code=file_name))                    

                    market_table = file_name[:2]
                    code = file_name[2:8]
                    with(open(os.path.join(directory, file_name), 'rb')) as f:    
                        while(True):                    
                            data = f.read(32)
                            if data:
                            	kv = {}
                                kv['code'] = code
                                kv['date'] = unpack('=L', data[0:4])[0]
                                kv['open'] = unpack('=L', data[4:8])[0]/100.0
                                kv['high'] = unpack('=L', data[8:12])[0]/100.0
                                kv['low'] = unpack('=L', data[12:16])[0]/100.0
                                kv['close'] = unpack('=L', data[16:20])[0]/100.0
                                kv['deal'] = unpack('=f', data[20:24])[0]
                                kv['amount'] = unpack('=L', data[24:28])[0]
                                #kv['reverse'] = unpack('=L', data[28:32])[0]

                                self.mysql_db.insertSQLIgnore(config[market_table], kv)                        
                            else:
                                break
                        self.mysql_db.commit()

        self.mysql_db.close()                


if __name__ == '__main__':
    worker = TdxStockWorker()
    worker.run(hist=False)
