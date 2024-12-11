# -*- coding: utf-8 -*-
import pandas as pd
import os
from visualization import plot_emg_nature_style

def read_next_file(counter, folder_pattern=r'D:\SEMG-EEG\SEMG-EEG raw\C_{}', file_pattern='C{}_L.csv'):
    """
    读取指定文件夹中的下一个CSV文件。

    Args:
        counter (int): 文件编号计数器。
        folder_pattern (str): 文件夹路径模式。
        file_pattern (str): 文件名模式。

    Returns:
        pd.DataFrame or None: 读取到的数据，如果没有文件则返回None。
    """
    file_path = os.path.join(folder_pattern.format(counter), file_pattern.format(counter))

    # 检查文件是否存在
    if os.path.exists(file_path):
        # 读取CSV文件，跳过前115行
        data = pd.read_csv(file_path, skiprows=115)

        # 打印文件名和所有列名
        print(f"正在读取文件: C{counter}_L.csv")
        print("列名:")
        print(data.columns)

        return data
    else:
        print(f"文件不存在: {file_path}")
        return None

def process_and_extract_emg_data(data):
    """
    从原始数���中提取EMG数据并重命名列。

    Args:
        data (pd.DataFrame): 原始数据。

    Returns:
        pd.DataFrame: 提取并处理后的EMG数据。
    """
    # 提取第一列（时间列）
    time_column = data.iloc[:, 0]

    # 筛选出列名中包含"EMG"的所有列
    emg_columns = data.filter(regex='EMG', axis=1)

    # 合并时间列和筛选出的EMG列
    processed_data = pd.concat([time_column, emg_columns], axis=1)

    # 新的列名列表
    new_column_names = ['time', 'LDe', 'RDe', 'LTA', 'RTA', 'LRA', 'RRA', 'LTi', 'RTi', 
                       'LGa', 'RGa', 'LRF', 'RRF', 'LES', 'RES', 'LMu', 'RMu']

    # 创建一个字典，将当前列名映射到新的列名
    columns_map = {old_name: new_name for old_name, new_name in zip(processed_data.columns, new_column_names)}

    # 使用rename方法更改列名
    processed_data.rename(columns=columns_map, inplace=True)

    return processed_data

# 初始化文件编号计数器
counter = 1

# 读取文件
data = read_next_file(counter)

if data is not None:
    # 处理EMG数据
    emg_data = process_and_extract_emg_data(data)

    # 保存EMG数据
    output_file = f'C{counter}_LEMG.CSV'
    emg_data.to_csv(output_file, index=False)
    print(f"EMG数据已保存到: {os.path.abspath(output_file)}")

    # 绘制符合 Nature 期刊风格的 EMG 信号图
    plot_emg_nature_style(
        emg_data=emg_data,
        subject_id=f"C{counter}",
        save_path=os.path.join("D:/SEMG-EEG/figures/nature_quality", f"C{counter}_EMG_signals.tiff")
    )

    # 将文件编号计数器增加为下一轮读取的标准
    counter += 1 