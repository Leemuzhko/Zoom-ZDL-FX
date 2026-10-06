<p align="center">
  <h1 align="center">Zoom ZDL FX</h1>
</p>

<p align="center"><strong>Готовые пользовательские эффекты для оригинальной ZDL-платформы Zoom MS-series.</strong><br>
Модели усилителей, кабинетов и IR-эффекты в одном репозитории.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Format-ZDL-475569?style=flat-square" alt="Format: ZDL">
  <img src="https://img.shields.io/badge/Platform-Zoom_MS--series-2563eb?style=flat-square" alt="Platform: Zoom MS-series">
  <img src="https://img.shields.io/badge/Status-Experimental-92400e?style=flat-square" alt="Status: experimental">
  <img src="https://img.shields.io/badge/License-MIT-475569?style=flat-square" alt="License: MIT">
</p>

<p align="center"><a href="README.md">English</a> · <strong>Русский</strong></p>

<p align="center"><strong>Целевые устройства:</strong><br>
MS-50G · MS-70G · MS-60B · G1on · G1Xon · B1on<br>
<sub>Это целевая совместимость репозитория; не каждый эффект одинаково протестирован на каждой из перечисленных моделей.</sub></p>

<h3 align="center"><a href="https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest">Скачать все эффекты</a></h3>

<p align="center"><a href="#эффекты">Отдельные загрузки</a> · <a href="#установка-через-zoom-effect-manager">Установка</a> · <a href="https://ko-fi.com/leemuzhko">Поддержать на Ko-fi</a> · <a href="https://www.patreon.com/Leemuzhko">Поддержать на Patreon</a></p>

---

Здесь я собираю готовые рабочие ZDL-эффекты для оригинального/legacy поколения Zoom MS-series. Репозиторий рассчитан прежде всего на тех, кто хочет установить готовый эффект без самостоятельной сборки.

Разработка продолжается. Целевое семейство устройств: **MS-50G / MS-70G / MS-60B / G1on / G1Xon / B1on**. Поведение пользовательского ZDL может зависеть от конкретной педали, прошивки, цепочки эффектов и общей DSP-нагрузки, поэтому такие эффекты следует считать экспериментальными и проверять аккуратно.

## Эффекты

Каждый эффект распространяется как **полная папка-пакет**. Файлы `.ZDL`, одноимённый `.json`, PNG-иконку/изображение и остальные сопутствующие файлы нужно держать вместе.

В каталогах проектов показаны отдельные PNG-копии с непрозрачным белым фоном.
Исходные иконки Manager в `zdl/` и скачиваемые пакеты эффектов не изменены.

<!-- BEGIN GENERATED EFFECT CATALOG -->

| Type / Group | Project | Effects | Catalog / Description |
| --- | --- | ---: | --- |
| Filter (2) | HYBRID IR | 4 | [Catalog](zdl/filter/hybrid-ir/README.ru.md) |
| Filter (2) | Stereo IR loaders | 5 | [Catalog](zdl/filter/stereo-ir/README.ru.md) |
| Drive (3) | Experimental NAM captures | 2 | [Catalog](zdl/drive/nam/README.ru.md) |
| GuitarAmp (4) | Modified Guitar Amps | 6 | [Catalog](zdl/guitar-amp/modified-amps/README.ru.md) |
| SFX (7) | SYNTHESIS SYNx2 | 1 | [Catalog](zdl/sfx/synthesis/README.ru.md) |

<!-- END GENERATED EFFECT CATALOG -->

В релиз также входит общий архив **All-ZDL-FX-<версия>.zip** со всей коллекцией.

Карточки и загрузки находятся в каталогах проектов выше. Для каждого проекта
есть архив `<проект>-project.zip`. [Поддержка каталога](CATALOG.ru.md).

### SYNTHESIS SYNx2 + MIDI-контроллер

[Эффект, Windows-установщик и инструкция DAW](zdl/sfx/synthesis/README.ru.md).

## Установка через Zoom Effect Manager

### 1. Установите Zoom Effect Manager

