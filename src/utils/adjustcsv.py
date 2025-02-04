import os
import pandas as pd

# 设置目录路径
folder_path = '../../data/medium'

# 获取该目录下所有的csv文件
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
# 遍历每个csv文件，检查重复行并保存修改后的文件
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    # 去除重复行
    df_cleaned = df.drop_duplicates()

    df_cleaned.to_csv(file_path, index=False, encoding='utf-8')
    print(f"{csv_file} 已清除重复行并保存")
