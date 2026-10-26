#!/usr/bin/env python3
"""Validate ontology syntax, cardinalities, and referenced local assets."""
import json, sys
from pathlib import Path
root=Path(__file__).resolve().parent.parent; onto=root/"ontology"
expected=json.loads((root/"agent-manifest.json").read_text(encoding="utf-8"))["counts"]
files={"official_shapes":"shapes_search.jsonl","shape_libraries":"shape_libraries.jsonl","external_svg_icons":"icons_search.jsonl","capability_scripts":"capabilities.jsonl","diagram_types":"diagram_types.jsonl"}
records={}; errors=[]
for key,name in files.items():
    rows=[]
    for n,line in enumerate((onto/name).read_text(encoding="utf-8").splitlines(),1):
        if line.strip():
            try: rows.append(json.loads(line))
            except Exception as exc: errors.append(f"{name}:{n}: {exc}")
    records[key]=rows
    if len(rows)!=expected[key]: errors.append(f"{name}: expected {expected[key]}, got {len(rows)}")
json.loads((onto/"drawio-ontology.jsonld").read_text(encoding="utf-8"))
json.loads((onto/"ontology-schema.json").read_text(encoding="utf-8"))
for row in records["official_shapes"]:
    for field in ("preview_png","contact_sheet","editable_source"):
        if not (root/row[field]).is_file(): errors.append(f"missing {field}: {row[field]}")
for row in records["external_svg_icons"]:
    if not (root/row["local_svg"]).is_file(): errors.append(f"missing SVG: {row['local_svg']}")
for row in records["capability_scripts"]:
    if not (root/row["script"]).is_file(): errors.append(f"missing script: {row['script']}")
result={"ok":not errors,"counts":{k:len(v) for k,v in records.items()},"errors":errors[:50],"error_count":len(errors)}
print(json.dumps(result,ensure_ascii=False,indent=2)); sys.exit(0 if not errors else 1)
