#!/bin/user/env python3
# -*- coding : utf-8 -*-

'''
	class simple demon
'''

class Telemecanique(object):
	'''
	Telemecanique 
	'''
	def show_info(self):
		print('This is a basi Telemecanique')

class Fan(Telemecanique):
	'''
	Fan
	'''

	def __init__(self,brand):
		self.__brand = brand

	def show_info(self):
		print('This is a Fan ,made in China ,brand is '+self.__brand)

	def work(self):
		print('I\'m working hard now ! Do you feel cool ?')


class Microwaveoven(Telemecanique):
	'''
	Microwave oven
	'''

	def __init__(self,power):
		self.power = power

	def show_info(self):
		print('I\'m a Microwave oven ,I\'m strong ...')

class Worker(object):
	'''
	Worker
	'''
	def show_info(self):
		print('I\'m work in hccc')

def run(obj):
	obj.show_info()


if __name__ == '__main__':
	run(Telemecanique())
	run(Fan('Media'))
	run(Microwaveoven(1000))
	run(Worker())
