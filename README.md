# MyPython
python 学习笔记、代码练习

python 学习计划

一.2017.2.3-2017.2.29   	 熟悉python
-------------------------------------------------------
1.练习廖雪峰python学习教程
2.实战练习

二.2017.3.1-2017.3.31    学习python flask相关知识
------------------------------------------------------
1.学习python web开发实战
2.学习web 相关知识






*************************************************************
1.基本的单元测试方法     ---OK
	测试模块函数
	测试模块类中的函数
	测试一个函数、类、模块的所有测试用例放入一个测试模块，就是一个完整的单元测试。
	对一个测试对象添加单元测试后，修改此模块之后只需要跑一次单元测试就能知道修改有无bug。
	编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
	以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
	对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

2.logging 的基本使用方法  ---OK
	logging 到console
	logging 到file
	同时logging到file和console

3.异常处理和调试
	try...except...else...finally...
	a.	添加print函数来调试
	b.	添加断言assert (expression), expression 应该为true。如果断言失败，抛出AssertionError。
	可以程序启动添加 -0 选项来关闭断言。
	c.	logging 
	d.	pdb    python3 -m pdb fileNeedDebug.py.
		进入pdb后使用下列指令：
		l 				查看代码
		n 				单步执行
		p valule 		查看变量值
		q 				结束调试
	e.	pdb.set_trace() .也是使用pdb但是不需要单步执行。import pdb 后，在需要调试的地方添加
		pdb.set_trace(),就可以设置断点。正常启动程序就会停在此处进入pdb ,使用 c 继续运行。
	***********logging 效率最好啦。

4.文档测试（doctest）
	doctest.testmod() 运行doctest。

	


