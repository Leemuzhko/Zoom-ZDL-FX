<p align="center">
  <h1 align="center">Zoom ZDL FX</h1>
</p>

<p align="center"><strong>Готовые пользовательские эффекты для оригинальной ZDL-платформы Zoom MS-series.</strong><br>
Модели усилителей, кабинетов и IR-эффекты в одном репозитории.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Format-ZDL-475569?style=flat-square" alt="Format: ZDL">
  <img src="https://img.shields.io/badge/Platform-Zoom_MS--series-2563eb?style=flat-square" alt="Platform: Zoom MS-series">
  <img src="https://img.shields.io/badge/Status-Experimental-92400e?style=flat-square" alt="Status: experimental">
  <img src="https://img.shields.io/badge/License-GPL--3.0-475569?style=flat-square" alt="License: GPL-3.0">
</p>

<p align="center"><a href="README.md">English</a> · <strong>Русский</strong></p>

<h3 align="center"><a href="https://github.com/Leemuzhko/Zoom-ZDL-FX/releases">Скачать все эффекты</a></h3>

<p align="center"><a href="#эффекты">Отдельные загрузки</a> · <a href="#установка">Установка</a> · <a href="https://ko-fi.com/leemuzhko">Поддержать на Ko-fi</a></p>

---

Здесь я собираю готовые рабочие ZDL-эффекты для оригинального/legacy поколения Zoom MS-series. Репозиторий рассчитан прежде всего на тех, кто хочет установить готовый эффект без самостоятельной сборки.

Разработка продолжается. Поведение пользовательского ZDL может зависеть от конкретной педали, прошивки, цепочки эффектов и общей DSP-нагрузки, поэтому такие эффекты следует считать экспериментальными и проверять аккуратно.

## Эффекты

Ссылки ниже скачивают актуальные файлы напрямую из ветки `main`.

| Эффект | Пакет | Скачать |
| --- | --- | --- |
| **CABSIM** | Отдельный ZDL | [CABSIM.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/CABSIM.ZDL) |
| **ENGL** | Отдельный ZDL | [ENGL.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/ENGL.ZDL) |
| **ENGL-2** | Отдельный ZDL | [ENGL-2.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/ENGL-2.ZDL) |
| **JCM800** | Отдельный ZDL | [JCM800.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/JCM800.ZDL) |
| **PLEXI** | Отдельный ZDL | [PLEXI.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/PLEXI.ZDL) |
| **IRDUAL4** | ZDL + metadata | [Открыть папку](zdl/DUAL%20IR/) |
| **MS1960** | ZDL + metadata | [Открыть папку](zdl/MS1960/) |
| **MS1960 V30 T1** | ZDL + metadata | [Открыть папку](zdl/MS1960_V30_T1/) |
| **MS1960 V30 T2** | ZDL + metadata | [Открыть папку](zdl/MS1960_V30_T2/) |

При выпуске релиза GitHub Actions автоматически упаковывает всю папку `zdl/` в один ZIP и прикладывает его к GitHub Release.

<a id="установка"></a>

## Установка

1. Скачайте нужный эффект или полный ZIP со страницы [Releases](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases).
2. Перенесите ZDL на педаль с помощью [Zoom Effect Manager](https://zoomeffectmanager.com/en/download/).
3. Сначала проверяйте один пользовательский эффект в простой цепочке.
4. Если появляются треск, артефакты или нестабильность, уменьшите DSP-нагрузку и удалите последний добавленный эффект.

Перед экспериментами с пользовательскими ZDL рекомендуется сохранить резервную копию эффектов и пресетов.

## Примечание про IR Loader

Некоторые варианты IR Loader могут превысить доступный DSP-бюджет в зависимости от длины IR и остальных эффектов в цепочке. Если появляются треск или другие артефакты, используйте более короткую конфигурацию или более лёгкий режим маршрутизации, если он предусмотрен эффектом.

Поле DSP cost в экспериментальных/пользовательских эффектах не следует считать точным процентом загрузки процессора.

## Создание собственных кабинетных эффектов

Если вы хотите использовать собственные импульсы кабинетов, а не только готовые эффекты, смотрите проект **[HYBRID IR](https://github.com/Leemuzhko/HYBRID-IR)**.

HYBRID IR позволяет подготавливать обычные IR и гибридные FIR/IIR-модели и упаковывать их для поддерживаемых Zoom workflow.

## Releases и общий ZIP

Тег вида `v*` (например `v1.0.0`) запускает workflow релиза. Он создаёт:

```text
Zoom-ZDL-FX-v1.0.0.zip
```

с коллекцией `zdl/`, README и лицензией.

Workflow также можно запустить вручную из GitHub Actions — в этом случае будет собран тестовый ZIP без публикации Release.

## Поддержать проект

Если эти эффекты вам полезны, можно [поддержать мою работу на Ko-fi](https://ko-fi.com/leemuzhko). Это помогает оплачивать разработку, тестирование и документацию.

Эффекты остаются бесплатными; донат не покупает функции, приоритетную поддержку или сроки релиза.

## Лицензия

Репозиторий распространяется по лицензии [GNU General Public License v3.0](LICENSE).

Zoom — торговая марка Zoom Corporation. Это независимый пользовательский проект, не связанный с Zoom Corporation и не одобренный ею.
