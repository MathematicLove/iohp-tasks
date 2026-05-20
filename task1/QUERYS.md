# Задача 1

### Запросы в чат

1. Вот моя структура директорий (корневая task1) - app/: docker-compose.yml, Dockerfile, templates/,routers/, schemas/, services/, requirements.txt.
Подойдет ли она для создания FastAPI приложения ?

Ответ: Структура выглядит логично и хорошо подходит для FastAPI-проекта. Есть чёткое разделение ответственности (routers, services, schemas, templates) — это плюс.
Однако я советую вынести Docker-файлы в корень проекта:

Dockerfile
docker-compose.yml
requirements.txt

Такое расположение является стандартным и более удобным при работе с Docker.

2. Создай красивый UI с использованием Jinja2, (я еще буду использовать uvicorn) для FastAPI и сделай под UI под конвертер метрик
(длина, масса, температура, объем). Пока без логики чисто шаблон. 

Ответ: (выдал шаблон HTML)

3. Убери лишние надписи, убери menu-bar он там не нужен, убери надписи ниже окна конвертера. Сделай по ГОСТ стандартам UX.

Ответ: Исправил HTML 

4. Вот мой код конвертера - (прикрепил файлы unit_converter.py, converter.py, routers/converter.py) - 
исправь логику - при вызове swap метода из одной метрики в другую, должна меняться и сама метрика автоматически.

Ответ: Исправил логику

5. Сервер не отвечает при запуске с docker (docker-compose), лог из docker. Объясни что не так:
```sh
app-1  | TypeError: unhashable type: 'dict'
app-1  | INFO:     172.18.0.1:57426 - "GET /favicon.ico HTTP/1.1" 404 Not Found
app-1  | INFO:     172.18.0.1:57434 - "GET /apple-touch-icon-precomposed.png HTTP/1.1" 404 Not Found
app-1  | INFO:     172.18.0.1:57436 - "GET /apple-touch-icon.png HTTP/1.1" 404 Not Found
app-1  | INFO:     172.18.0.1:57452 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```

Ответ: В index.html нужно убрать использование Jinja-переменных (всё грузится через JS): dict в шаблон. Jinja2 не может закешировать dict → unhashable type.

Свое решение: `request` поменял, оставил без категорий, так как была ошибка с Jinja2.

### Ошибки чата

1. Свое решение: Исправление счетчика (GUI) - защита от спуска до значений $< 0$, для массы, длины, объема.

2. В чате было явно сказано - моя ВМ на mac: `colima`, использующая синтаксис `docker-compose` вместо `docker compose`, для команд в CLI. Однако чат постоянно выдавал `docker compose`. 
