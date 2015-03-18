import logging

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
}
