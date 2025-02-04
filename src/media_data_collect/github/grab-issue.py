import requests
import json
import pandas as pd
import os
import time

# GitHub的API基础URL
github_api_url = "https://api.github.com/repos"
access_token = "xxxxxx"

# 设置请求头
headers = {
    "Authorization": f"token {access_token}"
}

# 读取CSV文件，假设文件名为github.csv
df = pd.read_csv("../../../data/medium/github.csv")

# 从2437行开始处理
df_to_process = df.iloc[2435:]

if not os.path.exists("../../../data/medium/github/issues"):
    os.makedirs("../../../data/medium/github/issues")

# 提取GitHub仓库的URL和项目slug
for _, row in df_to_process.iterrows():
    slug = row['slug']
    github_url = row['github-url']
    # 如果github_url为空，跳过该行
    if pd.isna(github_url):
        print(f"跳过空的GitHub URL: {slug}")
        continue
    try:
        # 检查URL是否是组织页面，处理没有repo的情况
        if "github.com" in github_url:
            parts = github_url.split('github.com/')[1].split('/')
            if len(parts) == 2:  # 形如 https://github.com/owner/repo
                owner, repo = parts[0], parts[1]
            else:  # 仅有组织（没有repo）的情况
                owner = parts[0]
                repo = None  # 这里没有repo名，后续处理时需要获取组织下的所有仓库
        else:
            print(f"跳过无效URL: {github_url} 的 {slug}")
            continue

        # 如果是组织（没有repo），获取组织下所有仓库
        if repo is None:
            org_repos_url = f"https://api.github.com/orgs/{owner}/repos"
            response = requests.get(org_repos_url, headers=headers)

            # 重试机制：最大重试次数为3次，间隔10秒
            retries = 0
            while response.status_code == 403 and retries < 3:
                print(f"请求过于频繁，状态码：{response.status_code}，正在重试... {slug}")
                time.sleep(10)  # 等待10秒后重试
                response = requests.get(org_repos_url, headers=headers)
                retries += 1

            if response.status_code == 200:
                repos = response.json()
                for repo_info in repos:
                    repo = repo_info['name']
                    issues_url = f"{github_api_url}/{owner}/{repo}/issues"
                    issue_response = requests.get(issues_url, headers=headers)

                    retries = 0
                    while issue_response.status_code == 403 and retries < 3:
                        print(f"请求过于频繁，状态码：{issue_response.status_code}，正在重试... {slug}/{repo}")
                        time.sleep(10)  # 等待10秒后重试
                        issue_response = requests.get(issues_url, headers=headers)
                        retries += 1

                    if issue_response.status_code == 200:
                        issues = issue_response.json()

                        # 将issues保存为JSON文件
                        filename = f"../../../data/medium/github/issues/{slug}_{repo}_issue.json"
                        with open(filename, 'w', encoding='utf-8') as f:
                            json.dump(issues, f, ensure_ascii=False, indent=4)
                        print(f"{slug} 的{repo}的issues数据已保存为 {filename}")
                    else:
                        print(f"无法获取 {slug} 的{repo}的issues数据，状态码：{issue_response.status_code}")
            else:
                print(f"无法获取 {slug} 的组织仓库，状态码：{response.status_code}")
        else:
            # 处理单个repo
            issues_url = f"{github_api_url}/{owner}/{repo}/issues"
            response = requests.get(issues_url, headers=headers)

            retries = 0
            while response.status_code == 403 and retries < 3:
                print(f"请求过于频繁，状态码：{response.status_code}，正在重试... {slug}")
                time.sleep(10)  # 等待10秒后重试
                response = requests.get(issues_url, headers=headers)
                retries += 1

            if response.status_code == 200:
                issues = response.json()

                # 将issues保存为JSON文件
                filename = f"../../../data/medium/github/issues/{slug}_issue.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(issues, f, ensure_ascii=False, indent=4)
                print(f"{slug} 的issues数据已保存为 {filename}")
            else:
                print(f"无法获取 {slug} 的issues数据，状态码：{response.status_code}")
    except Exception as e:
        print(f"请求 {slug} 出错: {e}")
