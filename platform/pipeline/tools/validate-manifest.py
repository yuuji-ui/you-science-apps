#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

def main():
    if len(sys.argv)!=3:
        print("Usage: validate-manifest.py SCHEMA MANIFEST")
        return 2
    schema=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    data=json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(data))
    if errors:
        print("FAIL")
        for e in errors:
            loc="$"+("."+ ".".join(map(str,e.path)) if e.path else "")
            print(f"- {loc}: {e.message}")
        return 1
    print("PASS")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
