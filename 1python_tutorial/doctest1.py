#!/user/bin/env python3
# -*- coding:utf-8 -*-

import doctest

class Dt:
	'''
		difine class, add ,sub,abs
	>>> ins = Dt()
	>>> ins.a = 3
	>>> ins.b = 4
	>>> ins.add()
	7
	7
	>>> ins.sub()
	-1
	-1
	>>> ins.abs()
	3
	4
	(3, 4)

	'''	
	def add(self):
		print(self.a + self.b)
		return self.a + self.b

	def sub(self):
		print(self.a - self.b)
		return self.a - self.b

	def abs(self):
		print(abs(self.a))
		print(abs(self.b))
		return abs(self.a),abs(self.b)

if __name__ == '__main__':
	doctest.testmod()