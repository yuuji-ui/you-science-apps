#!/usr/bin/env python3
"""You Science Apps integration pipeline.

1. Validate all app manifests
2. Generate catalog.json
3. Validate generated catalog
4. Copy generated catalog into site/catalog/
5. Emit machine-readable report
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apps-dir", required=True)
    parser.add_argument("--manifest-schema", required=True)
    parser.add_argument("--catalog-generator", required=True)
    parser.add_argument("--catalog-validator", required=True)
    parser.add_argument("--catalog-schema", required=True)
    parser.add_argument("--override", required=True)
    parser.add_argument("--groups", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    apps_dir = Path(args.apps_dir)
    manifest_schema = Path(args.manifest_schema)
    output = Path(args.output)
    report_path = Path(args.report)

    report = {
        "result": "PASS",
        "manifestValidation": [],
        "catalogGeneration": None,
        "catalogValidation": None,
        "errors": []
    }

    manifests = sorted(apps_dir.rglob("app.manifest.json"))
    if not manifests:
        report["result"] = "FAIL"
        report["errors"].append(f"No app.manifest.json found under {apps_dir}")
    else:
        for manifest in manifests:
            proc = run([
                sys.executable,
                str(Path(__file__).with_name("validate-manifest.py")),
                str(manifest_schema),
                str(manifest)
            ])
            item = {
                "manifest": str(manifest),
                "result": "PASS" if proc.returncode == 0 else "FAIL",
                "stdout": proc.stdout.strip(),
                "stderr": proc.stderr.strip()
            }
            report["manifestValidation"].append(item)
            if proc.returncode != 0:
                report["result"] = "FAIL"
                report["errors"].append(f"Manifest validation failed: {manifest}")

    if report["result"] == "PASS":
        gen = run([
            sys.executable,
            args.catalog_generator,
            "--apps-dir", str(apps_dir),
            "--override", args.override,
            "--groups", args.groups,
            "--output", str(output)
        ])
        report["catalogGeneration"] = {
            "result": "PASS" if gen.returncode == 0 else "FAIL",
            "stdout": gen.stdout.strip(),
            "stderr": gen.stderr.strip()
        }
        if gen.returncode != 0:
            report["result"] = "FAIL"
            report["errors"].append("Catalog generation failed")

    if report["result"] == "PASS":
        val = run([
            sys.executable,
            args.catalog_validator,
            args.catalog_schema,
            str(output)
        ])
        report["catalogValidation"] = {
            "result": "PASS" if val.returncode == 0 else "FAIL",
            "stdout": val.stdout.strip(),
            "stderr": val.stderr.strip()
        }
        if val.returncode != 0:
            report["result"] = "FAIL"
            report["errors"].append("Catalog validation failed")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
