#!/usr/bin/env python3
"""Loopback-only test collector; accepts one immutable capture per declared case."""
import argparse,hashlib,json
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial

def handler(root):
 manifest=json.loads((root/'manifest.json').read_text());cases=json.loads((root/'cases.json').read_text())['cases'];dest=root/'captures';dest.mkdir(exist_ok=True)
 class Handler(SimpleHTTPRequestHandler):
  def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(root),**kwargs)
  def end_headers(self):self.send_header('Cache-Control','no-store');super().end_headers()
  def do_POST(self):
   try:
    if self.path!='/capture':raise ValueError('Capture endpoint only')
    if self.headers.get('Origin')!='http://'+self.headers.get('Host',''):raise ValueError('Same-origin captures only')
    size=int(self.headers.get('Content-Length','0'))
    if not 0<size<4_000_000:raise ValueError('Invalid size')
    body=json.loads(self.rfile.read(size));name=body['name']
    if name not in cases or body['challenge']!=manifest['challenge'] or body['sourceRevision']!=manifest['revision']:raise ValueError('Binding mismatch')
    path=dest/(name+'.json')
    with path.open('x') as out:json.dump(body,out,indent=2,ensure_ascii=False)
    self.send_response(201);self.end_headers();self.wfile.write(b'{"saved":true}')
   except Exception as e:self.send_response(409);self.end_headers();self.wfile.write(str(e).encode())
 return Handler
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',type=Path,required=True);p.add_argument('--port',type=int,default=8770);a=p.parse_args();ThreadingHTTPServer(('127.0.0.1',a.port),handler(a.run.resolve())).serve_forever()
