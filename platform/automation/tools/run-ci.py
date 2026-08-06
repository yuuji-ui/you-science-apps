#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

class CIError(RuntimeError):
    pass

def run(command, cwd):
    proc=subprocess.run(command,cwd=cwd,text=True,capture_output=True)
    result={
      "command":command,
      "returnCode":proc.returncode,
      "stdout":proc.stdout.strip(),
      "stderr":proc.stderr.strip(),
      "result":"PASS" if proc.returncode==0 else "FAIL"
    }
    if proc.returncode!=0:
      raise CIError(
        "Command failed: "+" ".join(command)+"\n"+proc.stdout+"\n"+proc.stderr
      )
    return result

def require_paths(repo,paths):
    missing=[p for p in paths if not (repo/p).exists()]
    if missing:
      raise CIError("Required paths are missing: "+", ".join(missing))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",default=".")
    parser.add_argument("--report",default="platform/automation/docs/ci-report.json")
    parser.add_argument("--skip-component-tests",action="store_true")
    args=parser.parse_args()
    repo=Path(args.repo).resolve()
    report_path=repo/args.report
    report={"result":"PASS","mode":None,"steps":[],"errors":[]}

    try:
      require_paths(repo,[
        "requirements.txt",
        "site/index.html",
        "site/catalog/catalog.json",
        "platform/manifest/schemas/app-manifest.schema.json",
        "platform/manifest/tools/validate-manifest.py",
        "platform/catalog/schemas/catalog.schema.json",
        "platform/catalog/tools/generate-catalog.py",
        "platform/catalog/tools/validate-catalog.py",
        "platform/pipeline/tools/run-platform-pipeline.py",
        "platform/tools/app-registration-wizard/wizard-core.js",
      ])

      if not args.skip_component_tests:
        for test_path in [
          "platform/manifest/tests/test-manifest-schema.py",
          "platform/catalog/tests/test-catalog-generator.py",
          "platform/portal/tests/test-portal.py",
          "platform/pipeline/tests/test-platform-pipeline.py",
          "platform/tools/app-registration-wizard/tests/test-wizard.py",
          "platform/tools/app-update-wizard/tests/test-update-wizard.py",
          "platform/tools/classification-editor/tests/test-classification-editor.py",
          "platform/automation/tests/test-workflows.py",
        ]:
          require_paths(repo,[test_path])
          report["steps"].append(run([sys.executable,test_path],repo))

      manifests=sorted((repo/"site/apps").rglob("app.manifest.json")) \
        if (repo/"site/apps").exists() else []

      if manifests:
        report["mode"]="production"
        require_paths(repo,[
          "catalog-source/catalog.override.json",
          "catalog-source/catalog-groups.json",
        ])
        for manifest in manifests:
          report["steps"].append(run([
            sys.executable,
            "platform/manifest/tools/validate-manifest.py",
            "platform/manifest/schemas/app-manifest.schema.json",
            str(manifest.relative_to(repo))
          ],repo))

        report["steps"].append(run([
          sys.executable,
          "platform/catalog/tools/generate-catalog.py",
          "--apps-dir","site/apps",
          "--override","catalog-source/catalog.override.json",
          "--groups","catalog-source/catalog-groups.json",
          "--output","site/catalog/catalog.json",
          "--report","platform/automation/docs/catalog-generation-report.json",
        ],repo))
      else:
        report["mode"]="bootstrap"
        report["steps"].append({
          "result":"PASS",
          "message":"No app manifests under site/apps; validate committed catalog."
        })

      report["steps"].append(run([
        sys.executable,
        "platform/catalog/tools/validate-catalog.py",
        "platform/catalog/schemas/catalog.schema.json",
        "site/catalog/catalog.json",
      ],repo))

      index=(repo/"site/index.html").read_text(encoding="utf-8").lower()
      forbidden=[
        "google-analytics.com","googletagmanager.com","gtag(",
        "doubleclick.net","adsbygoogle"
      ]
      found=[x for x in forbidden if x in index]
      if found:
        raise CIError(
          "Forbidden analytics/advertising markers found: "+", ".join(found)
        )
      report["steps"].append({
        "result":"PASS","message":"Static privacy checks passed."
      })
    except Exception as exc:
      report["result"]="FAIL"
      report["errors"].append(str(exc))

    report_path.parent.mkdir(parents=True,exist_ok=True)
    report_path.write_text(
      json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8"
    )
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report["result"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
