# sunbinbin1991.github.io · GitHub 项目汇总网站

基于 GitHub 账号 [sunbinbin1991](https://github.com/sunbinbin1991) 公开数据生成的静态项目汇总网站，部署于 GitHub Pages。

## 在线访问

<https://sunbinbin1991.github.io/>

## 功能

- **账号信息与统计**：仓库数 / 原创数 / Stars / 关注者等
- **⚡ 最新动态**：来自 GitHub 公开活动流（Star / Fork / Push / PR 等），打开页面即实时拉取，并缓存 10 分钟
- **⭐ 精选原创项目**：按 Star 排序
- **全部仓库**：语言、Star、Fork、主题标签、主页链接、更新时间
- **筛选**：关键词搜索、类型（全部 / 原创 / Fork）、语言筛选、5 种排序
- **刷新按钮**：一键从 GitHub API 拉取最新数据；GitHub 限流时自动回退到快照数据

## 目录结构

```
index.html                     网站主页（含实时数据逻辑）
data.js                        数据快照（由 GitHub Actions 每 6 小时自动重建）
.github/workflows/refresh-data.yml   定时刷新工作流
_data/build.py                 数据生成脚本（抓取用户 / 仓库 / 动态并写出 data.js）
```

## 数据如何保持最新

1. **定时任务**：GitHub Actions 每 6 小时运行 `_data/build.py`，重新抓取仓库与动态，自动提交更新 `data.js`（也可在 Actions 页面手动触发）。
2. **实时拉取**：访客打开页面时，浏览器直接从 `api.github.com` 拉取最新仓库与动态（带 10 分钟本地缓存），限流时自动回退到快照。

## 本地重新生成数据

```bash
python _data/build.py   # 重新抓取并生成 data.js（需联网）
```

## 本地预览

直接用浏览器打开 `index.html` 即可（纯静态页面，无需服务器）。
