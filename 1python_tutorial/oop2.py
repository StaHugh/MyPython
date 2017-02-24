#!/user/bin/env python3
# -*- coding:utf-8 -*-

class Book(object):
	'''
	demon about class value , instanse value and protected value

			class value     		------   	instanse value
			protected class value   ------ 		protected class value
	'''
	name = 'class attr.name -->class book'
	__name = 'class protected attr.__name --->class book'

	def __init__(self,category,press):
		self.category = category
		self.__press = press

	def show_info(self):
		print('-------------show info -------------')
		#print('class.name :'+name)
		#print('class.__name:'+__name)
		print('instanse.category:'+self.category)
		print('instanse.__press:'+self.__press)

def run():
	webP = Book('Engineering','Machine Press')
	print(Book.name)
	webP.show_info()
	webP.__name = 'instanse name to test class protected attr'
	print('webP.__name belongs to ?....'+webP.__name)
	webP.__press = 'instanse new attr to test instanse protected attr'
	print('webP.__press belongs to ?....'+webP.__press)
	print(Book.name)
	webP.show_info()

if __name__ == '__main__':
	run()


