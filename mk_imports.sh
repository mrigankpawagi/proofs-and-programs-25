#!/bin/bash
set -e
find PfsProgs25 -name "*.lean" | env LC_ALL=C sort | sed 's/\.lean//;s,/,.,g;s/^/import /' > PnP2023.lean
cat Import_tail.lean >> PnP2023.lean
