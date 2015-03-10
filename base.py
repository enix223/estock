# System lib
import logging
import os
import sys

# User defined lib
from setting import config

class Base(object):

	def __init__(self):
		self.log = self._init_logger()


	def _init_logger(self):
		logging.baseConfig(level=config['LOG_LEVEL'],
			format=config['LOG_FORMAT'],
			filename=config['LOG_FILENAME'],
			filemode=config['LOG_FILEMODE'])

		return logging.getLogger(self.__class__.__name__)
		