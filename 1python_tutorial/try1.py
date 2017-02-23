#!/user/bin/env python3
# -*- coding:utf-8 -*-

'''
	raise exception , define new exception ,
'''

import logging

logging.basicConfig(filename='tryExcept.log')

# fun1 comment ,simple daemon
def fun1():
	try:
		print('try ...')
		r = 10 / 0
		print('result ',r)
	except ZeroDivisionError as e:
		print('exception ,',e)
	finally:
		print('finally..')
	print('end...')

def fun2(s):
	return 10/int(s)

def fun3(s):
	return fun2(s)

def main():
	try:
		fun3('0')
	except Exception as e:
		logging.exception(e)
	finally:
		print('going to test_myException')
		try:
			test_myException('s')
		except Exception as e:
			logging.exception(e)


class MyException(ValueError):
	pass

def test_myException(s):
	n = int(s)
	if 0 == n:
		raise MyException('here is myself exception')
	return 


if __name__ == '__main__':
	main()
	#test_myException('0')


