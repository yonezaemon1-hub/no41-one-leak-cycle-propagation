#!/usr/bin/env python3
"""Read-only SHA-256 and manifest coverage check; Python standard library."""
from hashlib import sha256
from pathlib import Path, PurePosixPath
import sys


def main():
    root = Path(__file__).resolve().parent
    manifest = root / "SHA256SUMS"
    expected = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        p = PurePosixPath(name)
        if p.is_absolute() or ".." in p.parts or name in expected:
            raise ValueError("Unsafe or duplicate manifest entry")
        expected[name] = digest
    failed = []
    for name, digest in expected.items():
        p = root / name
        if not p.is_file() or sha256(p.read_bytes()).hexdigest() != digest:
            failed.append(name)
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*")
              if p.is_file() and p != manifest and "__pycache__" not in p.parts}
    missing = sorted(actual - expected.keys())
    if failed or missing:
        print({"status": "FAIL", "mismatches": failed, "unlisted": missing})
        return 1
    print({"status": "PASS", "files": len(expected), "manifest_coverage": "complete"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
