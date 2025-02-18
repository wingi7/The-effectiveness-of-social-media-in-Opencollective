## 研究问题
了解在 Twitter/X 上提及 GitHub Sponsors 个人资料的现状和影响。研究的提出的观点不仅对学术理解有贡献，同时也为开发者、赞助者和类似 GitHub 的平台提供了实践意义。
#### 同时回答下面的问题
#### RQ1. : GitHub Sponsors 个人资料在 Twitter/X 上是如何被讨论的？
**1.1：提到 GitHub Sponsors 的推文有哪些特征？**1
分析推文的语言、账户类型和编程语言，帮助开发者制作更具吸引力的内容，从而吸引潜在赞助者。

**1.2：谁会在 Twitter/X 上提及 GitHub Sponsors 个人资料？**
了解谁在提及这些资料，从而帮助制定更有针对性的赞助策略。

**1.3：GitHub Sponsors 个人资料被提及的语境是什么？**
分析这些推文出现的背景，为开发者制定吸引赞助的策略提供参考。

**1.4：GitHub Sponsors 个人资料在 Twitter/X 上的提及时间是什么时候？**
研究提及的时机，帮助开发者确定最佳的发布推文时段以增加赞助机会。

#### RQ2: 在 Twitter/X 上提及 GitHub Sponsors 个人资料的影响是什么？
**2.1：GitHub Sponsors 个人资料提及的推文在 Twitter/X 上的反响如何？**
分析这些推文的互动情况（如点赞、转发和评论）。

**2.2：推文对 GitHub Sponsors 个人资料的讨论是怎样的？**
分析推文和回复内容，为开发者提供更好的社区互动策略。

**2.3：提到 GitHub Sponsors 个人资料的推文对赞助有何影响？**
使用因果分析方法定量评估提及推文对赞助数量的具体影响。

## 研究方法

采用定性和定量的分析方法

1. **数据收集**
- 来源：通过 Twitter/X Academic Research Access 收集从 2019 年 5 月（GitHub Sponsors 推出）到 2022 年 4 月的推文。
- 关键词：使用 "github.com/sponsors/" 检索所有包含 GitHub Sponsors 链接的推文，共收集到 11,582 条推文。
- 语言筛选：91% 的推文是英文，为保证分析一致性，仅选取英文推文（共 10,531 条）进行后续分析（除了RQ1.1）。
2. **定量分析**
- 推文特征：分析推文的语言分布、账户类型（个人或组织）和开发者主要使用的编程语言。
- 时间段活动分析：通过 GitHub API 分析开发者在发布推文前一周、发布当周以及发布后一周的活动变化（如提交代码、创建项目）。
- 推文互动分析：比较包含 GitHub Sponsors 链接的推文与其他赞助平台（如 Patreon、Open Collective）的互动情况。
3. **定性分析**
随机选取 351 条推文，通过手动标注分析推文的内容和语境：
- 行为分类：推文作者是“寻求赞助的人”还是“赞助者”。
- 语境分类：推文的目的是广告、表达感谢、或其他（如项目更新、发布新功能等）。
- 回复内容：分析推文下的回复类型（支持、感谢、仅使用表情符号等）。
4. **因果推断**
- 方法：使用倾向评分匹配法（PSM）评估提到 GitHub Sponsors 的推文对赞助者数量的影响。
- 对照组：选取没有发推文的开发者作为对照组，并与发推文的开发者进行比较。

## 结果
#### RQ1. : GitHub Sponsors 个人资料在 Twitter/X 上是如何被讨论的？
**1.1：提到 GitHub Sponsors 的推文有哪些特征？1**
- 推文语言：大部分推文是英文（94%）。其余语言中，日语占 5%，其他语言如西班牙语占比极小。1
- 账户类型：推文中提到的 GitHub Sponsors 个人资料主要是个人账户（87%），其余为组织账户（13%）。0
- 编程语言：JavaScript 是最常见的主编程语言，占个人账户的 25% 和组织账户的 18%。Python 和 PHP 分别在个人账户中占 10% 和 9%，在组织账户中占 9%。1

**1.2：谁会在 Twitter/X 上提及 GitHub Sponsors 个人资料？**
- 提及者：52% 的推文由希望获得赞助的开发者发布，48% 的推文由赞助者再发布。1角色多一点
- 赞助者的角色：赞助者可能会提及他们所依赖的项目开发者的 GitHub Sponsors 个人资料。

