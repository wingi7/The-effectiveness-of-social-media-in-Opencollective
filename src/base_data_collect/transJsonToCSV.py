import pandas as pd
import json

# 读取合并后的json文件
with open('../../data/collectiveInfo/merged_collective_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义所有可能的社交媒体类型
social_media_types = [
    "TWITTER", "TUMBLR", "MASTODON", "MATTERMOST", "SLACK", "LINKEDIN", "MEETUP", "FACEBOOK",
    "INSTAGRAM", "DISCORD", "YOUTUBE", "GITHUB", "GITLAB", "GIT", "WEBSITE", "DISCOURSE",
    "PIXELFED", "GHOST", "PEERTUBE", "TIKTOK", "TWITCH"
]

# 创建一个空的DataFrame，包含所有需要的列
columns = ["slug", "name", "githubHandle"]
for media in social_media_types:
    columns.append(f"{media}-url")
    columns.append(f"{media}-createdAt")
    columns.append(f"{media}-updatedAt")

df = pd.DataFrame(columns=columns)

# 临时存储数据
rows = []

# 提取每个项目的数据
for item in data:
    # 打印整个项来查看数据结构
    print("Item data:", item)

    # 获取项目的基本信息
    row = {
        "slug": item.get("slug", ""),
        "name": item.get("name", ""),
        "githubHandle": item.get("githubHandle", "")
    }

    # 获取社交媒体链接并填充
    social_links = item.get("socialLinks", [])
    # print("SocialLinks:", social_links)  # 打印socialLinks以便查看其结构

    # 填充社交媒体数据
    for media in social_media_types:
        media_links = [link for link in social_links if link["type"] == media]
        if media_links:
            link = media_links[0]  # 假设一个社交媒体类型最多有一个链接
            row[f"{media}-url"] = link.get("url", "")
            row[f"{media}-createdAt"] = link.get("createdAt", "")
            row[f"{media}-updatedAt"] = link.get("updatedAt", "")
        else:
            row[f"{media}-url"] = ""
            row[f"{media}-createdAt"] = ""
            row[f"{media}-updatedAt"] = ""

    # 打印每一行数据用于调试，确保数据正确
    # print("Row data:", row)

    # 将数据添加到临时列表中
    rows.append(row)

# 使用concat将所有行合并到DataFrame中
df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

# 保存DataFrame为CSV文件
df.to_csv('social_media_collective_data.csv', index=False, encoding='utf-8')

print("数据已保存为 social_media_collective_data.csv")
