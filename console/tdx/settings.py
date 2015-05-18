import logging
import sqlite3

conn = sqlite3.connect('estock.s3db')
rs = conn.cursor().execute('select key, value from config')
d = rs.fetchall()
conn.close()

config = {
	'DEBUG': True,

    # Logging setting
    'LOG_LEVEL':       logging.DEBUG,
    'LOG_FORMAT':      '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    'LOG_FILENAME':    'estock.log',
    'LOG_FILEMODE':    'a',
    'LOG_MAXBYTES':    10*1024*1024,
    'LOG_BACKUPCOUNT': 7,

	# DB Setting
	'DB_HOST': '127.0.0.1',
	'DB_DATABASE': 'estock',
	'DB_USER': 'estock',
	'DB_PASSWORD': '12qwaszx',

	# File setting
    'stock_code_file': 'codes.txt',
    'stock_code_file_encode': 'gbk',

    'stock_hist_file': 'hist.db',

    # TDX binary stock hist dir
    'tdx_hist_dirs': ('F:/zd_ztzq/vipdoc/sz/lday', 'F:/zd_ztzq/vipdoc/sh/lday', ),

    # TDX daily data URI
    'tdx_daily_uri': (
        #'http://www.tdx.com.cn/products/data/data/shzsday.zip', 
        #'http://www.tdx.com.cn/products/data/data/szzsday.zip',
        'http://www.tdx.com.cn/products/data/data/vipdoc/shlday.zip',
        'http://www.tdx.com.cn/products/data/data/vipdoc/szlday.zip',
        'http://www.tdx.com.cn/products/data/data/vipdoc/tdxzs_day.zip',
        ),

    # Table dict
    'sz': 'estock_hist_sz',
    'sh': 'estock_hist_sh',

    # Eastmoney -------------->
    #'EAST_DATA_URL': 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=NS&sty=NSST&st=12&sr=-1&p={page}&ps=50&stat=1&rt=47616849',
    #'EAST_END_PAGE': 28,
    #'EAST_CSV_PATH': './data/newstock.csv',
}

for key, value in d:    
    config[key.encode('ascii')] = value.encode('ascii')

if __name__ == '__main__':
    print config
