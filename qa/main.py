#-*- coding:utf-8 -*-
# water enviroment quality assessment

import os

import numpy as np
import pandas as pd
np.set_printoptions(suppress = True)

import method

def search_for(directoy,target):
	for (root,dirs,files) in os.walk(directoy):
		if target in files:
			return os.path.join(root,target)
			
def analysis():
	# m = int(input("监测点数目="))
	# n = int(input("监测点指标个数="))
	# k = int(input("评价等级数="))

	print("读取监测数据和标准数据")
	
	dir = input("请输入待查找的初始目录：")

	print()
	target1 = input("监测数据文件名(.csv)：")

	try:
		x0 = pd.read_csv(search_for(dir, target1))
	except Exception as e:
		print("读入监测数据文件错误")
		print(e)
		return
	'''
	x = np.zeros((m, n))
	f = open(search_for(dir, target1))	# 监测数据文件：m个样本，n个指标
	lines = f.readlines()
	x_row = 0
	for line in lines:		# 将目标文件数据输入进矩阵
		list = line.strip('\n').split(' ')
		x[x_row:] = list[0:n]
		x_row += 1
	'''
	print("\n监测数据")
	print(x0)
	
	
	# print("\n------------------------------------------------------------\n")
	print()
	target2 = input("标准数据文件名(.csv)：")

	try:
		s0 = pd.read_csv(search_for(dir, target2))
	except Exception as e:
		print("读入标准数据文件错误")
		print(e)
		return
	'''
	s = np.zeros((n, k))
	f = open(search_for(dir, target2))	# 指标标准文件：每个指标有k个等级
	lines = f.readlines()
	s_row = 0
	for line in lines:
		list = line.strip('\n').split(' ')
		s[s_row:] = list[0:k]
		s_row += 1
	'''
	print("\n评价指标")
	print(s0)
	
	print("\n------------------------------------------------------------\n")
	'''
	print("请输入对应数字选择综合评价方法")
	print("1.未确知测度法 2.灰关联分析法 3.模糊综合评价法")
	chose = int(input())
	while (chose != 1 and chose != 2 and chose != 3):
		chose = int(input("输入错误，请重新输入："))
		print(chose)
	if chose == 1:
		method.Unascertained_Measure_Model(m, n, k, x, s)
	elif chose == 2:
		method.Gray_Relational_Analysis(m, n, k, x, s)
	elif chose == 3:
		method.Fuzzy_Comprehensive_Evaluation(m, n, k, x, s)
	'''
	dataAssement = method.AssessmentModel(x0, s0)
	ans1 = dataAssement.Unascertained_Measure_Model()
	ans2 = dataAssement.Gray_Relational_Analysis()
	ans3 = dataAssement.Fuzzy_Comprehensive_Evaluation()
	
	name = dataAssement.name
	level = dataAssement.level
	# print(level)
	# print(name)
	print("          未确知测度   灰关联分析   模糊综合评价")
	
	for i in range(0, dataAssement.numOfm):
		print("%5s" % name[i], end = "   ")
		print("%5s" % level[ans1[i]], end = "级      ")
		print("%5s" % level[ans2[i]], end = "级      ")
		print("%5s" % level[ans3[i]], end = "级\n")

	#print(x.T)
	#show.showImg(n, tag, x.T)
	dataAssement.showElementImg()


def run_qa():
	print("\n                  水环境质量综合评价系统")
	print("\n------------------------------------------------------------\n")
	print("  使用未确知测度，灰关联分析，模糊综合评价三种模型进行评价")
	print("  输入基本数据文件即可得到结果")
	print("\n------------------------------------------------------------\n")

	while(True):
		analysis()
		print("\n------------------------------------------------------------\n")
		print("继续评价其他数据请输入1， 退出请输入2")
		isexit = int(input())
		while isexit != 1 and isexit != 2:
			isexit = int(input("输入错误，请重新输入："))
		if isexit == 2:
			break

if __name__ == '__main__':
	run_qa()
