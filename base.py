# System lib
import logging
from logging.handlers import RotatingFileHandler
import os
import sys

# User defined lib
from settings import config

class Base(object):	

	logger = None

	def __init__(self):
		self.__class__._init_logger()

	@classmethod
	def _init_logger(cls):	
		if Base.logger is None:
			handler = RotatingFileHandler(config['LOG_FILENAME'],
					mode        = config['LOG_FILEMODE'],
					maxBytes    = config['LOG_MAXBYTES'],
					backupCount = config['LOG_BACKUPCOUNT']
			)
			handler.setFormatter(logging.Formatter(config['LOG_FORMAT']))

			Base.logger = logging.getLogger(cls.__name__)
			Base.logger.addHandler(handler)
	

if __name__ == '__main__':
	class A(Base):
		def __init__(self):
			dd = 1
			super(A, self).__init__()

	class B(Base):
		def __init__(self):
			dd = 1
			super(B, self).__init__()

	a=A()
	a.logger.info('hi')
	b=B()
	b.logger.error('fuck')