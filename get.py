# -*- coding: utf-8 -*-
from utils.db_import import db
import urllib2

def download(r1='begin', r2='end', dt1='1900-01-01', dt2='9999-12-31'):    
    '''
    http://ichart.yahoo.com/table.csv?s=string&a=int&b=int&c=int&d=int&e=int&f=int&g=d&ignore=.csv
    s — 股票名称
    a — 起始时间，月
    b — 起始时间，日
    c — 起始时间，年
    d — 结束时间，月
    e — 结束时间，日
    f — 结束时间，年
    g — 时间周期。
    '''

    d1 = dt1.split('-')
    d2 = dt2.split('-')

    tb_layout = [
        "stock_code      ",
        "stock_price_date",
        "stock_open      ",
        "stock_high      ",
        "stock_low       ",
        "stock_close     ",
        "stock_volume    ",
        "stock_adj_close "
    ]
    
    __ShangHai__ = 'SS'
    __ShenZhen__ = 'SZ'    
    url = 'http://ichart.yahoo.com/table.csv?a=%s&b=%s&c=%s&d=%s&e=%s&f=%s' % (d1[1], d1[2], d1[0], d2[1], d2[2], d2[0])
    url += '&s=%s.%s'
    fname = 'data/%s_%s.csv'
    
    f = open('code.txt', 'r')
    flag = False
    mdb = db()
    for l in f:

        code = l.strip()
        
        #control the start position
        flag = True if (code == r1 or r1 == 'begin' or flag) else False            
        if not flag:
            continue
        
        d_url, d_name = url, fname
        if l.find('6') == 0:
            d_url, d_name = url % (code, __ShangHai__), fname % (l.strip(), __ShangHai__)
        else:
            d_url, d_name = url % (code, __ShenZhen__), fname % (l.strip(), __ShenZhen__)
            
        r = urllib2.Request(d_url)
        d = urllib2.urlopen(r).readlines()

        fw = open(d_name, 'w')
        i = 0
        for ll in d:
            #store in db
            if(i != 0):
                mdb.insert('stock_history', tb_layout, [code]+ll.split(','))
            
            #write csv
            fw.write(ll)
            i += 1
            
        fw.close()

        #cntrol the stop position
        flag = False if (code == r2 and r2 != 'end') else True
        if not flag:
            break
        
    f.close()
    mdb.close()

if __name__=='__main__':
    print('Download begin...')
    download(r1='000060', r2='000060')
    print('Finished!')

    
