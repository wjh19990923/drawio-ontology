#!/usr/bin/env python3
"""Token-efficient search over the local Draw.io ontology. Stdlib only."""
import argparse, json, re, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
FILES = {
  "shape": "shapes_search.jsonl", "icon": "icons_search.jsonl",
  "library": "shape_libraries.jsonl", "capability": "capabilities.jsonl",
  "diagram": "diagram_types.jsonl", "intent": "intent_routes.jsonl",
}

def norm(s): return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", str(s).lower()).strip()
STOP={"icon","icons","shape","shapes","diagram","drawio","architecture","visualization","figure","图标","图形","元素","图","架构","架构图","流程图"}
def score(record, query):
    core_keys={"id","name","title","library","domain","category","intent_terms","aliases","tags","match_terms","example_shapes","top_terms","elements"}
    core = norm(" ".join(str(v) for k,v in record.items() if k in core_keys))
    description = norm(record.get("description", ""))
    raw_terms=norm(query).split(); terms=[t for t in raw_terms if t not in STOP] or raw_terms
    q=" ".join(terms)
    if not q: return 0
    value = 100 if q in core else 20 if q in description else 0
    value += sum(20 for t in terms if t in core)
    value += sum(5 for t in terms if t in description and t not in core)
    title = norm(record.get("title") or record.get("name") or record.get("id") or "")
    value += 80 if q == title else 30 if title.startswith(q) else 0
    return value

def load(kind):
    with (ROOT / FILES[kind]).open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]

def main():
    ap=argparse.ArgumentParser(description="Search Draw.io capabilities, diagram types, shapes, libraries, and icons")
    ap.add_argument("query"); ap.add_argument("--kind",choices=["auto",*FILES],default="auto")
    ap.add_argument("--limit",type=int,default=8); ap.add_argument("--compact",action="store_true")
    args=ap.parse_args(); kinds=list(FILES) if args.kind=="auto" else [args.kind]
    found=[]
    for kind in kinds:
        for record in load(kind):
            s=score(record,args.query)
            if s: found.append((s,kind,record))
    found.sort(key=lambda x:(-x[0],x[1],str(x[2].get("title") or x[2].get("name") or x[2].get("id"))))
    output=[]
    for s,kind,record in found[:args.limit]:
        if args.compact:
            keep={k:record.get(k) for k in ("id","name","title","library","category","script","path","preview_png","local_svg","style") if record.get(k) is not None}
            record=keep
        output.append({"score":s,"kind":kind,**record})
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
