# Weather CLI

Консольный скрипт для получения текущей погоды по названию города.

**API**: Open-Meteo

## Запуск

### Локально

```bash
cd task2
pip install -r requirements.txt
python weather.py --city "Москва"
python weather.py # Или с интерактивным вводом
```

### Docker

```bash
cd task2
docker compose up --build
docker compose run --rm weather --city "Баку"
```

## Пример вывода:
```bash
% python weather.py 
Введите название города: Baku
Ищем: Baku...
Нашел: Баку, Азербайджан
...
Погода в БАКУ, Азербайджан
Температура : 21.0 C
Влажность : 71%
Скорость ветра : 14.0 км/ч

% python weather.py --city "Москва"
Ищем: Москва...
Нашел: Москва, Россия
...
Погода в МОСКВА, Россия
Температура : 29.5 C
Влажность : 29%
Скорость ветра : 8.8 км/ч
```