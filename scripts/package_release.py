"""Build effect, project and full-collection ZIPs from the validated manifest."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from project_catalog import load


def archive(output, source, prefix):
    with ZipFile(output, 'w', ZIP_DEFLATED) as target:
        for file in sorted(source.rglob('*')):
            if file.is_file():
                target.write(file, (Path(prefix) / file.relative_to(source)).as_posix())


def build(root, destination, version):
    manifest = load(root)
    controller = root / 'zdl/sfx/synthesis/controller/windows'
    receipt = json.loads((controller / 'windows-build-receipt.json').read_text(encoding='utf-8-sig'))
    installer = controller / receipt['installer']
    if hashlib.sha256(installer.read_bytes()).hexdigest() != receipt['sha256']:
        raise ValueError('Controller installer hash mismatch')
    destination.mkdir(parents=True, exist_ok=True)
    for effect in manifest['effects']:
        archive(destination / (effect['name'] + '.zip'), root / effect['path'], effect['name'])
    for project in manifest['projects']:
        archive(destination / (project['id'] + '-project.zip'), root / project['path'], project['id'])
    for file in controller.iterdir():
        if file.is_file():
            shutil.copy2(file, destination / file.name)
    with ZipFile(destination / f'All-ZDL-FX-{version}.zip', 'w', ZIP_DEFLATED) as target:
        for path in [root / 'zdl', root / 'assets']:
            for file in sorted(path.rglob('*')):
                if file.is_file():
                    target.write(file, ('Zoom-ZDL-FX-' + version + '/' + file.relative_to(root).as_posix()))
        for name in ('README.md', 'README.ru.md', 'LICENSE', 'catalog.json'):
            target.write(root / name, 'Zoom-ZDL-FX-' + version + '/' + name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required=True)
    parser.add_argument('--output', type=Path, default=Path('release-assets'))
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if '/' in args.version or '\\' in args.version:
        parser.error('Version cannot contain path separators')
    build(args.root.resolve(), args.output.resolve(), args.version)
