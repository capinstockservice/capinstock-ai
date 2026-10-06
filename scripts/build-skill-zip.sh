#!/usr/bin/env bash
# Собирает capinstock-skill.zip для загрузки навыка в Claude.ai:
# в корне архива должна лежать папка навыка (capinstock/SKILL.md), а не сам SKILL.md.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-$here/dist/capinstock-skill.zip}"
mkdir -p "$(dirname "$out")"
python3 - "$here/plugins/capinstock/skills" "$out" <<'PY'
import os, sys, zipfile
base, out = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(os.path.join(base, 'capinstock')):
        for f in sorted(files):
            if f.startswith('.'):
                continue
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, base))
print(out)
PY
