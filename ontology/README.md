# Draw.io Ontology

这是给 Agent 使用的分层知识入口，不替代原始图片或 skill。

## 规模

- 官方 Shape：10,446
- Shape Library：135
- AI/数据 SVG：328
- Capability Script：38
- Diagram Type：11

## 文件职责

- `drawio-ontology.jsonld`：核心实体关系图。
- `capabilities.jsonl`：脚本能力、输入、输出、依赖与意图。
- `diagram_types.jsonl`：图类型、布局、元素和推荐工具。
- `shape_libraries.jsonl`：官方图形库语义分类、数量、示例和浏览路径。
- `shapes_search.jsonl`：10,446 个 shape 的精确可查询索引；不要整体塞进上下文。
- `icons_search.jsonl`：本地 SVG 图标索引。
- `intent_routes.jsonl`：自然语言意图到工作流的路由。
- `query_ontology.py`：零依赖的本地查询工具。

## 最短使用方式

```powershell
powershell -ExecutionPolicy Bypass -File ontology/query_ontology.ps1 "查询词" --kind auto --compact
```
