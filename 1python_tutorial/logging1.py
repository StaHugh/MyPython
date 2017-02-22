#!/user/bin/env python3
# -*- coding : utf-8 -*-

import logging

logtofile = 1

# logging.basicConfig() 要在文件开头调用进行配置。
if (logtofile == 1):
	#logging to file
	logging.basicConfig(filename='loggingExampleFile.log',
					level=logging.DEBUG,
					filemode='a')
	logging.debug('logging to file debug , debugging message')
	logging.warning('logging to file warning, watch out')
	logging.info('logging to file inof , be careful')
else:
	#logging to console
	logging.warning('logging warning, watch out !') #print
	logging.info('logging info, be careful .') #not print
	print ('--------------------------------------------\n')
	

