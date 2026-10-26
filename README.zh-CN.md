# Draw.io Ontology：先看有哪些图形，再开始画图

[English](README.md) · [在线浏览图鉴](https://wjh19990923.github.io/drawio-ontology/) · [Agent 入口](AGENTS.md)

这个项目来自一个简单的问题：**“Draw.io 到底有哪些图形和小图标可以用？”**

我们把 drawio-skill 的图形索引渲染为可浏览的图片，再增加 Agent 可查询的分类、能力和路径信息。人可以看图挑元素，Agent 可以查到精确 style、尺寸和可编辑源文件。

这是基于 [drawio-skill](https://github.com/Agents365-ai/drawio-skill) 和 [Draw.io Desktop](https://github.com/jgraph/drawio-desktop) 制作的独立社区图鉴，不是官方产品。

## 包含什么

- 10,446 个官方图形索引条目，以及对应的单个 PNG 预览。
- 44 张联系表：每页集中展示多个图形，另附可编辑 `.drawio` 源文件。
- 135 个由命名空间/样式推导的分组，不等于 135 个官方图形库名称。
- 328 个 AI、LLM 和数据系统品牌 SVG，每个品牌选取一个版本。
- 38 个 skill 脚本的能力索引，以及 11 类图的绘制约定。
- JSONL、JSON-LD、本地查询工具和 Agent 阅读入口。

**联系表和单个 PNG 是同一批内容的两种展示方式。** SVG 品牌图标是额外的素材集。

## 怎么用

1. 打开[在线图鉴](https://wjh19990923.github.io/drawio-ontology/)。也可以点击 GitHub 的 **Code → Download ZIP**，解压后双击 `index.html`，离线浏览。
2. 看联系表快速挑选，或进入分类目录逐个查看。记住图形编号。
3. 通过索引找到 `editable_source`，在 Draw.io 中打开对应源文件，复制图形即可继续编辑。
4. 品牌 SVG 可以直接拖入 Draw.io。

PNG 是预览，不适合当作高清矢量素材。完整目录未压缩约 203 MiB。

## 给 Agent 使用

让 Agent 先读 [AGENTS.md](AGENTS.md) 和 [agent-manifest.json](agent-manifest.json)，再按需要查询，不必遍历全部图片。

在仓库根目录，使用 Python 3：

```sh
python ontology/query_ontology.py "aws lambda" --kind shape --limit 5
python ontology/query_ontology.py "OpenAI 图标" --kind icon
python ontology/query_ontology.py "LPIPS 神经网络" --kind diagram
python ontology/query_ontology.py "Terraform" --kind capability
python ontology/validate_ontology.py
```

完整查询结果包含可用路径；`--compact` 适合只需简要候选时。查询仅使用 Python 标准库，无需网络或模型 API。执行绘图脚本仍需按各脚本文档配置依赖。

## 范围与限制

这是 2026 年 8 月制作的快照，基于 Draw.io Desktop 30.0.4、drawio-skill 2.1.0，不保证覆盖新版 Draw.io 的全部素材。

当前 ontology 是轻量分类与检索层；JSON-LD 汇总能力、图类型、库和图标，Shape 详细记录在 JSONL 中。搜索基于关键词，分类含启发式规则。

预览经过批量生成和抽查，未逐一人工核验。复杂图形可能出现裁切或显示不完整，Text 等无边框元素可能为空白；遇到问题请查看 `.drawio` 源文件。历史批量生成脚本未包含在此快照中。欢迎通过 Issue 提交图形编号、截图和改进建议。

## 素材来源与许可证

本项目原创文档与查询/验证代码采用 MIT。第三方图形、品牌、索引和 skill 保留各自许可，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

特别是 Draw.io 内置素材包含针对 Atlassian 生态使用的限制，我们保留了完整原文；品牌标识的商标权属于各自所有者。不要把整个图鉴误认为无条件可再授权的原创图标包。
