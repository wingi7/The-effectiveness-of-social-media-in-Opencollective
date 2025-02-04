# 文件结构

其中media存储的是媒体相关的数据

```
data
├─ 📁media        	# 社交媒体相关的数据
│  ├─ 📁tables		# 表格，存储含有该sociallink的项目，文件名表示sociallink的type
│  │  ├─ 📄discord.csv
│  │  ├─ 📄discourse.csv
│  │  ├─ 📄facebook.csv
│  │  ├─ 📄ghost.csv
│  │  ├─ 📄git.csv
│  │  ├─ 📄github.csv
│  │  ├─ 📄gitlab.csv
│  │  ├─ 📄instagram.csv
│  │  ├─ 📄linkedin.csv
│  │  ├─ 📄mastodon.csv
│  │  ├─ 📄mattermost.csv
│  │  ├─ 📄meetup.csv
│  │  ├─ 📄peertube.csv
│  │  ├─ 📄pixelfed.csv
│  │  ├─ 📄slack.csv
│  │  ├─ 📄tiktok.csv
│  │  ├─ 📄tumblr.csv
│  │  ├─ 📄twitch.csv
│  │  ├─ 📄twitter.csv
│  │  ├─ 📄website.csv
│  │  └─ 📄youtube.csv
│  └─ 📄github.zip	# 含有github的项目的相关数据
├─ 📁RQ1
│  ├─ 📄social_media_usage_column.png		#社交媒体使用情况的柱形图
│  ├─ 📄social_media_usage_pie.png		#饼形图
│  └─ 📄social_media_usage_statistics.csv	#对社交媒体使用情况的统计
├─ 📁slugs		#从opencollective上获取项目slug时产生的相关文件
│  ├─ 📄cleaned_project_slugs.csv
│  ├─ 📄failed_slugs.csv
│  └─ 📄project_slugs.csv
├─ 📄collectiveInfo.zip	#opencollective上项目的相关信息
├─ 📄README.md
├─ 📄social_media_collective_data.csv	#汇总opencollective上获取的项目的社交媒体信息，主要是社交媒体的url
└─ 📄transaction.zip
```
