import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# 启动Chrome浏览器驱动
driver = webdriver.Chrome()

# 总共的页数
total_pages = 3483

# 打开CSV文件，准备写入数据（只保存slug）
with open('../../data/slugs/project_slugs.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Slug"])  # 写入CSV文件的表头

    # 遍历每一页
    for page in range(total_pages):
        # 构造每一页的URL，动态更新offset参数
        url = f"https://opencollective.com/search?offset={page * 20}&limit=20"
        print(f"正在爬取第{page + 1}页: {url}")

        # 打开当前页面
        driver.get(url)

        time.sleep(14)

        # 获取页面的HTML源代码
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 找到所有项目的链接
        projects = soup.find_all('a', href=True)

        # 存储当前页的有效slug
        page_slugs = []

        # 从第4个链接开始处理，跳过前3个固定链接
        for i, project in enumerate(projects[3:], start=4):
            href = project['href']
            slug = href.split('/')[-1]

            # 跳过无关的链接（如分页链接、帮助链接等）
            if slug.startswith('search') or 'help' in slug or 'signin' in slug:
                continue

            # 检查slug是否已经在当前页列表中，避免重复
            if slug not in page_slugs:
                page_slugs.append(slug)

            # 每页只保留前20个有效项目slug
            if len(page_slugs) >= 20:
                break

        # 将当前页的有效slug添加到CSV文件中
        for slug in page_slugs:
            writer.writerow([slug])  # 每一行保存一个slug

        # 输出当前页面爬取的结果（可选）
        print(f"第{page + 1}页共爬取 {len(page_slugs)} 个项目slug")

# 关闭浏览器
driver.quit()
