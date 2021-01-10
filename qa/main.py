#-*- coding:utf-8 -*-
# water enviroment quality assessment

import math
import numpy as np
import pandas as pd
np.set_printoptions(suppress = True)
import method as wam
import os

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
	target1 = input("监测数据文件名(.csv)：")
	target2 = input("标准数据文件名(.csv)：")
	
	x0 = pd.read_csv(search_for(dir, target1))
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
	m = x0.shape[0]
	n = x0.shape[1] - 1
	# x = np.zeros((m, n))
	x = x0.iloc[0:m, 1:n+1].values
	
	# print(x)
	
	# print("\n------------------------------------------------------------\n")
	s0 = pd.read_csv(search_for(dir, target2))
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
	k = s0.shape[1] - 1
	s = s0.iloc[0:n, 1:k+1].values
	# print(s)
	print("\n------------------------------------------------------------\n")
	'''
	print("请输入对应数字选择综合评价方法")
	print("1.未确知测度法 2.灰关联分析法 3.模糊综合评价法")
	chose = int(input())
	while (chose != 1 and chose != 2 and chose != 3):
		chose = int(input("输入错误，请重新输入："))
		print(chose)
	if chose == 1:
		wam.Unascertained_Measure_Model(m, n, k, x, s)
	elif chose == 2:
		wam.Gray_Relational_Analysis(m, n, k, x, s)
	elif chose == 3:
		wam.Fuzzy_Comprehensive_Evaluation(m, n, k, x, s)
	'''
	ans1 = wam.Unascertained_Measure_Model(m, n, k, x, s)
	ans2 = wam.Gray_Relational_Analysis(m, n, k, x, s)
	ans3 = wam.Fuzzy_Comprehensive_Evaluation(m, n, k, x, s)
	# print(x0[x0.columns[0]])
	name = x0[x0.columns[0]].values
	level = s0.columns[1:k+1].values
	# print(level)
	# print(name)
	print("          未确知测度   灰关联分析   模糊综合评价")
	
	for i in range(0, m):
		print("%5s" % name[i], end = "   ")
		print("%5s" % level[ans1[i]], end = "级      ")
		print("%5s" % level[ans2[i]], end = "级      ")
		print("%5s" % level[ans3[i]], end = "级\n")
	
		
