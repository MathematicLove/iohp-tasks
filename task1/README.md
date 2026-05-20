# Unit Converter

Простой и быстрый конвертер единиц с современным интерфейсом.  
Поддерживает:
- Длина
- Масса
- Температура
- Объём

## Сайт - на pages всегда статический!!! - он не имеет логики так как не связан с FastAPI! Для запуска лучше прогнать через Docker/Uvicorn!
GitHub Pages: https://mathematiclove.github.io/iohp-tasks/task1

### Стек:

#### **Back-end:**
- FastAPI (Python 3.12)
- Pydantic
- Uvicorn

#### **Front-end:**
- HTML5 + Tailwind CSS
- JavaScript
- Font Awesome

- Docker + Docker Compose
- GitHub Pages (статическая версия)

### Запуск

#### Локально через uvicorn:

```bash
cd task1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Через Docker:

```bash
cd task1
docker-compose up --build -d
```

Остановка:
```bash
cd task1
docker-compose down
```
