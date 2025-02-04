import json

# 读取有问题的JSON文件
with open('../../data/collectiveInfo/success_collective_data6.json', 'r', encoding='utf-8') as f:
    # 读取文件内容
    content = f.read()

# 修复文件：在每两个项目之间添加逗号
fixed_content = content.replace("}\n{", "},\n{")

# 将修复后的内容转换为JSON对象以确保格式正确
try:
    fixed_data = json.loads(f'[{fixed_content}]')  # 重新包装为一个大数组
except json.JSONDecodeError as e:
    print(f"解析错误: {e}")
    fixed_data = []

# 保存修复后的JSON文件
with open('../../data/collectiveInfo/fixed_file.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_data, f, ensure_ascii=False, indent=4)

print("文件修复完成并保存为 fixed_file.json")
