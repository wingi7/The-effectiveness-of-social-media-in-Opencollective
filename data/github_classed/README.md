**关于GitHub的数据是通过GitHub API获取得到issues文件，批量处理json生成csv文件，并进行数据清洗。**

**通过调用deepseek api使用deepseek-chat模型对title和body数据进行目的预测，同时使用fasttext库及预训练模型对语言进行分类,对置信度小于50%的数据语言标注为unknown。**