# Security Policy

## 支持的版本

| 版本 | 支持情况 |
| --- | --- |
| main 分支 | ✅ 持续支持 |

## 报告漏洞

请**不要**通过公开 issue 报告安全问题。

请通过 GitHub 的[私有漏洞报告](https://github.com/sunbinbin1991/sunbinbin1991.github.io/security/advisories/new)提交，或直接联系维护者。

我会尽快响应，通常在 7 天内给出初步反馈。

## 这个项目的攻击面

需要说明的是，本项目是一个**纯静态页面**，攻击面很小：

- **构建脚本** `_data/build.py` — 在 GitHub Actions 中运行，使用只读的 `GITHUB_TOKEN`
- **前端** `index.html` — 无后端、无数据库、无用户输入处理
- **数据来源** — 仅从 `api.github.com` 拉取公开数据

页面渲染仓库描述、README 等外部内容时，所有插入 DOM 的字段都经过 `esc()` HTML 转义。

如果你发现某处未转义导致 XSS，欢迎私下报告，修好后我们会在 issue 里致谢（如果你愿意）。