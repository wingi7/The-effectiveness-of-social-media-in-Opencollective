import requests
import json
import pandas as pd

# GitHub GraphQL API URL
graphql_url = "https://api.github.com/graphql"

# GitHub Personal Access Token
access_token = "xxxxxxx"  # Replace with your GitHub token

# 设置请求头
headers = {
    "Authorization": f"token {access_token}",
    "Content-Type": "application/json"
}

# GitHub GraphQL 查询，用于获取项目的基本信息及活跃度
graphql_query = """
query($owner: String!, $repo: String!) {
  repository(owner: $owner, name: $repo) {
    name
    owner {
      login
    }
    description
    stargazerCount
    forkCount
    watchers {
      totalCount
    }
    issues(states: OPEN) {
      totalCount
    }
    pullRequests(states: OPEN) {
      totalCount
    }
    releases {
      totalCount
    }
    primaryLanguage {
      name
    }
    createdAt
    updatedAt
  }
}
"""

# 获取组织下所有仓库的GraphQL查询
org_repos_query = """
query($org: String!) {
  organization(login: $org) {
    repositories(first: 100) {
      nodes {
        name
      }
    }
  }
}
"""

# 读取github.csv
df = pd.read_csv("../../../data/medium/github.csv")

# 遍历每个GitHub URL，获取对应仓库的基本信息
for _, row in df.iterrows():
    slug = row['slug']
    github_url = row['github-url']

    try:
        # 判断URL是仓库还是组织
        url_parts = github_url.split('github.com/')[1].split('/')

        # 如果是组织页面
        if len(url_parts) == 1:
            org_name = url_parts[0]  # 获取组织名
            print(f"这是一个组织页面，获取 {org_name} 下的仓库信息")

            # 获取组织仓库
            variables = {"org": org_name}
            response = requests.post(graphql_url, headers=headers,
                                     json={"query": org_repos_query, "variables": variables})

            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    repositories = data["data"]["organization"]["repositories"]["nodes"]
                    for repo in repositories:
                        repo_name = repo["name"]
                        variables = {"owner": org_name, "repo": repo_name}

                        # 获取每个仓库的详细信息
                        response = requests.post(graphql_url, headers=headers,
                                                 json={"query": graphql_query, "variables": variables})

                        if response.status_code == 200:
                            data = response.json()
                            if "data" in data:
                                repo_data = data["data"]["repository"]
                                repo_info = {
                                    "slug": slug,
                                    "name": repo_data["name"],
                                    "owner": repo_data["owner"]["login"],
                                    "description": repo_data.get("description", ""),
                                    "stargazerCount": repo_data["stargazerCount"],
                                    "forkCount": repo_data["forkCount"],
                                    "watchersCount": repo_data["watchers"]["totalCount"],
                                    "openIssuesCount": repo_data["issues"]["totalCount"],
                                    "openPullRequestsCount": repo_data["pullRequests"]["totalCount"],
                                    "releasesCount": repo_data["releases"]["totalCount"],
                                    "primaryLanguage": repo_data["primaryLanguage"]["name"] if repo_data[
                                        "primaryLanguage"] else "N/A",
                                    "createdAt": repo_data["createdAt"],
                                    "updatedAt": repo_data["updatedAt"]
                                }

                                # 将仓库信息保存为JSON文件
                                filename = f"../../../data/medium/github/repositories/{slug}_{repo_name}_repo_info.json"
                                with open(filename, 'w', encoding='utf-8') as f:
                                    json.dump(repo_info, f, ensure_ascii=False, indent=4)
                                print(f"{slug} 的 {repo_name} 仓库信息已保存为 {filename}")
                        else:
                            print(f"请求失败，状态码: {response.status_code} - {org_name}/{repo_name}")
                else:
                    print(f"无法获取 {org_name} 下的仓库信息")
            else:
                print(f"请求失败，状态码: {response.status_code} - {org_name}")

        # 如果是普通仓库
        elif len(url_parts) == 2:
            owner, repo = url_parts[0], url_parts[1]

            variables = {"owner": owner, "repo": repo}

            response = requests.post(graphql_url, headers=headers,
                                     json={"query": graphql_query, "variables": variables})

            if response.status_code == 200:
                data = response.json()
                if "data" in data:
                    repo_data = data["data"]["repository"]

                    # 提取仓库信息
                    repo_info = {
                        "slug": slug,
                        "name": repo_data["name"],
                        "owner": repo_data["owner"]["login"],
                        "description": repo_data.get("description", ""),
                        "stargazerCount": repo_data["stargazerCount"],
                        "forkCount": repo_data["forkCount"],
                        "watchersCount": repo_data["watchers"]["totalCount"],
                        "openIssuesCount": repo_data["issues"]["totalCount"],
                        "openPullRequestsCount": repo_data["pullRequests"]["totalCount"],
                        "releasesCount": repo_data["releases"]["totalCount"],
                        "primaryLanguage": repo_data["primaryLanguage"]["name"] if repo_data[
                            "primaryLanguage"] else "N/A",
                        "createdAt": repo_data["createdAt"],
                        "updatedAt": repo_data["updatedAt"]
                    }

                    # 将仓库信息保存为JSON文件
                    filename = f"../../../data/medium/github/repositories/{slug}_repo_info.json"
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(repo_info, f, ensure_ascii=False, indent=4)

                    print(f"{slug} 的仓库信息已保存为 {filename}")
                else:
                    print(f"无法获取 {slug} 的仓库信息")
            else:
                print(f"请求失败，状态码: {response.status_code} - {slug}")
    except Exception as e:
        print(f"处理 {slug} 时出错: {e}")
