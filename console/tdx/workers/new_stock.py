# -*- coding: utf-8 -*-
import re
import urllib2
import time
import csv

# user define lib
from settings import config
from base.single_thread import SingleThread
from base.base import Base

class EastmoneyWorker(Base):

	def __init__(self):
		super(EastmoneyWorker, self).__init__()

	def run(self):
		runner = SingleThread(self.get, max_retry=1)
		runner.run()

	def get(self):
		p = re.compile(r'\(\[(.*)\]\)')
		with open(config['EAST_CSV_PATH'], 'wb') as csvfile:
			writer = csv.writer(csvfile)
			for i in range(1, int(config['EAST_END_PAGE'])):
				url = config['EAST_DATA_URL'].format(page = i)
				self.logger.info('Downloading url: {url}'.format(url = url))
				f = urllib2.urlopen(url).read()
				if(f):
					content = p.search(f).group(1)
					for item in content.split(r'","'):
						writer.writerow(item.replace('"', '').split(','))


if __name__ == '__main__':
	worker = EastmoneyWorker()
	worker.run()

