#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/"site"/"index.html").read_text(encoding="utf-8")
C=json.loads((ROOT/"site"/"catalog"/"catalog.json").read_text(encoding="utf-8"))
checks={
"lang_ja":'<html lang="ja">' in HTML,
"viewport":'name="viewport"' in HTML,
"skip_link":'class="skip"' in HTML,
"aria_live":'aria-live="polite"' in HTML,
"no_analytics":"gtag(" not in HTML.lower(),
"no_external_script":not re.search(r'<script[^>]+src=["\']https?://',HTML,re.I),
"catalog_fetch":'fetch("./catalog/catalog.json"' in HTML,
"catalog_has_apps":len(C.get("apps",[]))>=1,
"featured_present":any(a.get("featured") for a in C["apps"]),
"deprecated_present":any(a.get("status")=="deprecated" for a in C["apps"])
}
for k,v in checks.items():print(("PASS" if v else "FAIL"),k)
failed=[k for k,v in checks.items() if not v]
if failed:raise SystemExit(1)
print("ALL TESTS PASS")
