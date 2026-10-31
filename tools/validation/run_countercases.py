#!/usr/bin/env python3
"""Run the unchanged historical static countercases with a new aggregate destination."""
import argparse
from pathlib import Path
import test_chain

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();dest=a.output.resolve()
 if dest.exists():p.error('Use a new output file')
 original=test_chain.dump;old=(test_chain.TOOLS/'evidence/countercases.json').resolve()
 def dump(path,value):
  original(dest if Path(path).resolve()==old else path,value)
 test_chain.dump=dump
 return test_chain.main()
if __name__=='__main__':raise SystemExit(main())
