# Contributing

感谢你愿意为这个模板花时间。无论是提一个 bug、补一种语言配色，还是改进文档，都很有价值。

## 快速开始

不需要任何构建工具。本地预览直接双击 `index.html` 即可。

```bash
# 1. Fork 本仓库
# 2. 克隆你的 fork
git clone https://github.com/<你的用户名>/sunbinbin1991.github.io.git
cd sunbinbin1991.github.io

# 3. 建分支
git checkout -b fix/你的改动

# 4. 改完后本地预览 index.html，确认正常
# 5. 提交并推送
git add -A && git commit -m "fix: 简短描述你的改动"
git push origin fix/你的改动
# 6. 在 GitHub 上发 PR，指向 main
```

> 如果你只是想部署自己的个人主页，不需要走 PR 流程 ——
> 直接 Fork 后改 `_data/build.py` 里的 `LOGIN = "sunbinbin1991"` 为你的用户名即可。

## 提交规范

- **一个 PR 只做一件事。** 混在一起的 PR 很难 review。
- **commit message 用祈使句**，前缀标类型：

  | 前缀 | 用途 |
  | --- | --- |
  | `fix:` | 修 bug |
  | `feat:` | 加功能 |
  | `docs:` | 只改文档 |
  | `refactor:` | 重构，不改行为 |
  | `chore:` | 构建 / 依赖等杂项 |

- **改 `data.js` 请不要手动编辑。** 它由 workflow 自动生成，你的改动会在 6 小时内被覆盖。要改数据生成逻辑，请改 `_data/build.py`。

## 代码约定

- `index.html` 是单文件（CSS + JS 内联），**零依赖**是这个模板的核心卖点，请不要引入任何第三方库或构建步骤。
- JS 保持 ES5 风格（`var` + `function`），与现有代码保持一致。
- 所有插入 DOM 的外部数据都要过 `esc()` 转义，避免 XSS。
- 改动后请在浏览器里点一遍「刷新数据」按钮，确认实时路径正常。

## 认领任务

打开 [Issues](../../issues)，找标了 `good first issue` 的。
**先留言认领**，避免两个人做同一件事。

## 需要帮助？

- 提 bug：开 issue，附上浏览器版本 + 复现步骤
- 想讨论功能：开 issue 标注 `discussion`
- 只是聊聊：[Discussions](../../discussions)

---

这个模板的设计目标很简单：**让新用户零成本拿到一个会自动更新的个人主页**。
任何让部署更简单、让页面更好看的改动我们都欢迎。