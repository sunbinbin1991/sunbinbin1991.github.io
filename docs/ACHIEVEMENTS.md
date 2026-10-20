# GitHub 成就获取行动手册

> 目标账号：`sunbinbin1991` ｜ 诊断时间：2026-10-20
> 结论：**成就为空的根因是「所有提交直推 main，从无被合并的 PR」**，不是缺少作品。

---

## 一、诊断结论（基于实测，非推测）

| 维度 | 实测结果 | 来源 |
| --- | --- | --- |
| 账号注册 | 2015 年 | GitHub API `/users/sunbinbin1991` |
| 公开仓库 | 68 个（21 原创 + 45fork） | `/users/sunbinbin1991/repos` |
| 本月提交 | 61 次，全部在 `sunbinbin1991.github.io` | `git log` + 个人主页 |
| **被合并的 PR** | **0** | 提交信息全为 `deploy:` / `chore:` 直推 |
| Achievements 徽章 | **0 枚** | 个人主页 Achievements 区为空 |

GitHub 的成就全部绑定**协作事件**（PR 合并、issue 关闭、star 阈值），
**直接 push 不产生任何成就计数**。这是「作品很多但徽章为零」的通用成因。

---

## 二、已完成的工程改动（真实修复，非刷量）

| 缺陷 | 实测复现 | 修复 | 验证结果 |
| --- | --- | --- | --- |
| 实时路径不翻页 | 150 仓库只显示 100，丢 6225 stars | `fetchAllRepos()` + `MAX_REPO_PAGES=5` 兜底 | 修复后 0 丢失 ✓ |
| 总数标签不刷新 | 实时拉取后仍显示启动时数字 | 移入 `renderTotal()` 纳入 `renderAll()` | 调用链已含 ✓ |
| README 截图被注释 | 图在 329KB 但 `<!-- -->` 住 | 启用并转 JPEG q85 | 329KB → 121KB（省 63%）✓ |

补充：CONTRIBUTING.md、PR 模板、issue 模板、CODE_OF_CONDUCT、SECURITY、CI workflow、.gitignore。

验证手段：Node `--check` 语法检查通过；CI 的三项检查本地复现全过；
分页逻辑用 150 仓库 / 68 仓库 / 700 仓库三档用例回测。

---

## 三、成就路径拆解

### 已具备条件，只差临门一脚

#### Pull Shark（默认档）· 2 个 PR 合并进默认分支
**难度：最低** ｜ 分支已推好，点两次即可达成

1. 打开下方链接创建 PR → 合并
   https://github.com/sunbinbin1991/sunbinbin1991.github.io/pull/new/fix/pagination-and-contrib-infra
2. 再建一个小 PR（例如给 `LANG_COLORS` 补配色、或补一个语言）→ 合并

> **关键**：必须**你提、你合、且合进 `main`**。
> 分支已推好：https://github.com/sunbinbin1991/sunbinbin1991.github.io/tree/fix/pagination-and-contrib-infra
>
> **提醒**：2026 年 GitHub 对「自己开仓库自己提自己合并」的刷分路径有反作弊折扣。
> 所以长期看，**真实外部贡献**（给别人的仓库提 PR）才最稳。

#### YOLO · 合并一个未经 review 的 PR
**难度：极低** ｜ 上面第2 个 PR 直接合并（不 Request review）即可

### 需要时间积累

#### Quickdraw · 5 分钟内关闭 issue
开一个 issue → 5 分钟内自己 close。目前仓库无 issue，
可先开一个真实的小 issue（如「XX 语言配色缺失」）再关掉。

#### Starstruck · 单仓库 16 star
当前单仓库最高仅 **6**（faceTracker），本仓库 **2**。
达成路径：README 优化提升转化 + 发到 showcase 渠道
（Hacker News Show HN、Reddit r/webdev、掘金、 Awesome 列表收录）。
**这是唯一无法靠代码改动达成、必须靠外部曝光的成就。**

#### Pair Extraordinaire · PR 中 co-author 一个提交
在 PR 描述里用 `Co-authored-by:` trailer，让协作者被记录。

---

## 四、执行优先级

| 优先级 | 动作 | 预期成就 | 耗时 |
| --- | --- | --- | --- |
| P0 | 合并已推好的 PR | Pull Shark | 2 分钟 |
| P0 | 再提并合一个小 PR | Pull Shark + YOLO | 5 分钟 |
| P1 | 开 issue 后 5 分钟内关闭 | Quickdraw | 2 分钟 |
| P2 | README 曝光推广| Starstruck | 数天 |
| P2 | 给外部仓库提 PR | Open Sourcerer + 稳定计数 | 长期 |

---

## 五、必须手动确认的设置

GitHub 成就默认可见，但建议核对一次：

**Settings → Public profile → 勾选**
- ☑ Show Achievements on my profile

同时确认仓库 **Settings → General → Features → Issues 已启用**（当前已启用）。

---

## 六、成就刷新的延迟

【实测/社区共识】徽章**不是实时的**，合并后通常需**24–48 小时**
由后台批处理写入 profile。若超时不出现，切换一次
「Show Achievements」开关可强制刷新缓存。

---

## 七、一句话总结

**别去刷成就，先修工程。** 这次改的两个缺陷是实测复现的真实问题，
走 PR 流程修它们，Pull Shark 自然到手；
Starstruck 则必须靠真实曝光 —— 那才是这个仓库值得争取的东西。