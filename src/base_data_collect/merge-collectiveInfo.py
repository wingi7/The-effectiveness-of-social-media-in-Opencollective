import json
import glob

# 找到所有的JSON文件
json_files = glob.glob("./collectiveInfo/*.json")  # 替换为你自己的文件路径

# 存储合并后的数据
all_data = []

# 读取每个JSON文件并合并数据
for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # 每个文件可能包含多个collective对象，提取所有数据并添加到all_data
        for item in data:
            if 'data' in item and 'collective' in item['data']:
                all_data.append(item['data']['collective'])

# 保存合并后的数据到一个新的JSON文件
with open('merged_collective_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print(f"所有数据已合并并保存到 merged_collective_data.json")
