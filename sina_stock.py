# -*- coding: utf-8 -*-
# System module
import urllib2
import codecs
import time
import re
from bs4 import BeautifulSoup

# User module
from settings import config
from utils.single_thread import SingleThread
from utils.db_import import MySQLDB

class SinaStockWorker(object):

    __url__ = 'http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/{code}.phtml'
    
    def __init__(self, output, encoding='gbk', delay=2):
    	self.encoding = encoding
        self.delay = delay
    	self.output = output
    	self.mysql_db = MySQLDB(config['DB_HOST'], config['DB_DATABASE'], config['DB_USER'], config['DB_PASSWORD'])

    def run(self):
    	runner = SingleThread(self.get, max_retry=1)
    	runner.run()

    def get(self):
        with(codecs.open(config['stock_code_file'], 'rb', config['stock_code_file_encode'])) as i:
            with(codecs.open(self.output, 'wb', self.encoding)) as o:
                for line in i.readlines():
                    code = line.split(',')[0]

                    if(code[0] != '6'):
                        continue
                    
                    r = urllib2.Request(self.__url__.format(code=code))
                    d = urllib2.urlopen(r).read().decode(self.encoding)
                    bs = BeautifulSoup(d)
                    print("Dowloading {code}..., page size={size}".format(code=code, size=len(d)))
                    time.sleep(self.delay)

                    # Get the table of the data
                    table = bs.find(id='FundHoldSharesTable')

                    if(table == None):
                        continue

                    # loop over each hist item
                    for tr in table.findAll('tr'):
                        tds = tr.findAll('td')
                        if(len(tds) == 0):
                            continue

                        if(len(tds[0].div.findAll('a')) == 0):
                            continue

                        date = tds[0].div.a.string
                        op   = tds[1].div.string
                        hi   = tds[2].div.string
                        cl   = tds[3].div.string
                        lo   = tds[4].div.string
                        deal = tds[5].div.string
                        amt  = tds[6].div.string
                        
                        self.mysql_db.insertSQLIgnore('estock_hist_sh', {'code': code, 'date': date, 'open': op, 'high': hi, 'close': cl, 'low': lo, 'deal': deal, 'amount': amt})

                # Commit the data and wait a moment
                self.mysql_db.commit()                
        
        self.mysql_db.close()            

                                                

if __name__ == '__main__':
	runner = SinaStockWorker('hello.txt')
	runner.run()
