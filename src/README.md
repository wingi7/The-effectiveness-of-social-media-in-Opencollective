# 文件结构

```
  src
├─ 📁base_data_collect		#从opencollective上搜集项目并爬取项目的一些基本信息，不包含具体社交媒体
│  ├─ 📄classify-medium.py
│  ├─ 📄grab-detailOC-info.py	#爬取项目基本信息
│  ├─ 📄grab-slugs.py		#爬取项目slug
│  ├─ 📄grabtransaction.py	#爬取项目的交易记录
│  ├─ 📄merge-collectiveInfo.py	#由于网络问题，爬取并不是一次完成，因此保存了多个json文件，需要合并
│  ├─ 📄trans-transactionscsv.py
│  └─ 📄transJsonToCSV.py
├─ 📁media_data_collect		#爬取项目具体的一些sociallink的信息
│  ├─ 📁github			#爬取github相关信息
│  │  ├─ 📄grab-commit.py
│  │  ├─ 📄grab-issue.py
│  │  └─ 📄grab-repoInfo.py
│  └─ 📁twitter
├─ 📁RQ1			#RQ1相关代码
│  └─ 📄media_statistic.py
├─ 📁utils			#一些辅助脚本，与课题不直接关联
│  ├─ 📄fixJson.py
│  ├─ 📄clean-space.py
│  └─ 📄adjustcsv.py
└─ 📄README.md
```

# 部分源码说明

## 基本信息获取

思路是先从opencollective上搜集一些项目的slug，然后根据项目的slug使用opencollective的api（主要是grphql）来获取项目的相关信息。

这部分源码的运行顺序为：

1. grab-slugs.py
2. grab-detailOC-info.py
3. merge-collectiveInfo.py
4. classify-medium.py
5. grabtransaction.py

## 媒体数据获取

### github

根据前一步的项目基本信息可以获知项目github的仓库地址，使用github提供的api（restful 与 graphql）来获取相关信息
