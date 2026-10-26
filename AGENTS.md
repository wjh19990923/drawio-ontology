# Draw.io Catalog: Agent Instructions

This folder is a layered knowledge base for Draw.io Desktop 30.0.4 and drawio-skill 2.1.0.
It contains 10,446 official shapes, 328 local SVG icons, 38 executable capability scripts, and 11 diagram-type presets.

## Mandatory read and routing order

1. Read `agent-manifest.json` for scope, counts, rules, and the canonical workflow.
2. Read `ontology/intent_routes.jsonl` and select the closest user intent.
3. Read only the matching row in `ontology/diagram_types.jsonl` and `ontology/capabilities.jsonl`.
4. Resolve visual assets with `ontology/query_ontology.py`; do not recursively scan PNG/SVG folders.
5. Read the authoritative skill instructions at `04_skill完整副本/SKILL.md` before executing a Draw.io task.

## Canonical queries

```powershell
powershell -ExecutionPolicy Bypass -File ontology/query_ontology.ps1 "aws lambda" --kind shape --limit 5 --compact
powershell -ExecutionPolicy Bypass -File ontology/query_ontology.ps1 "OpenAI 图标" --kind icon --compact
powershell -ExecutionPolicy Bypass -File ontology/query_ontology.ps1 "神经网络 LPIPS" --kind diagram --compact
powershell -ExecutionPolicy Bypass -File ontology/query_ontology.ps1 "Terraform architecture" --kind capability --compact
```

## Entity classes

- `DiagramType`: structural conventions and preferred tools.
- `Capability`: an executable skill script with inputs, outputs, dependencies, and intents.
- `ShapeLibrary`: a semantic collection of official Draw.io shapes.
- `Shape`: an official stencil/style with exact dimensions, preview, contact sheet, and editable source.
- `Icon`: a local external SVG, primarily AI/LLM/data brands; not an official Draw.io stencil.
- `IntentRoute`: maps natural-language tasks to diagram types and capabilities.

## Non-negotiable rules

- Never guess `shape=mxgraph.*`; use the exact `style` returned by the ontology or `shapesearch.py`.
- Do not load `shapes_search.jsonl` wholesale into the model context. Query it with the provided script.
- Use `.drawio` sources for copying editable shapes; PNGs are previews, not canonical definitions.
- For AI/LLM icons, prefer local SVG or `aiicons.py --embed` so offline export does not produce blanks.
- Large/layout-heavy graphs use extractor → graph JSON → `autolayout.py` → `.drawio` → `validate.py` → export.
- Hand-written XML must follow `04_skill完整副本/references/xml-authoring.md`.
- Final diagrams require validation plus a PNG visual check.
