import os
import pandas as pd
import matplotlib.pyplot as plt

# 社交媒体类型
social_media_types = [
    "TWITTER", "TUMBLR", "MASTODON", "MATTERMOST", "SLACK", "LINKEDIN", "MEETUP", "FACEBOOK",
    "INSTAGRAM", "DISCORD", "YOUTUBE", "GITHUB", "GITLAB", "GIT", "WEBSITE", "DISCOURSE",
    "PIXELFED", "GHOST", "PEERTUBE", "TIKTOK", "TWITCH"
]

# 初始化字典存储社交媒体的行数
social_media_counts = {}

# 遍历每个社交媒体的CSV文件，统计行数
for media in social_media_types:
    file_path = f'../../data/medium/{media.lower()}.csv'

    if os.path.exists(file_path):
        # 读取 CSV 文件并统计行数
        df = pd.read_csv(file_path)
        # 统计非空url的行数
        non_empty = df[media.lower() + '-url'].dropna().shape[0]
        social_media_counts[media] = non_empty
    else:
        # 如果没有该文件则计为0
        social_media_counts[media] = 0

# 将统计数据转化为DataFrame
count_df = pd.DataFrame(list(social_media_counts.items()), columns=['Social Media', 'Count'])

# 绘制饼图
plt.figure(figsize=(10, 7))
# 绘制饼图，不使用直接的labels，避免图上的文字
plt.pie(count_df['Count'], startangle=140, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')

# 添加标题
plt.title('Social Media Usage')
plt.axis('equal')  # 使得饼图为圆形

# 手动添加注释到饼图外部
plt.legend(
    count_df['Social Media'] + " - " + count_df['Count'].astype(str),
    loc="center left", bbox_to_anchor=(1, 0.5), title="Types"
)

plt.show()

# 绘制条形图
plt.figure(figsize=(10, 6))
plt.barh(count_df['Social Media'], count_df['Count'], color='skyblue')
plt.title('Social Media Usage')
plt.show()

# 保存统计结果为CSV文件
count_df.to_csv('../../data/social_media_usage_statistics.csv', index=False, encoding='utf-8')
