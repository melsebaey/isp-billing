# server.py — isp-billing
import json, os, shutil, datetime, socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8080
DB_FILE = 'isp_data.json'
BACKUP_DIR = 'backups'
HTML_FILE = 'index.html'
_rev = 0

def load_db():
    global _rev
    try:
        with open(DB_FILE, encoding='utf-8') as f:
            d = json.load(f); _rev = d.get('_rev', 0); return d
    except Exception:
        return None

def save_db(d):
    global _rev
    _rev = int(d.get('_rev', 0)) + 1; d['_rev'] = _rev
    with open(DB_FILE + '.tmp', 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False)
    shutil.move(DB_FILE + '.tmp', DB_FILE)
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        dst = os.path.join(BACKUP_DIR, 'backup_' + datetime.date.today().isoformat() + '.json')
        if not os.path.exists(dst): shutil.copy(DB_FILE, dst)
        olds = sorted(os.listdir(BACKUP_DIR))
        while len(olds) > 30: os.remove(os.path.join(BACKUP_DIR, olds.pop(0)))
    except Exception: pass

def list_backups():
    try:
        return sorted([f for f in os.listdir(BACKUP_DIR) if f.endswith('.json')], reverse=True)
    except Exception:
        return []

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(b)))
        self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith('/api/backups'):
            self._json(list_backups()); return
        if self.path.startswith('/api/backup/'):
            name = os.path.basename(self.path.split('/api/backup/')[1])
            p = os.path.join(BACKUP_DIR, name)
            if os.path.isfile(p):
                with open(p, 'rb') as f: b = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Disposition', 'attachment; filename="%s"' % name)
                self.send_header('Content-Length', str(len(b)))
                self.end_headers(); self.wfile.write(b)
            else:
                self.send_response(404); self.end_headers()
            return
        if self.path.startswith('/api/db'):
            d = load_db()
            if d is None: self._json({'rev': 0, 'db': None})
            else: self._json({'rev': _rev, 'db': {k: v for k, v in d.items() if k != '_rev'}})
            return
        p = HTML_FILE if self.path in ('/', '/index.html') else self.path.lstrip('/').split('?')[0]
        p = os.path.normpath(p)
        if not os.path.isfile(p): self.send_response(404); self.end_headers(); return
        ext = os.path.splitext(p)[1].lower()
        ct = {'.html': 'text/html; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg',
              '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml',
              '.ico': 'image/x-icon'}.get(ext, 'application/octet-stream')
        with open(p, 'rb') as f: b = f.read()
        self.send_response(200); self.send_header('Content-Type', ct)
        self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_POST(self):
        if self.path.startswith('/api/restore'):
            n = int(self.headers.get('Content-Length', 0))
            try:
                data = json.loads(self.rfile.read(n).decode('utf-8'))
                name = os.path.basename(str(data.get('file', '')))
                p = os.path.join(BACKUP_DIR, name)
                if os.path.isfile(p):
                    with open(p, encoding='utf-8') as f: d = json.load(f)
                    save_db(d)
                    self._json({'ok': True, 'rev': _rev})
                else:
                    self._json({'ok': False, 'error': 'not found'}, 404)
            except Exception as e:
                self._json({'ok': False, 'error': str(e)}, 400)
            return
        if self.path.startswith('/api/db'):
            n = int(self.headers.get('Content-Length', 0))
            try:
                save_db(json.loads(self.rfile.read(n).decode('utf-8')))
                self._json({'ok': True, 'rev': _rev})
            except Exception as e:
                self._json({'ok': False, 'error': str(e)}, 400)
        else:
            self.send_response(404); self.end_headers()

if __name__ == '__main__':
    print('=' * 55)
    print('  🌐 isp-billing-Working Now')
    print('  From this pc:      http://localhost:%d' % PORT)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80))
        print('  From any pc :  http://%s:%d' % (s.getsockname()[0], PORT)); s.close()
    except Exception: pass
    print('  DATABASE: ' + os.path.abspath(DB_FILE))
    print('  BACKUP: ' + os.path.abspath(BACKUP_DIR))
    print('  To stop server: Ctrl+C — Do not close this window!')
    print('=' * 55)
    ThreadingHTTPServer(('0.0.0.0', PORT), H).serve_forever()
