#!/usr/bin/env python3
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[3]
V = (ROOT/".github/workflows/validate-platform.yml").read_text(encoding="utf-8")
D = (ROOT/".github/workflows/deploy-pages.yml").read_text(encoding="utf-8")
C = (ROOT/"platform/automation/tools/run-ci.py").read_text(encoding="utf-8")
checks = {
    "checkout_v6": "actions/checkout@v6" in V and "actions/checkout@v6" in D,
    "setup_python_v6": "actions/setup-python@v6" in D,
    "configure_pages_v5": "actions/configure-pages@v5" in D,
    "upload_pages_v4": "actions/upload-pages-artifact@v4" in D,
    "deploy_pages_v4": "actions/deploy-pages@v4" in D,
    "pages_write": "pages: write" in D,
    "id_token_write": "id-token: write" in D,
    "github_pages_environment": "name: github-pages" in D,
    "site_artifact": "path: site" in D,
    "bootstrap_mode": '"bootstrap"' in C,
    "production_mode": '"production"' in C,
    "privacy_check": "Static privacy checks passed." in C,
}
for k,v in checks.items():
    print(("PASS" if v else "FAIL"), k)
if not all(checks.values()):
    raise SystemExit(1)
print("ALL TESTS PASS")
