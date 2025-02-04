import pandas as pd

# 读取CSV文件
df = pd.read_csv('../../data/slugs/project_slugs.csv')

# 删除空行（空值或者只有空格的行）
df = df.dropna(subset=['Slug'])

# 将清理后的数据重新保存到新的CSV文件中
df.to_csv('cleaned_project_slugs.csv', index=False)

print("空行已删除，并保存为 cleaned_project_slugs.csv")
