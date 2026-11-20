#!/usr/bin/env python3
"""Read-only checks for the pinned floral Linux 4.14 input."""
import argparse
import json
import re
from pathlib import Path


def audit(root):
    required = ["Makefile", "build.config.floral", "arch/arm64", "drivers"]
    results = {path: (root / path).exists() for path in required}
    version = None
    makefile = root / "Makefile"
    if makefile.is_file():
        text = makefile.read_text(errors="replace")
        m = re.search(r"^VERSION\\s*=\\s*(\\d+)\\s*$", text, re.M)
        n = re.search(r"^PATCHLEVEL\\s*=\\s*(\\d+)\\s*$", text, re.M)
        if m and n:
            version = f"{m.group(1)}.{n.group(1)}"
    info = {"kernel_path": str(root.resolve()), "required": results,
            "kernel_series": version, "kernelsu_gitmodules_present":
            (root / ".gitmodules").is_file(),
            "pass": all(results.values()) and version == "4.14"}
    return info


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("kernel", type=Path)
    args = parser.parse_args()
    result = audit(args.kernel)
    print(json.dumps(result, indent=2))
    return 0 if result["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
