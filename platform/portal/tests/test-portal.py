#!/usr/bin/env python3
from pathlib import Path
import re

REPO=Path(__file__).resolve().parents[3]
HTML=(REPO/"site/index.html").read_text(encoding="utf-8")
checks={
 "no_level_display": "Level ${" not in HTML and ">Level " not in HTML,
 "difficulty_mapping": 'if(score<=2)return "basic"' in HTML and 'if(score<=4)return "standard"' in HTML,
 "favorites": 'ysa.portal.favorites.v1' in HTML,
 "recent": 'ysa.portal.recent.v1' in HTML and ".slice(0,3)" in HTML,
 "three_columns": "repeat(3,minmax(0,1fr))" in HTML,
 "two_columns": "repeat(2,minmax(0,1fr))" in HTML,
 "filters": all(x in HTML for x in ['id="group"','id="audience"','id="category"','id="difficulty"']),
 "privacy_notice": "この端末のブラウザ内だけに保存" in HTML,
 "shared_device_warning": "次に使う人にも見える可能性" in HTML,
}
for name,ok in checks.items(): print(("PASS" if ok else "FAIL"),name)
if not all(checks.values()): raise SystemExit(1)
print("ALL TESTS PASS")
