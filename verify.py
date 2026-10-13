from pathlib import Path
from bs4 import BeautifulSoup
import json
from urllib.parse import urlsplit
root=Path(__file__).parent/'dist';errors=[];count=0
for file in root.rglob('*.html'):
 s=BeautifulSoup(file.read_text(),'html.parser');count+=1
 if len(s.select('h1'))!=1:errors.append(f'{file}: h1')
 if not s.select_one('meta[name=description]'):errors.append(f'{file}: description')
 for script in s.select('script[type="application/ld+json"]'):json.loads(script.string)
 for el in s.select('a[href],img[src],script[src],link[href]'):
  url=el.get('src') or el.get('href');path=urlsplit(url).path
  if url.startswith('/'):
   target=root/path.lstrip('/')
   if not (target.is_file() or (target/'index.html').is_file()):errors.append(f'{file}: missing {path}')
assert not errors,'\n'.join(errors)
posts=json.loads((root.parent/'archive.json').read_text());assert len(posts)==32
for p in posts:assert len(BeautifulSoup(p['body'],'html.parser').get_text().split())>100
print(f'PASS: {count} HTML files, internal links, local assets, metadata, JSON-LD and 32 complete migrated posts')
