# encoding:utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
pylab.mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def draw_heatmap(data, xlabels, ylabels):
    """
    画热力图函数
    :param data: 数据，是一个二维数组
    :param xlabels: 横轴坐标名称
    :param ylabels: 纵轴坐标名称
    :return: null
    """

    figure = plt.figure()  # 画布特征，默认即可，可根据喜好调整
    ax = figure.add_subplot()  # 添加一个子画布
    ax.set_xticks(range(len(xlabels)))  # 横坐标长度
    ax.set_xticklabels(xlabels)  # 横坐标标签
    ax.set_yticks(range(len(ylabels)))  # 纵坐标长度
    ax.set_yticklabels(ylabels)  # 纵坐标标签

    vmax = data[0][0]
    vmin = data[0][0]

    #  获取二维数组中的 最大和最小两个值
    for i in data:  # 遍历二维数组，每次i获取到的是一维数组
        for j in i:  # 遍历一维数组，每次获取到的是一个数字
            if j > vmax:
                vmax = j
            if j < vmin:
                vmin = j

    cmap = cm.Reds  # 图像的颜色
    # interpolation 用来控制显示，参考https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html?highlight=interpolation
    map = ax.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)
    plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)  # 添加右侧的色带
    plt.xticks(rotation=90)  # 横轴将字体进行旋转 90 度
    plt.yticks(rotation=360)  # 纵轴将字体进行旋转 0 度
    plt.show()  # 显示图像

def get_labels(num,label):
    '''
    获取一个数组
    :param num: 数量
    :param label: 标签前缀
    :return: 数组
    '''
    arr = []
    for i in range(0, num):
        arr.append(label + str(i))
    return arr

# main 函数，程序的入口
if __name__ == '__main__':
    # 从Excel 中读取数据
    dataFrame = pd.read_excel('E:\\GEO_DOC\\2020年6月份\\月\\allRes2.xlsx', sheet_name="allRes2", encoding='gbk')
    # 从 dataFrame 中提取三行数据，列为mixedProportion，fromWin，toWin
    # 根据需求提取数据
    val1 = dataFrame.head(10)[['mixedProportion', 'fromWin', 'toWin']]

    # 坐标轴坐标名称，要和数据对的上哈
    xlabels = get_labels(val1.shape[1], "x")  # shape 输出数组的行和列数
    ylabels = get_labels(val1.shape[0], "y")
    # 执行画热泪图的函数
    draw_heatmap(val1.values, xlabels, ylabels)
