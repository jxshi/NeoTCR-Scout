"""Tiny dependency-free build backend for editable installs in restricted envs.

The project runtime code uses optional integrations for Typer/Pydantic/Pandas/Jinja2,
but CI sandboxes may not be able to download build dependencies. This backend
creates a minimal wheel containing a .pth file that points Python at the source
tree plus standard dist-info metadata and console entry points.
"""

from __future__ import annotations

import base64
import csv
import hashlib
import io
import zipfile
from pathlib import Path

NAME = "neotcr_scout"
DIST = "neotcr_scout-0.1.0"
WHEEL_NAME = f"{DIST}-py3-none-any.whl"


def get_requires_for_build_wheel(config_settings=None):
    return []


def get_requires_for_build_editable(config_settings=None):
    return []


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    dist_info = Path(metadata_directory) / f"{DIST}.dist-info"
    dist_info.mkdir(parents=True, exist_ok=True)
    _write_metadata(dist_info)
    return dist_info.name


def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    return prepare_metadata_for_build_wheel(metadata_directory, config_settings)


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    return _build(wheel_directory)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    return _build(wheel_directory)


def _build(wheel_directory) -> str:
    wheel_dir = Path(wheel_directory)
    wheel_dir.mkdir(parents=True, exist_ok=True)
    wheel_path = wheel_dir / WHEEL_NAME
    records: list[tuple[str, str, str]] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        _writestr(zf, records, f"{NAME}.pth", str(Path.cwd()))
        _writestr(zf, records, f"{DIST}.dist-info/METADATA", _metadata_text())
        _writestr(zf, records, f"{DIST}.dist-info/WHEEL", "Wheel-Version: 1.0\nGenerator: NeoTCR-Scout minimal backend\nRoot-Is-Purelib: true\nTag: py3-none-any\n")
        _writestr(zf, records, f"{DIST}.dist-info/entry_points.txt", "[console_scripts]\nneotcr-scout = neotcr_scout.cli:main\n")
        record_name = f"{DIST}.dist-info/RECORD"
        record_stream = io.StringIO()
        writer = csv.writer(record_stream)
        writer.writerows(records)
        writer.writerow((record_name, "", ""))
        zf.writestr(record_name, record_stream.getvalue())
    return wheel_path.name


def _write_metadata(dist_info: Path) -> None:
    (dist_info / "METADATA").write_text(_metadata_text(), encoding="utf-8")
    (dist_info / "WHEEL").write_text("Wheel-Version: 1.0\nGenerator: NeoTCR-Scout minimal backend\nRoot-Is-Purelib: true\nTag: py3-none-any\n", encoding="utf-8")
    (dist_info / "entry_points.txt").write_text("[console_scripts]\nneotcr-scout = neotcr_scout.cli:main\n", encoding="utf-8")


def _metadata_text() -> str:
    return "\n".join(
        [
            "Metadata-Version: 2.1",
            "Name: neotcr-scout",
            "Version: 0.1.0",
            "Summary: Evidence-guided neoantigen-specific TCR discovery and prioritization workflow.",
            "Requires-Python: >=3.10",
            "License: MIT",
            "",
        ]
    )


def _writestr(zf: zipfile.ZipFile, records: list[tuple[str, str, str]], name: str, content: str) -> None:
    data = content.encode("utf-8")
    zf.writestr(name, data)
    digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")
    records.append((name, f"sha256={digest}", str(len(data))))
