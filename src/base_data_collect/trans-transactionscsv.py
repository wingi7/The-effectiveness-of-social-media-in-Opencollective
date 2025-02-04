import os
import json
import pandas as pd

# 文件夹路径
json_folder_path = '../../data/transactions'
csv_folder_path = '../../data/transactions_csv'

# 遍历文件夹中的所有 JSON 文件
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json'):  # 只处理 .json 文件
        json_file_path = os.path.join(json_folder_path, filename)

        # 打开 JSON 文件并读取内容
        with open(json_file_path, 'r', encoding='utf-8') as f:
            transactions_data = json.load(f)

        # 创建一个空的列表，用来存储所有要转换成CSV的数据
        flattened_data = []

        # 检查如果数据为空，则只保存列名
        if transactions_data:
            # 遍历 JSON 数据并展开
            for transaction in transactions_data:
                # 提取基本字段
                base_data = {
                    "id": transaction["id"],
                    "uuid": transaction["uuid"],
                    "type": transaction["type"],
                    "kind": transaction["kind"],
                    "createdAt": transaction["createdAt"],
                    "updatedAt": transaction["updatedAt"]
                }

                # 提取 amount 字段中的数据，并添加到 base_data 中
                amount_data = transaction["amount"]
                base_data.update({
                    "amount_value": amount_data["value"],
                    "amount_currency": amount_data["currency"],
                    "amount_valueInCents": amount_data["valueInCents"]
                })

                # 将每个事务的结果添加到 flattened_data 列表
                flattened_data.append(base_data)
        else:
            # 如果数据为空，则保留列名
            flattened_data = [{
                "id": None,
                "uuid": None,
                "type": None,
                "kind": None,
                "createdAt": None,
                "updatedAt": None,
                "amount_value": None,
                "amount_currency": None,
                "amount_valueInCents": None
            }]
        df = pd.DataFrame(flattened_data)
        # 保存
        csv_file_path = os.path.join(csv_folder_path, f"{filename[:-5]}.csv")
        df.to_csv(csv_file_path, index=False, encoding='utf-8')

# import os
# import json
# import pandas as pd
#
# json_folder_path = '../../data/transactions'
# csv_folder_path = '../../data/transactions_csv'
#
# # 遍历文件夹中的所有 JSON 文件
# for filename in os.listdir(json_folder_path):
#     if filename.endswith('.json'):  # 只处理 .json 文件
#         json_file_path = os.path.join(json_folder_path, filename)
#
#         # 打开 JSON 文件并读取内容
#         with open(json_file_path, 'r', encoding='utf-8') as f:
#             transactions_data = json.load(f)
#         # 创建一个空的列表，用来存储所有要转换成CSV的数据
#         flattened_data = []
#         # 遍历 JSON 数据并展开
#         for transaction in transactions_data:
#             # 提取基本字段
#             base_data = {
#                 "id": transaction["id"],
#                 "uuid": transaction["uuid"],
#                 "type": transaction["type"],
#                 "kind": transaction["kind"],
#                 "createdAt": transaction["createdAt"],
#                 "updatedAt": transaction["updatedAt"]
#             }
#             # 提取 amount 字段中的数据，并添加到 base_data 中
#             amount_data = transaction["amount"]
#             base_data.update({
#                 "amount_value": amount_data["value"],
#                 "amount_currency": amount_data["currency"],
#                 "amount_valueInCents": amount_data["valueInCents"]
#             })
#             # 将每个事务的结果添加到 flattened_data 列表
#             flattened_data.append(base_data)
#         # 将数据转化为 DataFrame
#         df = pd.DataFrame(flattened_data)
#         # 构建对应的 CSV 文件名（与 JSON 文件名相同，但扩展名为 .csv）
#         csv_file_path = os.path.join(csv_folder_path, f"{filename[:-5]}.csv")
#
#         df.to_csv(csv_file_path, index=False, encoding='utf-8')
#
#         print(f"{filename} 的交易数据已保存为 {csv_file_path}")
