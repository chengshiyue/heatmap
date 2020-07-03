# encoding:utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pylab
import xlrd

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文乱码
pylab.mpl.rcParams['axes.unicode_minus'] = False  # 防止中文乱码


def draw_heatmap(data, xlabels, ylabels):
    cmap = cm.Blues
    figure = plt.figure(facecolor='w')
    ax = figure.add_subplot(2, 1, 1, position=[0.1, 0.15, 0.8, 0.8])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax = data[0][0]
    vmin = data[0][0]
    for i in data:
        for j in i:
            if j > vmax:
                vmax = j
            if j < vmin:
                vmin = j
    map = ax.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)
    cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    plt.xticks(rotation=90)  # 将字体进行旋转
    plt.yticks(rotation=360)
    plt.show()


dataFrame = pd.read_excel('allRes2.xlsx', sheet_name="allRes2", encoding='gbk')
# 包含每个柱子对应值的序列
val1 = dataFrame.head(3)[['mixedProportion','fromWin','toWin']]

xlabels = ['x1','x2','x3']
ylabels = ['y1', 'y2', 'y3']
draw_heatmap(val1.values, xlabels, ylabels)