import main

def run_qa():
	print("\n                  水环境质量综合评价系统")
	print("\n------------------------------------------------------------\n")
	print("  使用未确知测度，灰关联分析，模糊综合评价三种模型进行评价")
	print("  输入基本数据文件即可得到结果")
	print("\n------------------------------------------------------------\n")

	while(True):
		main.analysis()
		print("\n------------------------------------------------------------\n")
		print("继续评价其他数据请输入1， 退出请输入2")
		isexit = int(input())
		while isexit != 1 and isexit != 2:
			isexit = int(input("输入错误，请重新输入："))
		if isexit == 2:
			break
			
if __name__ == '__main__':
	run_qa()
