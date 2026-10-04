"""Generate grouped README tables and exact white-matte PNG preview copies."""
import argparse
from itertools import groupby
import html
from io import BytesIO
import json
from pathlib import Path
import struct

from PIL import Image

HEADER = '| Effect Card | Effect Description | Effect Group | ID | Version | File Name | Download |'
GROUPS = {2:'Filter',3:'Drive',4:'GuitarAmp',7:'SFX'}
BEGIN = '<!-- BEGIN GENERATED EFFECT CATALOG -->'
END = '<!-- END GENERATED EFFECT CATALOG -->'


def cell(value):
    return html.escape(str(value).strip(),quote=False).replace('|','&#124;').replace('\r',' ').replace('\n',' ')


def catalogue(root):
    effects = []
    previews = {}
    for folder in (root/'zdl').iterdir():
        if not folder.is_dir():
            continue
        zdl = next(folder.glob('*.ZDL'))
        meta = json.loads(next(folder.glob('*.json')).read_text(encoding='utf-8-sig'))
        raw = zdl.read_bytes()
        if raw[60] not in GROUPS:
            raise ValueError('Unsupported group: '+str(raw[60]))
        icon = folder/meta['iconFile']
        with Image.open(icon) as source:
            rgba = source.convert('RGBA')
            white = Image.new('RGBA',rgba.size,(255,255,255,255))
            encoded = BytesIO()
            Image.alpha_composite(white,rgba).convert('RGB').save(encoded,format='PNG')
            previews[folder.name+'.png'] = encoded.getvalue()
        effects.append(dict(folder=folder.name,meta=meta,gid=raw[60],
                            effect_id=struct.unpack_from('<H',raw,64)[0],
                            version=raw[68:72].decode('ascii'),filename=zdl.name))
    return sorted(effects,key=lambda e:(e['gid'],e['folder'])),previews


def tables(effects,language):
    sections = []
    for gid,entries in groupby(effects,key=lambda e:e['gid']):
        lines = [f'### {GROUPS[gid]} ({gid})','',HEADER,
                 '| --- | --- | --- | --- | --- | --- | --- |']
        for effect in entries:
            meta = effect['meta']
            description = meta.get('descriptionRus') if language == 'ru' else meta.get('descriptionEng')
            if not description or '\ufffd' in description:
                description = meta.get('descriptionEng') or meta['name']
            values = [f'<img src="assets/effect-cards/{effect["folder"]}.png" alt="{html.escape(meta["name"],quote=True)}" width="128" height="96">',
                      cell(description),f'{GROUPS[gid]} ({gid})',str(effect['effect_id']),
                      effect['version'],f'`{effect["filename"]}`',
                      f'[ZIP](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/{effect["folder"]}.zip)']
            lines.append('| '+' | '.join(values)+' |')
        sections.append('\n'.join(lines))
    return '\n\n'.join(sections)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    root = parser.parse_args().root.resolve()
    effects,previews = catalogue(root)
    readmes = {}
    for filename,language in (('README.md','en'),('README.ru.md','ru')):
        path = root/filename
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines(keepends=True)
        begins = [i for i,line in enumerate(lines) if line.rstrip('\r\n') == BEGIN]
        ends = [i for i,line in enumerate(lines) if line.rstrip('\r\n') == END]
        if len(begins) != 1 or len(ends) != 1:
            raise ValueError('README needs exactly one catalogue marker pair: '+filename)
        start = sum(len(line) for line in lines[:begins[0]+1])
        end = sum(len(line) for line in lines[:ends[0]])
        if end <= start:
            raise ValueError('Reversed catalogue markers: '+filename)
        text = text[:start]+'\n'+tables(effects,language)+'\n\n'+text[end:]
        readmes[path] = text
    # Preflight/render both documents and every input before any output write.
    preview_dir = root/'assets/effect-cards'
    preview_dir.mkdir(parents=True,exist_ok=True)
    for name,png in previews.items():
        (preview_dir/name).write_bytes(png)
    for path,text in readmes.items():
        path.write_text(text,encoding='utf-8')
    print(f'{len(effects)} effects grouped; opaque PNG copies generated')


if __name__ == '__main__':
    main()
