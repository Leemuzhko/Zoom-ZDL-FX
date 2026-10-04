"""Public README catalogue acceptance against the actual distribution files."""
from pathlib import Path
import json
import html
import struct
import unittest
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HEADER = '| Effect Card | Effect Description | Effect Group | ID | Version | File Name | Download |'
GROUPS = {2:'Filter',3:'Drive',4:'GuitarAmp',7:'SFX'}


class CatalogTests(unittest.TestCase):
    def test_bad_readme_preflight_does_not_write_any_generated_outputs(self):
        with tempfile.TemporaryDirectory(prefix='catalogue-failure-') as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT/'zdl/SYNX2',root/'zdl/SYNX2')
            for name in ('README.md','README.ru.md'):
                text = (ROOT/name).read_text(encoding='utf-8')
                if name == 'README.ru.md':
                    text = text.replace('<!-- END GENERATED EFFECT CATALOG -->','MISSING END MARKER')
                (root/name).write_text(text,encoding='utf-8')
            preview = root/'assets/effect-cards/SYNX2.png'
            preview.parent.mkdir(parents=True)
            preview.write_bytes(b'preserve previous derived artifact')
            before = {p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
            run = subprocess.run([sys.executable,'-B',str(ROOT/'scripts/update_catalog.py'),
                                  '--root',str(root)],capture_output=True)
            self.assertNotEqual(run.returncode,0)
            self.assertEqual({p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()},before)

    def test_generator_preserves_prose_and_description_like_old_sentinels(self):
        with tempfile.TemporaryDirectory(prefix='catalogue-test-') as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT/'zdl/SYNX2',root/'zdl/SYNX2')
            meta_path = root/'zdl/SYNX2/SYNX2.json'
            meta = json.loads(meta_path.read_text(encoding='utf-8'))
            meta['descriptionEng'] = 'A tagged release is mentioned inside this description.'
            meta['descriptionRus'] = 'В релиз также может входить описание.'
            meta_path.write_text(json.dumps(meta),encoding='utf-8')
            for name,heading in (('README.md','## Effects\n'),('README.ru.md','## Эффекты\n')):
                text = (ROOT/name).read_text(encoding='utf-8')
                note = 'KEEP THIS PROSE <!-- BEGIN GENERATED EFFECT CATALOG --> example <!-- END GENERATED EFFECT CATALOG -->'
                text = text.replace(heading,heading+'\n### User note\n'+note+'\n',1)
                (root/name).write_text(text,encoding='utf-8')
            command = [sys.executable,'-B',str(ROOT/'scripts/update_catalog.py'),'--root',str(root)]
            subprocess.run(command,check=True,capture_output=True)
            first = {name:(root/name).read_bytes() for name in ('README.md','README.ru.md')}
            self.assertTrue(all(note.encode() in content for content in first.values()))
            subprocess.run(command,check=True,capture_output=True)
            self.assertEqual({name:(root/name).read_bytes() for name in first},first)

    def test_white_preview_copies_preserve_size_and_opaque_source_pixels(self):
        from PIL import Image
        for folder in (p for p in (ROOT/'zdl').iterdir() if p.is_dir()):
            meta = json.loads(next(folder.glob('*.json')).read_text(encoding='utf-8-sig'))
            with Image.open(folder/meta['iconFile']) as source, \
                 Image.open(ROOT/'assets/effect-cards'/(folder.name+'.png')) as preview:
                self.assertEqual(preview.size,source.size)
                rgba = source.convert('RGBA')
                output = preview.convert('RGBA')
                self.assertEqual(output.getchannel('A').getextrema(),(255,255))
                for y in range(rgba.height):
                    for x in range(rgba.width):
                        r,g,b,a = rgba.getpixel((x,y))
                        expected = tuple((v*a+255*(255-a)+127)//255 for v in (r,g,b))+(255,)
                        self.assertEqual(output.getpixel((x,y)),expected,(folder.name,x,y))

    def test_catalogue_has_seven_columns_and_matches_every_package(self):
        for language in ('README.md','README.ru.md'):
            text = (ROOT/language).read_text(encoding='utf-8')
            self.assertTrue(HEADER in text,f'Missing seven-column catalogue: {language}')
            self.assertNotIn('| Display Name |',text)
            section = text.split('## Effects\n' if language == 'README.md' else '## Эффекты\n',1)[1]
            section = section.split('A tagged release' if language == 'README.md' else 'В релиз также',1)[0]
            rows = [line.strip('| ').split(' | ') for line in section.splitlines()
                    if line.startswith('| <img ')]
            folders = sorted((p for p in (ROOT/'zdl').iterdir() if p.is_dir()),
                             key=lambda p:(next(p.glob('*.ZDL')).read_bytes()[60],p.name))
            self.assertEqual(len(rows),len(folders))
            for cells,folder in zip(rows,folders):
                with self.subTest(language=language,effect=folder.name):
                    self.assertEqual(len(cells),7)
                    zdl = next(folder.glob('*.ZDL'))
                    meta = json.loads(next(folder.glob('*.json')).read_text(encoding='utf-8-sig'))
                    raw = zdl.read_bytes()
                    self.assertIn(f'assets/effect-cards/{folder.name}.png',cells[0])
                    description = meta.get('descriptionRus') if language == 'README.ru.md' else meta.get('descriptionEng')
                    if not description or '\ufffd' in description:
                        description = meta.get('descriptionEng') or meta['name']
                    self.assertEqual(cells[1],html.escape(description.strip(),quote=False))
                    self.assertEqual(cells[2],f'{GROUPS[raw[60]]} ({raw[60]})')
                    self.assertEqual(cells[3],str(struct.unpack_from('<H',raw,64)[0]))
                    self.assertEqual(cells[4],raw[68:72].decode('ascii'))
                    self.assertIn(zdl.name,cells[5])
                    self.assertIn(f'/download/{folder.name}.zip',cells[6])
            headings = [line for line in section.splitlines() if line.startswith('### ')]
            self.assertEqual(headings,['### Filter (2)','### Drive (3)','### GuitarAmp (4)','### SFX (7)'])


if __name__ == '__main__':
    unittest.main()
