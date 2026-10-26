# Draw.io 零部件视觉图鉴

双击 `打开这里_index.html` 开始浏览。

## 目录说明

- `01_官方Shapes_PNG/png/`：44 张完整联系表，覆盖 10,446 个官方 Draw.io shape。
- `01_官方Shapes_PNG/individual_png/`：10,446 个单独 PNG，按 135 个图形库/命名空间分类。
- `01_官方Shapes_PNG/drawio_source/`：联系表对应的可编辑 `.drawio` 源文件。
- `02_完整Shape索引/`：完整 CSV/JSON 索引，包含编号、名称、尺寸、类型、标签和精确 style。
- `03_AI与数据图标_SVG/`：drawio-skill 支持的 AI、LLM 和数据系统本地 SVG 图标。
- `04_skill完整副本/`：drawio-skill 2.1.0 的完整副本、脚本与参考说明。
- `05_Drawio内置图片资源/`：从本机 Draw.io 30.0.4 安装包提取的 2,038 个原始图片资源。
- `功能总览.md`：skill 所有随附脚本与主要能力的自动汇总。

## 如何把看到的图形用到图中

1. 在 PNG 图鉴中记下左上角的编号。
2. 在 `02_完整Shape索引/shape-index.csv` 搜索编号或名称。
3. 复制该行的 `style` 到 `.drawio` XML，或者直接打开对应的 `.drawio` 联系表复制该 shape。
4. AI/LLM 图标可以把 SVG 直接拖入 Draw.io；本目录中的文件均已本地化，离线可见。

注意：少数 Text、Autosize Text、容器辅助项本身没有可见轮廓，空白缩略图是其真实默认状态，并非导出失败。
