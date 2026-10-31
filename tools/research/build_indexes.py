#!/usr/bin/env python3
"""Retired legacy writer: its fixed 2026-10-25 index would erase newer navigation."""
if __name__=='__main__':
 import sys
 print('Historical index writer retired without writing files. Use tools/research/navigation.py --output NEWFILE for the current navigation audit. Original source is preserved under docs/research/analyses/AGENT-WORKFLOW-2026-10-31/before/build_indexes.py.',file=sys.stderr)
 raise SystemExit(2)
