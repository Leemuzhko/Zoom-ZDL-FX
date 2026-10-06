"""Publication checks: preserved effect bytes, edited descriptions, links and ZIPs."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from project_catalog import load, render, matches
from package_release import build


class CatalogTests(unittest.TestCase):
    def test_all_original_effect_files_remain_byte_exact(self):
        baseline = json.loads((ROOT / 'tests/package-baseline.json').read_text())
        actual = {}
        for effect in load(ROOT)['effects']:
            for file in (ROOT / effect['path']).iterdir():
                if file.is_file():
                    actual[effect['name'] + '/' + file.name] = hashlib.sha256(file.read_bytes()).hexdigest()
        self.assertEqual(actual, baseline)

    def test_generated_catalogues_are_current_and_root_is_bounded(self):
        for file, content in render(ROOT).items():
            self.assertTrue(matches(file, content), str(file))
        manifest = load(ROOT)
        for language in ('README.md', 'README.ru.md'):
            root = (ROOT / language).read_text(encoding='utf-8')
            self.assertNotIn('| <img ', root)
            self.assertEqual(len([line for line in root.splitlines() if line.startswith('| ')]) - 2,
                             len(manifest['projects']))
            for project in manifest['projects']:
                text = (ROOT / project['path'] / language).read_text(encoding='utf-8')
                rows = [line for line in text.splitlines() if line.startswith('| <img ')]
                expected = [e for e in manifest['effects'] if e['project'] == project['id']]
                self.assertEqual(len(rows), len(expected))
                ids = [int(row.split(' | ')[3]) for row in rows]
                self.assertEqual(ids, sorted(ids))
                for row, effect in zip(rows, expected):
                    self.assertIn(effect['description']['ru' if language.endswith('.ru.md') else 'en'], row)
                    self.assertIn('/download/' + effect['name'] + '.zip', row)
                    self.assertIn('[' + effect['name'] + '.ZIP]', row)
                    self.assertEqual(len(row.split(' | ')), 6)

    def test_imported_user_descriptions_survive_generator(self):
        manifest = load(ROOT)
        ms1960 = next(e for e in manifest['effects'] if e['name'] == 'MS1960')
        self.assertEqual(ms1960['project'], 'hybrid-ir')
        self.assertEqual(ms1960['path'], 'zdl/filter/hybrid-ir/MS1960')
        self.assertEqual({e['name'] for e in manifest['effects'] if e['project'] == 'dual-ir'},
                         {'IRDUAL4', 'M1960VT1', 'M1960VT2', 'MS1960VS'})
        self.assertEqual(next(e for e in manifest['effects'] if e['name'] == 'IRDUAL4')['description']['en'],
                         'DUAL IR loader with 4x2048 taps IR bank. Experimental.')
        self.assertIn('Synthesator wit 2xOscillators',
                      next(e for e in manifest['effects'] if e['name'] == 'SYNX2')['description']['en'])

    def test_invalid_readme_causes_no_output_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'repo'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git', 'release-assets', '__pycache__'))
            path = root / 'zdl/sfx/synthesis/README.ru.md'
            path.write_text(path.read_text(encoding='utf-8').replace('<!-- END GENERATED EFFECT CATALOG -->', ''), encoding='utf-8')
            before = {p.relative_to(root): hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
            with self.assertRaises(ValueError):
                render(root)
            after = {p.relative_to(root): hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(before, after)

    def test_effect_cards_have_white_matte_and_original_size(self):
        from PIL import Image
        manifest = load(ROOT)
        projects = {p['id']: p for p in manifest['projects']}
        for effect in manifest['effects']:
            with Image.open(ROOT / effect['path'] / effect['meta']['iconFile']) as source, Image.open(
                    ROOT / projects[effect['project']]['path'] / 'cards' / (effect['name'] + '.png')) as card:
                self.assertEqual(source.size, card.size)
                self.assertEqual(card.convert('RGBA').getchannel('A').getextrema(), (255, 255))

    def test_preview_check_accepts_new_compression_but_rejects_changed_pixels(self):
        from io import BytesIO
        from PIL import Image
        path = ROOT / 'zdl/sfx/synthesis/cards/SYNX2.png'
        with Image.open(path) as image:
            same = BytesIO()
            image.save(same, format='PNG', compress_level=0)
            self.assertTrue(matches(path, same.getvalue()))
            altered = image.copy()
            original = image.getpixel((0, 0))
            altered.putpixel((0, 0), tuple(255 - channel for channel in original))
            different = BytesIO()
            altered.save(different, format='PNG')
            self.assertFalse(matches(path, different.getvalue()))

    def test_release_archives_preserve_single_effect_names_and_bundle_controller(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            (output / 'synthesis-project.zip').write_bytes(b'stale project archive')
            build(ROOT, output, 'test')
            manifest = load(ROOT)
            for effect in manifest['effects']:
                folder = ROOT / effect['path']
                with ZipFile(output / (effect['name'] + '.zip')) as archive:
                    self.assertEqual(set(archive.namelist()), {effect['name'] + '/' + f.name for f in folder.iterdir() if f.is_file()})
                    for file in folder.iterdir():
                        if file.is_file():
                            self.assertEqual(archive.read(effect['name'] + '/' + file.name), file.read_bytes())
            self.assertFalse((output / 'synthesis-project.zip').exists())
            self.assertTrue((output / 'SYNTHESIS-SYNx2-0.1.2-Windows-x64-Setup.exe').is_file())
            with ZipFile(output / 'All-ZDL-FX-test.zip') as archive:
                self.assertIn('Zoom-ZDL-FX-test/catalog.json', archive.namelist())
                self.assertIn('Zoom-ZDL-FX-test/zdl/sfx/synthesis/SYNX2/SYNX2.ZDL', archive.namelist())
                self.assertIn('Zoom-ZDL-FX-test/zdl/sfx/synthesis/controller/windows/SYNTHESIS-SYNx2-0.1.2-Windows-x64-Setup.exe', archive.namelist())

    def test_local_markdown_and_card_links_exist(self):
        import re
        for readme in ROOT.rglob('*.md'):
            if '.git' in readme.parts or 'release-assets' in readme.parts:
                continue
            for target in re.findall(r'\]\(([^)]+)\)|src="([^"]+)"', readme.read_text(encoding='utf-8')):
                value = next(x for x in target if x)
                if value.startswith(('http:', 'https:', '#')):
                    continue
                self.assertTrue((readme.parent / value.split('#')[0]).exists(), (readme, value))


if __name__ == '__main__':
    unittest.main()
