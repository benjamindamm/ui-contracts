from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
import json,mimetypes
w=Path(__file__).parent.resolve();host=w/'host';root=w.parent
vendors={'vendor/scxml.js':root/'scxml-runtime/tool/node_modules/@scion-scxml/scxml/dist/scxml.min.js','vendor/polyfill.js':root/'scxml-runtime/tool/node_modules/@babel/polyfill/dist/polyfill.min.js'}
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  name=self.path.split('?')[0].lstrip('/')or'index.html';p=vendors.get(name,host/name).resolve()
  if p not in vendors.values() and not p.is_relative_to(host):self.send_error(403);return
  if not p.is_file():self.send_error(404);return
  data=p.read_bytes();self.send_response(200);self.send_header('Content-Type',mimetypes.guess_type(str(p))[0]or'application/octet-stream');self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
 def do_POST(self):
  if self.path!='/capture':self.send_error(404);return
  try:
   d=json.loads(self.rfile.read(int(self.headers['Content-Length'])));name=d['name'];assert name.replace('-','').isalnum() and len(name)<80
   (w/'captures'/(name+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
  except Exception as e:self.send_error(400,str(e));return
  self.send_response(200);self.end_headers();self.wfile.write(b'{}')
s=ThreadingHTTPServer(('127.0.0.1',0),Handler);(w/'server.json').write_text(json.dumps({'port':s.server_port,'url':'http://127.0.0.1:'+str(s.server_port)+'/'}));print(s.server_port,flush=True);s.serve_forever()
