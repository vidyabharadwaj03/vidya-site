#!/usr/bin/env python3
"""Substitutes {{FONT_PLACEHOLDER}} tokens in index.template.html with the
base64-encoded font data in fonts/, writing the result to index.html.

Run this after editing index.template.html, then republish index.html
as the Claude Artifact.
"""
mapping = {
    'FRAUNCES500': 'fonts/fraunces500.woff2.b64',
    'FRAUNCES600': 'fonts/fraunces600.woff2.b64',
    'FRAUNCES500I': 'fonts/fraunces500i.woff2.b64',
    'PLEX400': 'fonts/plex400.woff2.b64',
    'PLEX500': 'fonts/plex500.woff2.b64',
}

with open('index.template.html', 'r') as f:
    html = f.read()

for key, path in mapping.items():
    with open(path, 'r') as f:
        b64 = f.read().strip()
    placeholder = '{{' + key + '}}'
    if placeholder not in html:
        print('WARNING: placeholder not found:', placeholder)
    html = html.replace(placeholder, b64)

with open('index.html', 'w') as f:
    f.write(html)

print('Wrote index.html —', len(html), 'bytes')
