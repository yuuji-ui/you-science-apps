#!/usr/bin/env python3
"""Generate You Science Apps catalog.json from app manifests."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PUBLISHABLE_STATUSES = {"active", "maintenance", "deprecated"}


class CatalogError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise CatalogError(f"File not found: {path}")
    except json.JSONDecodeError as exc:
        raise CatalogError(f"Invalid JSON: {path}: {exc}") from exc


def find_manifests(apps_dir: Path) -> list[Path]:
    return sorted(apps_dir.rglob("app.manifest.json"))


def to_catalog_app(manifest: dict[str, Any]) -> dict[str, Any]:
    education = manifest["education"]
    hosted = manifest["distribution"]["hosted"]
    links = manifest.get("links", {})
    return {
        "appId": manifest["appId"],
        "title": manifest["title"],
        "version": manifest["version"],
        "status": manifest["status"],
        "level": manifest.get("level"),
        "schoolStage": education["schoolStage"],
        "subjects": education["subjects"],
        "grades": education["grades"],
        "units": education["units"],
        "appTypes": education["appTypes"],
        "learningGoals": education["learningGoals"],
        "useCases": education["useCases"],
        "hostedUrl": links.get("hostedUrl") if hosted.get("enabled") else None,
        "featured": False,
        "hidden": False,
        "sortOrder": 1000,
        "labels": [],
        "deprecatedMessage": None,
    }


def apply_override(app: dict[str, Any], override: dict[str, Any]) -> None:
    allowed = {"featured","hidden","sortOrder","labels","deprecatedMessage"}
    for key, value in override.items():
        if key not in allowed:
            raise CatalogError(
                f"Override for {app['appId']} contains forbidden field: {key}"
            )
        app[key] = value


def validate_unique_ids(apps: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    duplicates: list[str] = []
    for app in apps:
        app_id = app["appId"]
        if app_id in seen:
            duplicates.append(app_id)
        seen.add(app_id)
    if duplicates:
        raise CatalogError(
            "Duplicate appId values: " + ", ".join(sorted(set(duplicates)))
        )


def validate_groups(groups: list[dict[str, Any]], app_ids: set[str]) -> None:
    group_ids: set[str] = set()
    for group in groups:
        gid = group["groupId"]
        if gid in group_ids:
            raise CatalogError(f"Duplicate groupId: {gid}")
        group_ids.add(gid)
        missing = sorted(set(group["appIds"]) - app_ids)
        if missing:
            raise CatalogError(
                f"Group {gid} references unknown appId(s): {', '.join(missing)}"
            )


def generate_catalog(
    apps_dir: Path,
    override_path: Path,
    groups_path: Path,
    include_hidden: bool = False,
) -> dict[str, Any]:
    manifest_paths = find_manifests(apps_dir)
    if not manifest_paths:
        raise CatalogError(f"No app.manifest.json found under {apps_dir}")

    apps: list[dict[str, Any]] = []
    source_paths: dict[str, str] = {}

    for path in manifest_paths:
        manifest = load_json(path)
        required = ["appId","title","version","status","education","distribution","privacy","license"]
        missing = [key for key in required if key not in manifest]
        if missing:
            raise CatalogError(f"{path}: missing required keys: {', '.join(missing)}")

        app_id = manifest["appId"]
        if app_id in source_paths:
            raise CatalogError(
                f"Duplicate appId {app_id}: {source_paths[app_id]} and {path}"
            )
        source_paths[app_id] = str(path)

        if manifest["status"] not in PUBLISHABLE_STATUSES:
            continue

        apps.append(to_catalog_app(manifest))

    validate_unique_ids(apps)

    override_data = load_json(override_path)
    app_overrides = override_data.get("apps", {})
    known_ids = {app["appId"] for app in apps}

    unknown_overrides = sorted(set(app_overrides) - known_ids)
    if unknown_overrides:
        raise CatalogError(
            "Override references unknown or unpublished appId(s): "
            + ", ".join(unknown_overrides)
        )

    for app in apps:
        if app["appId"] in app_overrides:
            apply_override(app, app_overrides[app["appId"]])

    if not include_hidden:
        apps = [app for app in apps if not app["hidden"]]

    apps.sort(
        key=lambda app: (
            app["sortOrder"],
            0 if app["featured"] else 1,
            app["title"],
            app["appId"],
        )
    )

    groups_data = load_json(groups_path)
    groups = groups_data.get("groups", [])
    visible_ids = {app["appId"] for app in apps}
    validate_groups(groups, visible_ids)
    groups = sorted(groups, key=lambda g: (g["sortOrder"], g["title"], g["groupId"]))

    return {
        "schemaVersion": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "apps": apps,
        "groups": groups,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apps-dir", required=True)
    parser.add_argument("--override", required=True)
    parser.add_argument("--groups", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--report")
    parser.add_argument("--include-hidden", action="store_true")
    args = parser.parse_args()

    output_path = Path(args.output)
    report_path = Path(args.report) if args.report else None

    try:
        catalog = generate_catalog(
            Path(args.apps_dir),
            Path(args.override),
            Path(args.groups),
            args.include_hidden,
        )
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        report = {
            "result": "PASS",
            "apps": len(catalog["apps"]),
            "groups": len(catalog["groups"]),
            "output": str(output_path),
        }
        print(json.dumps(report, ensure_ascii=False))
        if report_path:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(
                json.dumps(report, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        return 0
    except CatalogError as exc:
        report = {"result": "FAIL", "error": str(exc)}
        print(json.dumps(report, ensure_ascii=False))
        if report_path:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(
                json.dumps(report, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
