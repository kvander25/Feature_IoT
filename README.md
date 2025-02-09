# Проект: Умный горшок для растений с использованием моделирования портов
Выполнили студенты гр.ЭВТ-22-1БЗу
kvander25:    Луговой
Pe1enev:      Пеленев

Описание проекта:
Для проекта "Умный горшок для растений" с использованием Python на Linux, 
мы можем создать модель IoT-устройства, имитируя работу с физическими портами через файлы. 
Этот подход помогает реализовать логику, без необходимости работы с конкретным оборудованием, например, с Raspberry Pi.

Умный горшок для растений должен мониторить параметры окружающей среды (влажность почвы, температура, свет) и управлять поливом растения. Примерная логика работы:
- Система считывает данные с датчиков (влажности, температуры и света).
- Если влажность почвы ниже порога, включается насос для полива.
- Если температура слишком высокая, система может запускать вентилятор.
- Все данные записываются в файлы для мониторинга и анализа.

Предположим, что все датчики и устройства управления имитируются с помощью файлов:
- soilmoisture.txt — файл с уровнем влажности почвы.
- temperature.txt — файл с текущей температурой.
- light.txt — файл с уровнем света.
- pumpstate.txt — файл, в котором хранится состояние насоса (включен/выключен).
- fanstate.txt — файл, в котором хранится состояние вентилятора (включен/выключен).
- light.txt — файл с уровнем света.
- display.txt — файл с выводом данных на дисплей.

Описание файлов и их формат
1. soilmoisture.txt: Хранит значение влажности почвы в процентах (например, 45%).
2. temperature.txt: Хранит текущую температуру (например, 25°C).
3. light.txt: Хранит значение освещенности (например, 350 люксов).
4. pumpstate.txt: Хранит состояние насоса, 0 — выключен, 1 — включен.
5. fanstate.txt: Хранит состояние вентилятора, 0 — выключен, 1 — включен.
6. display.txt: Хранит значения вывода на дисплей, температуры и освещенности.

Примечания:
В реальной системе данные с датчиков считываются через порты ввода/вывода, но для имитации в Linux мы используем файлы.

![image](https://github.com/user-attachments/assets/96b67cb7-e241-4764-aae7-2c60943a103b)

