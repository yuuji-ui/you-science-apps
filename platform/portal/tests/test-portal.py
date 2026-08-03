#!/usr/bin/env python3
"""You Science Apps Portalの静的検証。"""

from pathlib import Path
import json
import re

# このファイル：
# platform/portal/tests/test-portal.py
#
# リポジトリのルート：
# parents[3]
REPOSITORY_ROOT = Path(__file__).resolve().parents[3]

HTML_PATH = REPOSITORY_ROOT / "site" / "index.html"
CATALOG_PATH = REPOSITORY_ROOT / "site" / "catalog" / "catalog.json"


def main() -> int:
    html = HTML_PATH.read_text(encoding="utf-8")
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    checks = {
        "lang_ja": '<html lang="ja">' in html,
        "viewport": 'name="viewport"' in html,
        "skip_link": 'class="skip"' in html,
        "aria_live": 'aria-live="polite"' in html,
        "no_analytics": "gtag(" not in html.lower(),
        "no_external_script": not re.search(
            r'<script[^>]+src=["\']https?://',
            html,
            re.IGNORECASE,
        ),
        "catalog_fetch": 'fetch("./catalog/catalog.json"' in html,
        "catalog_has_apps": len(catalog.get("apps", [])) >= 1,
        "featured_present": any(
            app.get("featured") for app in catalog.get("apps", [])
        ),
        "deprecated_present": any(
            app.get("status") == "deprecated"
            for app in catalog.get("apps", [])
        ),
    }

    failed = []

    for name, passed in checks.items():
        print(("PASS" if passed else "FAIL"), name)

        if not passed:
            failed.append(name)

    if failed:
        print("FAILED:", ", ".join(failed))
        return 1

    print("ALL TESTS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
