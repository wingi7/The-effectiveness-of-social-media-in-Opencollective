import pandas as pd
import requests
import json
import time
import concurrent.futures

# GraphQL端点
url = "https://api.opencollective.com/graphql/v2"

# 你的个人令牌
personal_token = "f2e80a439066362a24289599eaf145349cc03c5a"

# 请求头
headers = {
    "Content-Type": "application/json",
    "Personal-Token": personal_token
}

# 读取cleaned_project_slugs.csv
slugs_df = pd.read_csv('../../data/slugs/cleaned_project_slugs.csv')

# 从第3423行开始爬取
start_index = 3423
slugs_to_query = slugs_df.iloc[start_index:]['Slug']

# GraphQL查询
query = """
query($slug: String) {
  collective(slug: $slug) {
    slug
    name
    githubHandle
    socialLinks {
      type
      url
      createdAt
      updatedAt
    }
  }
}
"""

# 每个线程处理的`slug`数量
batch_size = 100


# 将`slug`划分为多个批次
def chunk_slugs(slugs, batch_size):
    for i in range(0, len(slugs), batch_size):
        yield slugs[i:i + batch_size]


# 并行爬取数据
def fetch_data(batch_slugs):
    batch_data = []
    failed_slugs = []
    for slug in batch_slugs:
        variables = {"slug": slug}
        retries = 0
        while retries < 5:  # 重试5次
            try:
                response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)

                if response.status_code == 200:
                    data = response.json()

                    # 检查是否存在错误
                    if 'errors' in data:
                        print(f"错误: {slug} - {data['errors']}")
                        failed_slugs.append(slug)
                    else:
                        batch_data.append(data)
                        print(f"成功: {slug}")
                    break
                elif response.status_code == 429:
                    print(f"请求过多，状态码: {response.status_code}. 等待10秒钟后重试...")
                    time.sleep(10)  # 等待10秒后重试
                    retries += 1
                else:
                    print(f"请求失败，状态码：{response.status_code} - {slug}")
                    failed_slugs.append(slug)
                    break
            except Exception as e:
                print(f"请求异常，错误: {e}")
                failed_slugs.append(slug)
                break
    return batch_data, failed_slugs


# 保存查询成功的结果到JSON文件
def save_to_file(batch_data, f):
    with open(f, 'a', encoding='utf-8') as file:
        if batch_data:
            for data in batch_data:
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.write("\n")


# 打开文件，准备保存查询成功的结果
with open('../../data/collectiveInfo/success_collective_data6.json', 'w', encoding='utf-8') as f:
    f.write('[')  # 开始数组

    # 使用线程池并行爬取
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:  # 限制为2个线程
        # 将slug列表划分成多个批次
        slugs_batches = list(chunk_slugs(slugs_to_query, batch_size))

        # 创建每个线程的任务
        futures = [executor.submit(fetch_data, batch) for batch in slugs_batches]

        # 获取线程结果并保存
        for future in concurrent.futures.as_completed(futures):
            batch_data, failed_slugs = future.result()
            save_to_file(batch_data, 'success_collective_data6.json')
            print(f"处理完一批数据")

    # 完成后结束数组
    with open('../../data/collectiveInfo/success_collective_data6.json', 'a', encoding='utf-8') as f:
        f.write(']')  # 结束数组

# 保存查询失败的slug到CSV文件
failed_slugs_df = pd.DataFrame(failed_slugs, columns=['Failed Slugs'])
failed_slugs_df.to_csv('failed_slugs.csv', index=False)

print(f"所有查询失败的slug已保存为 failed_slugs.csv")

