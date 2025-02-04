import pandas as pd
import os
import numpy as np

# 所有社交媒体类型
social_media_types = [
    "TWITTER", "TUMBLR", "MASTODON", "MATTERMOST", "SLACK", "LINKEDIN", "MEETUP", "FACEBOOK",
    "INSTAGRAM", "DISCORD", "YOUTUBE", "GITHUB", "GITLAB", "GIT", "WEBSITE", "DISCOURSE",
    "PIXELFED", "GHOST", "PEERTUBE", "TIKTOK", "TWITCH"
]

# 初始化字典来存储每个社交媒体类型的数据
social_media_data = {media: [] for media in social_media_types}

# 读取social_media_collective_data.csv中的数据
social_media_df = pd.read_csv('../../data/social_media_collective_data.csv')

# 遍历每个项目，查看其社交媒体链接
for _, row in social_media_df.iterrows():
    slug = row['slug']
    name = row['name']

    # 遍历所有社交媒体类型
    for media in social_media_types:
        # 获取当前社交媒体类型的链接
        sociallink_url = row.get(f'{media}-url', None)

        # 如果链接不为空且不是NaN时，才将该项目的信息加入到对应的社交媒体数据列表中
        if sociallink_url and sociallink_url != 'nan' and pd.notna(sociallink_url):
            social_media_data[media].append({
                "slug": slug,
                "name": name,
                f"{media.lower()}-url": sociallink_url  # 使用小写的社交媒体类型作为列名
            })

# 将每个社交媒体的数据保存为对应的CSV文件
for media, data in social_media_data.items():
    # 只有当该社交媒体有数据时才保存文件
    if data:
        media_df = pd.DataFrame(data)
        # 去重，保留唯一行
        media_df = media_df.drop_duplicates()
    else:
        # 如果没有数据，创建一个空的DataFrame，只包含列名
        media_df = pd.DataFrame(columns=["slug", "name", f"{media.lower()}-url"])

    # 保存 CSV 文件到medium文件夹
    media_df.to_csv(f'../../data/medium/{media.lower()}.csv', index=False, encoding='utf-8')
    #print(f"{media} 数据已保存为 medium/{media.lower()}.csv")
