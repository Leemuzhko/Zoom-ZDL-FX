# Варианты MIDI-маршрута — проверено 2026-10-06

[English](MIDI_ROUTING.md)

Daniel Schmitt из nerds.de письменно разрешил 2026-10-06 запрошенное бесплатное
некоммерческое распространение с оригинальным, неизменённым, подписанным
установщиком LoopBe1, сохранением лицензии и авторства. Общие коммерческие условия
остаются действующими. На отдельный вопрос о цене branded-сборки ответа нет.
Текущий контроллер 0.1.2 не включает драйвер; этот docs-update не реализует его
интеграцию в установщик.

Windows MIDI Services предоставляет native loopback с совместимостью WinMM.
MIDI 2.0 loopback — перекрёстная пара A/B; Basic Loopback имеет одно имя, как
LoopBe1. Текущая документация Microsoft планирует массовую доступность Basic
Loopback на конец ноября 2026; разработчикам он доступен сейчас. Проверять
возможности конкретного ПК, а не предполагать их у любой Windows 11. Использовать
пользовательские, а не diagnostic endpoints. Имена можно настроить.

Контроллер использует RtMidi WinMM; совместимость приёма из созданного native-
порта ожидается по документации. Создание порта требует MIDI Services tools/SDK.
Текущая кнопка DAW ещё ищет LoopBe1. Win11 runtime/audio не проверены: компьютер
сборки — Win10 22H2/build19045. Драйверы и службы не устанавливались. Будущий
вариант — native при наличии возможностей и LoopBe1 как fallback; это план,
а не функция выпущенного контроллера.

Официальные источники:

- [Обзор Windows MIDI Services](https://microsoft.github.io/MIDI/)
- [Loopback A/B](https://microsoft.github.io/MIDI/kb/virtual-loopback/)
- [Basic Loopback и сроки внедрения](https://microsoft.github.io/MIDI/tools/midiloopbacksetup/)
- [Совместимость WinMM](https://microsoft.github.io/MIDI/sdk-reference/Transports/BasicLoopback/)
- [Ограничения diagnostic endpoints](https://microsoft.github.io/MIDI/kb/diagnostic-endpoints/)