# import pandas as pd
# import requests
# import json
# import time
# # GraphQL端点
# url = "https://api.opencollective.com/graphql/v2"
# # 你的个人令牌
# personal_token = "f2e80a439066362a24289599eaf145349cc03c5a"
# # 请求头
# headers = {
#     "Content-Type": "application/json",
#     "Personal-Token": personal_token
# }
# # 读取cleaned_project_slugs.csv
# slugs_df = pd.read_csv('cleaned_project_slugs.csv')
# # 从716行（即beehaw-collective之后）开始爬取
# start_index = 3423  # 你可以根据情况调整这个起始行号
# slugs_to_query = slugs_df.iloc[start_index:]['Slug']
# # 存储查询结果
# all_data = []
# # 存储查询失败的slug
# failed_slugs = []
# # GraphQL查询
# query = """
# query($slug: String) {
#   collective(slug: $slug) {
#     slug
#     name
#     githubHandle
#     socialLinks {
#       type
#       url
#       createdAt
#       updatedAt
#     }
#   }
# }
# """
# # 打开文件，准备保存查询成功的结果
# with open('success_collective_data6.json', 'w', encoding='utf-8') as f:
#     f.write('[')  # 开始数组
#     for index, slug in enumerate(slugs_to_query):
#         variables = {"slug": slug}
#
#         retries = 0
#         while retries < 5:  # 重试5次
#             response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
#             if response.status_code == 200:
#                 data = response.json()
#                 if 'errors' in data:
#                     print(f"错误: {slug} - {data['errors']}")
#                     failed_slugs.append(slug)  # 将失败的slug添加到failed_slugs列表中
#                 else:
#                     f.write(',\n')  # 不是第一个元素，加逗号
#                     json.dump(data, f, ensure_ascii=False, indent=4)
#                     f.write("\n")  # 每个查询结果保存为一行
#                     print(f"成功: {slug}")
#                 break
#             elif response.status_code == 429:
#                 print(f"请求过多，状态码: {response.status_code}. 等待10秒钟后重试...")
#                 time.sleep(10)  # 等待10秒后重试
#                 retries += 1
#             else:
#                 print(f"请求失败，状态码：{response.status_code} - {slug}")
#                 failed_slugs.append(slug)
#                 break
#     f.write(']')
# # 保存查询失败的slug到CSV文件
# failed_slugs_df = pd.DataFrame(failed_slugs, columns=['Failed Slugs'])
# failed_slugs_df.to_csv('failed_slugs.csv', index=False)
# print(f"所有查询失败的slug已保存为 failed_slugs.csv")

# import requests
# import json
# import pandas as pd
# import time
#
# # GraphQL端点
# url = "https://api.opencollective.com/graphql/v2"
#
# # 你的个人令牌
# personal_token = "f2e80a439066362a24289599eaf145349cc03c5a"
#
# # 请求头
# headers = {
#     "Content-Type": "application/json",
#     "Personal-Token": personal_token
# }
#
# # 读取cleaned_project_slugs.csv
# slugs_df = pd.read_csv('cleaned_project_slugs.csv')
#
# # 存储查询结果
# all_data = []
#
# # 存储查询失败的slug
# failed_slugs = []
#
# # GraphQL查询
# query = """
# query($slug: String) {
#   collective(slug: $slug) {
#     slug
#     name
#     githubHandle
#     socialLinks {
#       type
#       url
#       createdAt
#       updatedAt
#     }
#   }
# }
# """
#
# # 打开文件，准备保存查询成功的结果
# with open('success_collective_data3.json', 'w', encoding='utf-8') as f:
#     f.write('[')  # 开始数组
#
#     for index, slug in enumerate(slugs_df['Slug']):
#         variables = {"slug": slug}
#
#         retries = 0
#         while retries < 5:  # 重试5次
#             response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
#
#             if response.status_code == 200:
#                 data = response.json()
#
#                 # 检查是否存在错误
#                 if 'errors' in data:
#                     print(f"错误: {slug} - {data['errors']}")
#                     failed_slugs.append(slug)  # 将失败的slug添加到failed_slugs列表中
#                 else:
#                     # 将成功的结果添加到all_data中
#                     f.write(',\n')  # 不是第一个元素，加逗号
#                     json.dump(data, f, ensure_ascii=False, indent=4)
#                     f.write("\n")  # 每个查询结果保存为一行
#                     print(f"成功: {slug}")
#                 break
#             elif response.status_code == 429:
#                 print(f"请求过多，状态码: {response.status_code}. 等待10秒钟后重试...")
#                 time.sleep(10)  # 等待10秒后重试
#                 retries += 1
#             else:
#                 print(f"请求失败，状态码：{response.status_code} - {slug}")
#                 failed_slugs.append(slug)
#                 break
#
#     f.write(']')  # 结束数组
#
# # 保存查询失败的slug到CSV文件
# failed_slugs_df = pd.DataFrame(failed_slugs, columns=['Failed Slugs'])
# failed_slugs_df.to_csv('failed_slugs.csv', index=False)
#
# print(f"所有查询失败的slug已保存为 failed_slugs.csv")
