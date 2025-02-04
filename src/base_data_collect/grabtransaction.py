import requests
import json
import pandas as pd
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

# 交易查询的GraphQL查询，增加了交易金额（amount）
transaction_query = """
query($slug: String, $limit: Int!, $offset: Int!) {
  collective(slug: $slug) {
    slug
    id
    transactions(limit: $limit, offset: $offset) {
      nodes {
        id
        uuid
        type
        kind
        createdAt
        updatedAt
        amount  # 这里加入了交易金额字段
      }
    }
  }
}
"""

# 获取交易数据
def get_transactions(slug, limit=100, offset=0):
    variables = {"slug": slug, "limit": limit, "offset": offset}

    response = requests.post(url, json={"query": transaction_query, "variables": variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            print(f"错误: {slug} - {data['errors']}")
            return None
        else:
            # 提取交易数据
            transactions = data['data']['collective']['transactions']['nodes']
            return transactions
    else:
        print(f"请求失败，状态码：{response.status_code} - {slug}")
        return None


# 读取social_media_collective_data.csv中的slug列
slugs_df = pd.read_csv('../../data/social_media_collective_data.csv')
# 从第3878行开始
slugs_to_query = slugs_df['slug'][3876:].tolist()  # 确保csv文件中的列名是slug

# 每个线程处理的批次大小
batch_size = 100

# 将所有slug分成批次
def divide_into_batches(slugs, batch_size):
    for i in range(0, len(slugs), batch_size):
        yield slugs[i:i + batch_size]

# 并行获取交易数据的函数
def fetch_transactions_for_batch(batch):
    for slug in batch:
        all_transactions = []
        offset = 0
        limit = 100
        while True:
            transactions = get_transactions(slug, limit=limit, offset=offset)
            if transactions:
                all_transactions.extend(transactions)  # 将当前页的数据加入到all_transactions列表中
                offset += limit
                # 如果返回的数据小于limit，表示已获取完所有数据
                if len(transactions) < limit:
                    break
            else:
                print(f"无法获取数据: {slug}")
                break
            time.sleep(1)  # 避免请求过多，休眠1秒

        # 将每个slug的交易数据保存为单独的JSON文件
        filename = f"../../data/transactions/{slug}_transactions.json"
        with open(filename, 'w', encoding='utf-8') as f:
            # 如果没有交易数据，保存空的JSON文件
            if all_transactions:
                json.dump(all_transactions, f, ensure_ascii=False, indent=4)
            else:
                json.dump([], f, ensure_ascii=False, indent=4)  # 保存空的交易数据列表
        print(f"{slug} 的交易数据已保存为 {filename}")


# 使用ThreadPoolExecutor并行处理每个批次
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # 划分批次并提交任务到线程池
    batches = list(divide_into_batches(slugs_to_query, batch_size))
    futures = [executor.submit(fetch_transactions_for_batch, batch) for batch in batches]

# 结束后所有数据会被保存到相应的文件中