Актуальную версию можно скачать здесь:

**[Zoom Effect Manager — Скачать](https://zoomeffectmanager.com/ru/download/)**

### 2. Создайте папку для пользовательских эффектов

Удобный вариант структуры:

```text
Zoom Effect Manager/
└─ Custom Effects/
   ├─ MS1960/
   │  ├─ MS1960.ZDL
   │  ├─ MS1960.json
   │  └─ HYBRIDIR.png
   ├─ GJ_IR/
   │  ├─ GJ_IR.ZDL
   │  ├─ GJ_IR.json
   │  └─ GJ_IR.png
   └─ ...
```

Для эффектов, скачанных ZIP-пакетом, **распакуйте саму папку эффекта в `Custom Effects/`**. Не вынимайте из неё только ZDL: JSON, изображение/иконка и другие сопровождающие файлы должны оставаться рядом.

Одиночные ZDL также можно положить прямо в `Custom Effects/` или в любую подпапку.

### 3. Укажите эту папку в Zoom Effect Manager

В Zoom Effect Manager:

1. Откройте **Настройки**.
2. Включите **Читать эффекты из папки** для ZDL.
3. Добавьте/выберите созданную родительскую папку, например:
   `Zoom Effect Manager/Custom Effects/`
4. После добавления или изменения файлов перезапустите Zoom Effect Manager.

Программа читает выбранную папку рекурсивно, поэтому каждый эффект можно спокойно держать в собственной подпапке.

Подробно: **[Чтение эффектов из папки](https://zoomeffectmanager.com/ru/posts/reading-effects-from-folder/)**.

### 4. Запишите эффект в педаль

Подключите Zoom к компьютеру **до запуска Zoom Effect Manager**, откройте раздел эффектов, выберите нужный эффект и запишите его в устройство.

См. также: **[Zoom Effect Manager — Быстрый старт](https://zoomeffectmanager.com/ru/posts/quick-start/)**.

Сначала проверяйте один пользовательский эффект в простой цепочке. Перед экспериментами рекомендуется сохранить резервную копию эффектов и пресетов.

## Примечание про IR Loader

Некоторые варианты IR Loader могут превысить доступный DSP-бюджет в зависимости от длины IR и остальных эффектов в цепочке. Если появляются треск или другие артефакты, используйте более короткую конфигурацию или более лёгкий режим маршрутизации, если он предусмотрен эффектом.

Поле DSP cost в экспериментальных/пользовательских эффектах не следует считать точным процентом загрузки процессора.

## Создание собственных кабинетных эффектов

Если вы хотите использовать собственные импульсы кабинетов, а не только готовые эффекты, смотрите проект **[HYBRID IR](https://github.com/Leemuzhko/HYBRID-IR)**.

HYBRID IR позволяет подготавливать обычные IR и гибридные FIR/IIR-модели и упаковывать их для поддерживаемых Zoom workflow.

## Releases

Тег вида `v*` (например `v1.0.0`) создаёт:

- отдельный ZIP каждого эффекта из `catalog.json`, с прежними именами;
- ZIP каждого проекта, включая SYNTHESIS с Windows-контроллером;
- отдельный Windows-установщик SYNTHESIS и инструкция DAW;
- общий архив `All-ZDL-FX-<версия>.zip` со всей коллекцией.

Workflow также можно запустить вручную из GitHub Actions — будут собраны те же ZIP-файлы как artifacts без публикации Release.

## Поддержать проект

Если эти эффекты вам полезны, можно поддержать мою работу на [Ko-fi](https://ko-fi.com/leemuzhko) или [Patreon](https://www.patreon.com/Leemuzhko). Это помогает оплачивать разработку, тестирование и документацию.

Эффекты остаются бесплатными; донат не покупает функции, приоритетную поддержку или сроки релиза.

## Лицензия

Репозиторий распространяется по лицензии [MIT](LICENSE).

Zoom — торговая марка Zoom Corporation. Это независимый пользовательский проект, не связанный с Zoom Corporation и не одобренный ею.
