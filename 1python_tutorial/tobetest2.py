#!/user/bin/env python3
# -*- coding : utf-8 -*-

import tobetest1
import unittest

class mytest(unittest.TestCase):

	# init
	def setUp(self):
		self.tclass = tobetest1.myclass()#instanse class to be test

	def tearDown(self):
		pass

	def test_sum(self):
		self.assertEqual(tobetest1.mysum(1, 2), 3)

	def test_sub(self):
		self.assertEqual(tobetest1.mysub(9, 3), 6)

	def test_class_sum(self):
		self.assertEqual(self.tclass.sum(4, 5), 9)

	def test_class_sub(self):
		self.assertEqual(self.tclass.sub(7, 2), 5)

if __name__ == '__main__':
	unittest.main()

