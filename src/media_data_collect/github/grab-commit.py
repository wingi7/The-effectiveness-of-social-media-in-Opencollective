import requests
import json
import pandas as pd
import os
import time

# GitHub的API基础URL
github_api_url = "https://api.github.com/repos"
access_token = "xxxxxxx"

# 设置请求头
headers = {
    "Authorization": f"token {access_token}"
}

# 读取CSV文件，假设文件名为github.csv
df = pd.read_csv("../../../data/medium/github.csv")

# 创建commits存储目录，如果没有的话
if not os.path.exists("../../../data/medium/github/commits"):
    os.makedirs("../../../data/medium/github/commits")

# 提取GitHub仓库的URL和项目slug
for _, row in df.iterrows():
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
            if len(parts) == 2:
                owner, repo = parts[0], parts[1]
            else:
                owner = parts[0]
                repo = None  # 这里没有repo名，后续处理时需要获取组织下的所有仓库
        else:
            print(f"跳过无效URL: {github_url} 的 {slug}")
            continue
        # 如果是组织（没有repo），获取组织下所有仓库
        if repo is None:
            org_repos_url = f"https://api.github.com/orgs/{owner}/repos"
            response = requests.get(org_repos_url, headers=headers)
            if response.status_code == 200:
                repos = response.json()
                for repo_info in repos:
                    repo = repo_info['name']
                    commits_url = f"{github_api_url}/{owner}/{repo}/commits"
                    commit_response = requests.get(commits_url, headers=headers)
                    if commit_response.status_code == 200:
                        commits = commit_response.json()

                        # 将commits保存为JSON文件
                        filename = f"../../../data/medium/github/commits/{slug}_{repo}_commit.json"
                        with open(filename, 'w', encoding='utf-8') as f:
                            json.dump(commits, f, ensure_ascii=False, indent=4)
                        print(f"{slug} 的{repo}的commits数据已保存为 {filename}")
                    else:
                        print(f"无法获取 {slug} 的{repo}的commits数据，状态码：{commit_response.status_code}")
            else:
                print(f"无法获取 {slug} 的组织仓库，状态码：{response.status_code}")
        else:
            # 处理单个repo
            commits_url = f"{github_api_url}/{owner}/{repo}/commits"
            response = requests.get(commits_url, headers=headers)

            if response.status_code == 200:
                commits = response.json()

                # 将commits保存为JSON文件
                filename = f"../../../data/medium/github/commits/{slug}_commit.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(commits, f, ensure_ascii=False, indent=4)
                print(f"{slug} 的commits数据已保存为 {filename}")
            else:
                print(f"无法获取 {slug} 的commits数据，状态码：{response.status_code}")

    except Exception as e:
        print(f"请求 {slug} 出错: {e}")
    # time.sleep(1)
