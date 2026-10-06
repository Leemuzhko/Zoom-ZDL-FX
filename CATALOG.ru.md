# Поддержка каталога

[English](CATALOG.md)

Корневой README — индекс проектов. Пакеты расположены по схеме
`zdl/<тип>/<проект>/<эффект>/`; исходные ZDL, JSON и изображение хранятся вместе.
Типы соответствуют GID: Filter 2, Drive 3, GuitarAmp 4, SFX 7; проекты — семействам
продукта.

`catalog.json` хранит принадлежность и редакционные описания EN/RU. Начальные
описания перенесены из пользовательских README ревизии
`febcec184ed54e7653a28ffe88322007883066f9`, а не старых sidecar JSON. ID/версия/GID
читаются из ZDL; имя для Manager и ссылка на изображение — из sidecar.
Таблицы эффектов сортируются по числовому ID из ZDL по возрастанию; при одинаковом
ID — по имени. Порядок в EN и RU одинаковый.

Для нового эффекта положить полный пакет в проект и добавить запись в manifest.
Для проекта добавить парные README с маркерами каталога. Ручной текст вне маркеров
сохраняется.

```text
python -m pip install -r scripts/requirements.txt
python scripts/update_catalog.py
python scripts/update_catalog.py --check
python -m unittest discover -s tests -v
python scripts/package_release.py --version preview
```

Упаковка использует manifest, сохраняя прежние имена `<эффект>.zip`, и добавляет
`<проект>-project.zip` и `All-ZDL-FX-<версия>.zip`. SYNTHESIS и общий архив содержат
контроллер; EXE, инструкция и отчёт прикладываются также отдельно. LoopBe1 остаётся
внешним. `tests/package-baseline.json` хранит хеши пакетов до перемещения.

PR проверяет каталоги, хеши и архивы и создаёт workflow artifacts. Только тег `v*`
публикует Release. Этот PR не сливает main и не публикует новый релиз; существующие
теги и release assets не изменяются.
