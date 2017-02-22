#!/user/bin/env python3
# -*- coding:utf-8 -*-

'''
	logging both to file and console
'''
import logging

logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s%(message)s',
					datefmt='%a, %d %b %Y %H:%M:%S',
					filename='logbothexample.log',
					filemode='w')

#define StreamHandler ,将INFO及以上打印到stderr,并添加到当前的日志处理对象

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.debug('logging both debug message')
logging.info('logging both info message')
logging.warning('logging both warning message')

