# -*- coding: utf-8 -*-
# System lib import
import urllib2
import codecs
import re
from bs4 import BeautifulSoup

# User defined lib import
from settings import config
from utils.single_thread import SingleThread

class GetStockCodeWorker(object):

    __url__ = 'http://quote.eastmoney.com/stocklist.html'

    def __init__(self, output, encoding='gbk'):
        self.output = output
        self.encoding = encoding

    def run(self):
        worker = SingleThread(self._get_code_list)
        worker.run()
        
    def _get_code_list(self):
        r = urllib2.Request(self.__url__)
        d = urllib2.urlopen(r).read().decode(self.encoding)
        bs = BeautifulSoup(d)
        with(codecs.open(self.output, 'wb', self.encoding)) as o:
            for ul in bs.find(id='quotesearch').findAll('ul'):
                for li in ul.children:
                    code = re.compile(r'\d{6}').findall(li.string)
                    if(len(code) == 1):
                        code = code[0]                    
                        codename = li.string[:li.string.find('(')] 
                        # Write the code and name to output file                       
                        o.write(u'{code}, {name}\r\n'.format(code=code, name=codename))           
        

                        
if __name__ == '__main__':     
    worker = GetStockCodeWorker(config['stock_code_file'], config['stock_code_file_encode'])
    worker.run()
                    
