#-*- coding:utf-8 -*-
# assessment model

import math
import numpy as np
np.set_printoptions(suppress = True)
import matplotlib.pyplot as plt

class AssessmentModel(object):
	def __init__(self, monitoringData, standardData):
		self.numOfMonpoint = monitoringData.shape[0]
		self.numOfElement = monitoringData.shape[1] - 1
		self.numOfLevel = standardData.shape[1] - 1
		self.monitoringData = monitoringData.iloc[0:self.numOfMonpoint, 1:self.numOfElement+1].values
		self.standardData = standardData.iloc[0:self.numOfElement, 1:self.numOfLevel+1].values
		self.tagElement = monitoringData.columns[1:self.numOfElement+1]
		self.monitoringName = monitoringData[monitoringData.columns[0]].values
		self.assessmentLevel = standardData.columns[1:self.numOfLevel+1].values

	@property
	def name(self):
		return self.monitoringName

	@property
	def level(self):
		return self.assessmentLevel

	@property
	def element(self):
		return self.tagElement

	@property
	def numOfm(self):
		return self.numOfMonpoint

	@property
	def numOfe(self):
		return self.numOfElement

	@property
	def numOfl(self):
		return self.numOfLevel

	def showElementImg(self):
		m = self.numOfMonpoint
		tag = self.tagElement
		data = self.monitoringData.T
		x = np.arange(m)
		total_width, n = 0.8, len(tag)
		width = total_width / n
		x = x - (total_width - width) / 2

		for i in range(len(tag)):
			plt.bar(x + width * i, data[i], width=width, label=tag[i])
		'''
		plt.bar(x, l1, width=width, label='未确知测度', color='red')
		plt.bar(x + width, l2, width=width, label='灰关联分析', color='deepskyblue')
		plt.bar(x + 2 * width, l3, width=width, label='模糊综合评价', color='green')
		'''

		plt.xticks()
		plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
		plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
		plt.ylabel('浓度')
		plt.xlabel('监测点')
		plt.rcParams['savefig.dpi'] = 300  # 图片像素
		plt.rcParams['figure.dpi'] = 300  # 分辨率
		plt.rcParams['figure.figsize'] = (20.0, 15.0)  # 尺寸
		plt.title("各监测点各指标浓度示意图")
		#plt.savefig('show.png')
		plt.show()

	# 未确知测度法
	def Unascertained_Measure_Model(self):
		m = self.numOfMonpoint
		n = self.numOfElement
		k = self.numOfLevel
		x = self.monitoringData
		a = self.standardData
		u1 = np.zeros((m, n, k))	# 计算单指标未确知测度
		for i in range(0, m):
			for j in range(0, n):
				flag = 0
				for l in range(0, k - 1):		# 判断等级数值是递增还是递减的
					if a[j][l] < a[j][l+1]:
						break
					elif a[j][l] > a[j][l+1]:
						flag = 1
						break
				if flag == 0:		# 递增
					if x[i][j] <= a[j][0]:
						u1[i][j][0] = 1
						for l in range(1, k):
							u1[i][j][l] = 0
					elif x[i][j] >= a[j][k-1]:
						u1[i][j][k-1] = 1
						for l in range(1, k):
							u1[i][j][k-1-l] = 0
					else:
						for l in range(0, k-1):
							if a[j][l] <= x[i][j] and x[i][j] <= a[j][l+1]:
								u1[i][j][l] = (a[j][l+1] - x[i][j]) / (a[j][l+1] - a[j][l])
								# print("1%f" % u1[i][j][l])
								u1[i][j][l+1] = (x[i][j] - a[j][l]) / (a[j][l+1] - a[j][l])
								# print("1%f" % u1[i][j][l+1])
				else:				# 递减
					if x[i][j] >= a[j][0]:
						u1[i][j][0] = 1
						for l in range(1, k):
							u1[i][j][l] = 0
					elif x[i][j] <= a[j][k-1]:
						u1[i][j][k-1] = 1
						for l in range(1, k):
							u1[i][j][k-1-l] = 0
					else:
						for l in range(0, k-1):
							if a[j][l] >= x[i][j] and x[i][j] >= a[j][l+1]:
								u1[i][j][l] = (x[i][j] - a[j][l+1]) / (a[j][l] - a[j][l+1])
								# print("2%f" % u1[i][j][l])
								u1[i][j][l+1] = (a[j][l] - x[i][j]) / (a[j][l] - a[j][l+1])
								# print("2%f" % u1[i][j][l+1])
		'''
		print("单指标未确知测度")
		for i in range(0, m):
			print("x%d: " % int(i + 1))
			print(u1[i])
			print("\n")
			
		print("------------------------------------------------------------\n")
		'''
		v = np.zeros((m, n))
		w = np.zeros((m, n))
		sumv = np.zeros(m)
		for i in range(0, m):
			for j in range(0, n):
				t = 0
				for l in range(0, k):
					if u1[i][j][l] != 0:
						t += u1[i][j][l] * math.log(u1[i][j][l], 2)
				v[i][j] = 1 + (1.0 / math.log(k, 2)) * t
			sumv[i] += v[i][j]
		for i in range(0, m):
			for j in range(0, n):
				w[i][j] = v[i][j] / sumv[i]
		'''
		print("指标权重（客观赋值法）")
		print(w)

		print("\n------------------------------------------------------------\n")
		'''

		u2 = np.zeros((m, k))
		for i in range(0, m):
			for l in range(0, k):
				t = 0
				for j in range(0, n):
					t += w[i][j] * u1[i][j][l]
				u2[i][l] = t
		'''
		print("多指标未确知测度")
		print(u2)

		print("\n------------------------------------------------------------\n")
		'''

		# print("样本识别")
		# r = float(input("置信度="))
		r = 0.7
		ans = [0]*m
		for i in range(0, m):
			l = 0
			sumr = 0
			while(sumr < r):
				sumr += u2[i][l]
				l = l + 1
			ans[i] = l
			# print("样本x%d属于%d级" % (i + 1, l))
		return ans
		
	# 灰关联分析法
	def Gray_Relational_Analysis(self):
		m = self.numOfMonpoint
		n = self.numOfElement
		k = self.numOfLevel
		x = self.monitoringData
		s = self.standardData
		b = np.zeros((n, k))	# 标准矩阵
		a = np.zeros((m, n))	# 样本矩阵
		for j in range(0, n):
			flag = 0
			for l in range(0, k - 1):		# 判断等级数值是递增还是递减的
				if s[j][l] < s[j][l+1]:
					break
				elif s[j][l] > s[j][l+1]:
					flag = 1
					break
			if flag == 0:	# 指标越大，污染越重
				for l in range(0, k):	# 标准矩阵
					b[j][l] = (s[j][k-1] - s[j][l]) / (s[j][k-1] - s[j][0])
				for i in range(0, m):		#样本矩阵
					if x[i][j] <= s[j][1]:
						a[i][j] = 1
					elif x[i][j] >= s[j][k-1]:
						a[i][j] = 0
					else:
						a[i][j] = (s[j][k-1] - x[i][j]) / (s[j][k-1] - s[j][0])
			else:			# 指标越大，污染越轻
				for l in range(0, k):	#样本矩阵
					b[j][l] = (s[j][l] - s[j][k-1]) / (s[j][0] - s[j][k-1])
				for i in range(0, m):
					if x[i][j] >= s[j][1]:
						a[i][j] = 1
					elif x[i][j] <= s[j][k-1]:
						a[i][j] = 0
					else:
						a[i][j] = (x[i][j] - s[j][k-1]) / (s[j][0] - s[j][k-1])
		'''
		print("标准矩阵")
		print(b)
		print("\n")
		print("样本矩阵")
		print(a)

		print("\n------------------------------------------------------------\n")
		'''
		# 计算关联度
		ef = np.zeros((m, k, n))		# 初始化关联离散函数矩阵
		'''
		print("关联离散函数，选择幂函数法请输入1，选择极差法请输入2")
		chose = input()
		while chose != 1 and chose != 2:
		chose = input("输入错误，请重新选择：")
		if chose == 1:	# 幂函数法
			print("幂函数法")
			c = input("c的取值（1-4）：")
			for i in range(0, m):
				for l in range(0, k):
					for j in range(0, n):
						t = abs(b[j][l] - a[i][j])
						ef[i][l][j] = (1 - t) / (1 + t)
			for i in range(0, m):
				print(ef[i])
		elif chose == 2:
			print("极差法")
			p = input("分辨系数=")
			for i in range(0, m):
				min = -1
				max = 
		'''
		# print("幂函数法")
		# c = int(input("c的取值（1-4）："))
		c = 2
		for i in range(0, m):
			for l in range(0, k):
				for j in range(0, n):
					t = math.pow(abs(b[j][l] - a[i][j]), c)
					ef[i][l][j] = (1 - t) / (1 + t)
					# ef[i][l][j] = 1 - abs(b[j][l] - a[i][j])
		'''
		for i in range(0, m):
			print(ef[i])
		'''
		# print("\n------------------------------------------------------------\n")

		ss = [0]*n
		for j in range(0, n):
			t = 0
			for l in range(0, k):
				t += s[j][l]
			ss[j] = t / k
		
		w0 = np.zeros((m, n))
		w1 = np.zeros((m, n))
		sumw = np.zeros(m)
		for i in range(0, m):
			for j in range(0, n):
				w0[i][j] = x[i][j] / ss[j]
				sumw[i] += w0[i][j]
			
		for i in range(0, m):
			for j in range(0, n):
				w1[i][j] = w0[i][j] / sumw[i]
			
		fk = np.zeros((m, k))
		for i in range(0, m):
			for l in range(0, k):
				t = 0
				for j in range(0, n):
					t += w1[i][j] * ef[i][l][j]
				fk[i][l] = t
		
		ans = [0]*m
		for i in range(0, m):
			# print(fk[i], end = " ")
			index = 1
			mint = -1
			for l in range(0, k):
				if fk[i][l] >= mint:
					mint = fk[i][l]
					index = l + 1
			ans[i] = index
			# print("评价等级为%d级" % index)
		return ans
		
	# 模糊综合评价法
	def Fuzzy_Comprehensive_Evaluation(self):
		m = self.numOfMonpoint
		n = self.numOfElement
		k = self.numOfLevel
		x = self.monitoringData
		s = self.standardData
		x1 = x.T
		r = np.zeros((m, n, k))
		for i in range(0, m):
			for j in range(0, n):
				flag = 0
				for l in range(0, k - 1):		# 判断等级数值是递增还是递减的
					if s[j][l] < s[j][l+1]:
						break
					elif s[j][l] > s[j][l+1]:
						flag = 1
						break
				if flag == 0:
					for l in range(0, k):
						if l == 0:
							if x[i][j] <= s[j][l]:		# 第1级
								r[i][j][l] = 1
							elif x[i][j] >= s[j][1]:
								r[i][j][l] = 0
							else:
								r[i][j][0] = (x[i][j] - s[j][1]) / (s[j][0] - s[j][1])
						elif l == k - 1:
							if x[i][j] <= s[j][l-1]:		# 第k级
								r[i][j][l] = 0
							elif x[i][j] >= s[j][l]:
								r[i][j][l] = 1
							else:
								r[i][j][l] = (x[i][j] - s[j][l-1]) / (s[j][l] - s[j][l-1])
						else:
							if x[i][j] <= s[j][l-1] or x[i][j] >= s[j][l+1]:		# 第2,3...,k-1级
								r[i][j][l] = 0
							elif x[i][j] > s[j][l-1] and x[i][j] < s[j][l]:
								r[i][j][l] = (x[i][j] - s[j][l-1]) / (s[j][l] - s[j][l-1])
							else:
								r[i][j][l] = (x[i][j] - s[j][l+1]) / (s[j][l] - s[j][l+1])
				else:
					for l in range(0, k):
						if l == 0:
							if x[i][j] >= s[j][l]:		# 第1级
								r[i][j][l] = 1
							elif x[i][j] <= s[j][1]:
								r[i][j][l] = 0
							else:
								r[i][j][0] = (x[i][j] - s[j][1]) / (s[j][0] - s[j][1])
						elif l == k - 1:
							if x[i][j] >= s[j][l-1]:		# 第k级
								r[i][j][l] = 0
							elif x[i][j] <= s[j][l]:
								r[i][j][l] = 1
							else:
								r[i][j][l] = (x[i][j] - s[j][l-1]) / (s[j][l] - s[j][l-1])
						else:
							if x[i][j] >= s[j][l-1] or x[i][j] <= s[j][l+1]:		# 第2,3...,k-1级
								r[i][j][l] = 0
							elif x[i][j] < s[j][l-1] and x[i][j] > s[j][l]:
								r[i][j][l] = (x[i][j] - s[j][l-1]) / (s[j][l] - s[j][l-1])
							else:
								r[i][j][l] = (x[i][j] - s[j][l+1]) / (s[j][l] - s[j][l+1])
		'''
		for i in range(0, m):
			print(r[i])

		print("\n------------------------------------------------------------\n")
		'''
			
		w = np.zeros(n)
		e = np.zeros((n, m))
		sume = np.zeros(n)
		for i in range(0, n):
			for j in range(0, m):
				e[i][j] = (max(x1[i]) - x1[i][j]) / (max(x1[i]) - min(x1[i]))	# 归一化
				sume[i] += e[i][j]
			# fq = np.zeros((n, m))
			# print(e)
			# print(sume)
		h = [0]*n
		sumh = 0
		for i in range(0, n):
			t = 0
			for j in range(0, m):
				fq = (e[i][j] + 1) / (sume[i] + 1)
				# print(fq)
				t += fq * math.log(fq)
			h[i] = (-1) * t / math.log(m)
			sumh += h[i]
		for i in range(0, n):
			w[i] = (1 - h[i]) / (n - sumh)

		# print(w)
		# print(r[0])
		ans = [0]*m
		for i in range(0, m):
			b0 = np.dot(w, r[i])
			# print(b0, end = " ")
			mint = -1
			index = 0
			for l in range(0, k):
				if b0[l] >= mint:
					mint = b0[l]
					index = l + 1
			ans[i] = index
			# print("为第%d级" % index)
		return ans

