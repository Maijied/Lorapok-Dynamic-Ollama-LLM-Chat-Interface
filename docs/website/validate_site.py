import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '<title>' not in content or '</title>' not in content:
    sys.exit('Missing title tag')

if 'meta name="description"' not in content:
    sys.exit('Missing meta description')

ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))
for href in re.findall(r'href=["\']([^"\']+)["\']', content):
    if href.startswith('#'):
        target = href[1:]
        if target and target not in ids:
            sys.exit(f'Broken anchor link: {href}')

print('Site validation passed')