**1.3：GitHub Sponsors 个人资料被提及的语境（目的）是什么？1**
常见语境：
- 广告：21% 的推文是开发者宣传自己或他人的 GitHub Sponsors 个人资料。
- 感谢捐赠：10% 的推文对赞助者表示感谢。
- 其他：推文还包括提到新功能（3%）、更新（2%）以及可持续性需求（1%）。

**1.4：GitHub Sponsors 个人资料在 Twitter/X 上的提及时间是什么时候？1**
- 无特定时间：45% 的推文没有明确提及发布的时机。
- 启动时：18% 的推文在 GitHub Sponsors 个人资料激活时发布。
- 捐赠相关：10% 的推文在收到捐赠时发布。
- 更新或活动：一些推文在项目更新、发布新功能或组织活动时发布。

#### RQ2: 在 Twitter/X 上提及 GitHub Sponsors 个人资料的影响是什么？
**2.1：GitHub Sponsors 个人资料提及的推文在 Twitter/X 上的反响如何？1**
- GitHub Sponsors 推文的互动率（如点赞、转发和回复）低于 Patreon 和 Open Collective。
- 大多数推文没有收到回复，少数推文获得了对捐赠的感谢（8%）。

**2.2：推文对 GitHub Sponsors 个人资料的讨论是怎样的？0**
- 回复中包含对开发者工作的支持（2%）或仅用表情符号表示情感。
- 大部分回复表达了对捐赠或工作的认可。

**2.3：提到 GitHub Sponsors 个人资料的推文对赞助有何影响？1（模型方法）**
- 提及 GitHub Sponsors 的推文平均增加了 1.22 名赞助者。
- 赞助的增加具有统计学意义，但效果因开发者个人情况而异。

#### SUMMARY
- GitHub Sponsors 推文的作用：在 Twitter/X 上提及 GitHub Sponsors 个人资料对增加赞助者数量具有积极影响，且开发者通常在发布推文的当周更加活跃。
- 互动的不足：虽然 GitHub Sponsors 在 Twitter 上的可见性较高，但其互动率低于其他捐赠平台。

## 威胁有效性的因素
1. 编码的主观性
2. 因果推断结果的局限性
3. 推文中包含多个 GitHub Sponsors 个人资料的情况
4. 仅分析包含 GitHub Sponsors 链接的推文
5. 开发者主要编程语言的局限性
6. GitHub Sponsors 推文与其他平台数据规模的差异
7. 外部有效性
   
## 讨论
**研究对不同的利益者有不同的建议**
1. 希望获得赞助的开发者：
    - 在推文中提及 GitHub Sponsors 个人资料可以增加赞助者的数量。这表明社交媒体的使用对吸引赞助至关重要，开发者应积极扩大其在 GitHub 平台以外的网络影响力。
    - 总结了多种推文类型和发布语境，为开发者设计更具吸引力的社交媒体策略提供了参考。
2. 赞助者：
    - 约一半的推文来自赞助者，这表明赞助者对提高开源项目的知名度起到了重要作用。
    - 即使赞助金额较小，赞助者也可以通过社交媒体宣传开发者，从而扩大开发者的影响力，让更多人认识到其优秀的工作。
3. 企业：
    - 企业和开源项目的关系正在发生变化，特别是对开源项目可持续性的关注日益增加。与其仅仅对可持续性问题表示不满，企业可以通过两种方式支持开源项目：
      1. 提供直接的经济支持。
      2. 通过社交媒体宣传与推广相关项目，以增强其知名度。

**未来的工作**
1. 更广泛的社交媒体分析：
    本研究仅分析了 Twitter/X 平台。未来的研究可以扩展到其他社交媒体平台（如 Facebook、Reddit）以获得更全面的见解。

2. 长期影响研究：
    目前尚未明确赞助对开源项目长期可持续性的具体影响，因此需要进一步的研究。

3. 探索其他影响因素：
    推文之外的其他因素可能也会显著影响赞助的获得，例如开发者的项目领域、技术特点或社区建设能力。未来研究可以深入挖掘这些因素。
4. 模板和交互优化：
    GitHub 提供的推文模板对吸引赞助有一定作用，但其互动率较低。未来研究可以探索更有效的推文模板设计以及提高用户互动的策略。

## 结论
该研究表明，通过分析含有 GitHub Sponsors 链接的 10,000 多条推文，社交媒体（Twitter/X）对吸引开源软件项目的赞助者具有显著的积极影响。开发者在发布相关推文的那一周通常对开源项目的贡献更活跃。保持社交媒体活跃的开源开发者能够更容易获得捐赠，从而支持项目的可持续发展，体现了社交媒体和捐赠平台在开源生态系统中的紧密联系。
