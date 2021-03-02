# -*- codeing = utf-8 -*-
# @Time : 2021/3/2 10:28
# @Author : wy
# @File : show.py
# @Software : PyCharm

import matplotlib.pyplot as plt
import numpy as np

def showImg(m, l1, l2, l3):
    x = np.arange(m)
    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.bar(x, l1, width=width, label='未确知测度', color='red')
    plt.bar(x + width, l2, width=width, label='灰关联分析', color='deepskyblue')
    plt.bar(x + 2 * width, l3, width=width, label='模糊综合评价', color='green')

    plt.xticks()
    plt.legend(loc="upper left")  # 防止label和图像重合显示不出来
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.ylabel('等级')
    plt.xlabel('监测点')
    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 尺寸
    plt.title("title")
    plt.savefig('result.png')
    plt.show()
