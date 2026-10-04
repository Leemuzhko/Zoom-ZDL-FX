"""Public README catalogue acceptance against the actual distribution files."""
from pathlib import Path
import json
import html
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1]
HEADER = '| Effect Card | Display Name | Effect Description | Effect Group | ID | Version | File Name | Download |'
GROUPS = {2:'Filter',3:'Drive',4:'GuitarAmp',7:'SFX'}


class CatalogTests(unittest.TestCase):
    def test_catalogue_has_eight_columns_and_matches_every_package(self):
        for language in ('README.md','README.ru.md'):
            text = (ROOT/language).read_text(encoding='utf-8')
            self.assertTrue(HEADER in text,f'Missing eight-column catalogue: {language}')
            lines = text.split(HEADER,1)[1].split('\n\n',1)[0].splitlines()[2:]
            rows = [line.strip('| ').split(' | ') for line in lines if line.startswith('|')]
            folders = sorted(p for p in (ROOT/'zdl').iterdir() if p.is_dir())
            self.assertEqual(len(rows),len(folders))
            for cells,folder in zip(rows,folders):
                with self.subTest(language=language,effect=folder.name):
                    self.assertEqual(len(cells),8)
                    zdl = next(folder.glob('*.ZDL'))
                    meta = json.loads(next(folder.glob('*.json')).read_text(encoding='utf-8-sig'))
                    raw = zdl.read_bytes()
                    self.assertIn(f'zdl/{folder.name}/{meta["iconFile"]}',cells[0])
                    self.assertIn(meta['name'],cells[1])
                    description = meta.get('descriptionRus') if language == 'README.ru.md' else meta.get('descriptionEng')
                    if not description or '\ufffd' in description:
                        description = meta.get('descriptionEng') or meta['name']
                    self.assertEqual(cells[2],html.escape(description.strip(),quote=False))
                    self.assertEqual(cells[3],f'{GROUPS[raw[60]]} ({raw[60]})')
                    self.assertEqual(cells[4],str(struct.unpack_from('<H',raw,64)[0]))
                    self.assertEqual(cells[5],raw[68:72].decode('ascii'))
                    self.assertIn(zdl.name,cells[6])
                    self.assertIn(f'/download/{folder.name}.zip',cells[7])


if __name__ == '__main__':
    unittest.main()
