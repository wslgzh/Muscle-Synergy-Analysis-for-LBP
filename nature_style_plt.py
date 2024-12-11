# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def setup_nature_style():
    """
    设置符合Nature期刊的全局绘图样式
    参考: https://www.nature.com/nature/editorial-policies/image-integrity
    """
    
    # 基础设置
    plt.style.use('default')
    
    # 字体设置 (Nature要求使用无衬线字体)
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rcParams['font.size'] = 8
    plt.rcParams['axes.labelsize'] = 8
    plt.rcParams['axes.titlesize'] = 9
    plt.rcParams['xtick.labelsize'] = 7
    plt.rcParams['ytick.labelsize'] = 7
    plt.rcParams['legend.fontsize'] = 7
    
    # 图像质量设置
    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.figsize'] = [3.5, 2.625]  # 89mm (Nature单栏宽度)
    
    # 线宽设置
    plt.rcParams['axes.linewidth'] = 0.5
    plt.rcParams['lines.linewidth'] = 0.8
    plt.rcParams['grid.linewidth'] = 0.5
    
    # 其他样式设置
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['axes.axisbelow'] = True 