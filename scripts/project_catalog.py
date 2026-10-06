"""Validate the distribution manifest and generate bounded project catalogues."""
import argparse
import html
from io import BytesIO
import json
from pathlib import Path
import struct
from PIL import Image

BEGIN = '<!-- BEGIN GENERATED EFFECT CATALOG -->'
END = '<!-- END GENERATED EFFECT CATALOG -->'
GROUPS = {'filter': (2, 'Filter'), 'drive': (3, 'Drive'),
          'guitar-amp': (4, 'GuitarAmp'), 'sfx': (7, 'SFX')}
RELEASE = 'https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/'


def cell(value):
    return html.escape(str(value), quote=False).replace('|', '&#124;').replace('\n', ' ')


def load(root):
    manifest = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    projects = {p['id']: p for p in manifest['projects']}
    if len(projects) != len(manifest['projects']):
        raise ValueError('Duplicate project')
    names, paths = set(), set()
    for effect in manifest['effects']:
        project = projects[effect['project']]
        folder = (root / effect['path']).resolve()
        if not folder.is_relative_to(root.resolve()) or folder.parent != (root / project['path']).resolve():
            raise ValueError('Invalid effect path')
        if effect['name'] in names or folder in paths:
            raise ValueError('Duplicate effect')
        names.add(effect['name']); paths.add(folder)
        zdls = list(folder.glob('*.ZDL'))
        metas = list(folder.glob('*.json'))
        if len(zdls) != 1 or len(metas) != 1:
            raise ValueError('Each effect needs one ZDL and JSON')
        raw = zdls[0].read_bytes()
        if raw[60] != GROUPS[project['type']][0]:
            raise ValueError('Type/GID mismatch: ' + effect['name'])
        effect['meta'] = json.loads(metas[0].read_text(encoding='utf-8-sig'))
        icon = (folder / effect['meta']['iconFile']).resolve()
        if not icon.is_relative_to(folder) or not icon.is_file():
            raise ValueError('Invalid icon path')
        effect.update(gid=raw[60], effect_id=struct.unpack_from('<H', raw, 64)[0],
                      version=raw[68:72].decode('ascii'), filename=zdls[0].name)
    actual = {p.parent.resolve() for p in (root / 'zdl').rglob('*.ZDL')}
    if actual != paths:
        raise ValueError('Manifest must cover every ZDL exactly once')
    return manifest


def replace_section(text, generated):
    lines = text.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.strip() == BEGIN]
    ends = [i for i, line in enumerate(lines) if line.strip() == END]
    if len(starts) != 1 or len(ends) != 1 or starts[0] >= ends[0]:
        raise ValueError('Exactly one ordered marker pair is required')
    return ''.join(lines[:starts[0] + 1]) + '\n' + generated + '\n\n' + ''.join(lines[ends[0]:])


def render(root):
    manifest = load(root)
    outputs = {}
    for lang, filename in [('en', 'README.md'), ('ru', 'README.ru.md')]:
        index = [('| Type / Group | Project | Effects | Catalog / Description |' if lang == 'en'
                  else '| Тип / группа | Проект | Эффекты | Каталог / описание |'),
                 '| --- | --- | ---: | --- |']
        for project in manifest['projects']:
            effects = [e for e in manifest['effects'] if e['project'] == project['id']]
            gid, group = GROUPS[project['type']]
            title = project.get('title_ru', project['title']) if lang == 'ru' else project['title']
            label = 'Каталог' if lang == 'ru' else 'Catalog'
            index.append(f'| {group} ({gid}) | {title} | {len(effects)} | [{label}]({project["path"]}/{filename}) |')
            rows = [('| Effect Card | Effect Description | Effect Group | ID | Version | File Name | Download |' if lang == 'en'
                     else '| Карточка эффекта | Описание эффекта | Группа | ID | Версия | Имя файла | Скачать |'),
                    '| --- | --- | --- | --- | --- | --- | --- |']
            for effect in effects:
                rows.append('| ' + ' | '.join([
                    f'<img src="cards/{effect["name"]}.png" alt="{html.escape(effect["meta"]["name"], quote=True)}" width="128" height="96">',
                    cell(effect['description'][lang]), f'{group} ({gid})', str(effect['effect_id']),
                    effect['version'], '`' + effect['filename'] + '`',
                    f'[ZIP]({RELEASE}{effect["name"]}.zip)']) + ' |')
                with Image.open(root / effect['path'] / effect['meta']['iconFile']) as source:
                    rgba = source.convert('RGBA')
                    white = Image.new('RGBA', rgba.size, (255, 255, 255, 255))
                    encoded = BytesIO()
                    Image.alpha_composite(white, rgba).convert('RGB').save(encoded, format='PNG')
                    outputs[root / project['path'] / 'cards' / (effect['name'] + '.png')] = encoded.getvalue()
            project_readme = root / project['path'] / filename
            outputs[project_readme] = replace_section(project_readme.read_text(encoding='utf-8'), '\n'.join(rows)).encode('utf-8')
        path = root / filename
        outputs[path] = replace_section(path.read_text(encoding='utf-8'), '\n'.join(index)).encode('utf-8')
    return outputs


def matches(path, content):
    if not path.is_file():
        return False
    if path.suffix == '.png':
        # Pillow/zlib compression may differ by platform/version; compare the
        # actual white-matte image, not its incidental PNG encoding.
        with Image.open(path) as current, Image.open(BytesIO(content)) as expected:
            return current.mode == expected.mode and current.size == expected.size and current.tobytes() == expected.tobytes()
    return path.read_bytes() == content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    outputs = render(args.root.resolve())
    if args.check:
        stale = [str(p) for p, content in outputs.items() if not matches(p, content)]
        if stale:
            parser.exit(1, 'Stale catalogues: ' + ', '.join(stale) + '\n')
    else:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    print('Project catalogues validated')


if __name__ == '__main__':
    main()
