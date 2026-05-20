import sys
import requests
import argparse
from typing import Dict, Optional

def get_coordinates(city: str) -> Optional[Dict]:
    """Получаем координаты города через Open-Meteo Geocoding API"""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if not data.get("results"):
            return None
        result = data["results"][0]
        return {
            "name": result["name"],
            "country": result.get("country", ""),
            "latitude": result["latitude"],
            "longitude": result["longitude"]
        }
    except Exception:
        return None


def get_weather(lat: float, lon: float) -> Optional[Dict]:
    """Получаем текущую погоду"""
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&"
        f"current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&"
        f"timezone=auto"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["current"]
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Погода по городу (Open-Meteo)")
    parser.add_argument("--city", type=str, help="Название города")
    args = parser.parse_args()

    city = args.city or input("Введите название города: ").strip()
    if not city:
        print("Ошибка - город не указан")
        sys.exit(1)

    print(f"Ищем: {city}...")

    coords = get_coordinates(city)
    if not coords:
        print(f"Упс... город '{city}' не найден")
        sys.exit(1)

    print(f"Нашел! : {coords['name']}, {coords['country']}")
    print("...")

    weather = get_weather(coords["latitude"], coords["longitude"])
    if not weather:
        print("Не удалось получить данные :(")
        sys.exit(1)

    print(f"Погода в {coords['name'].upper()}, {coords['country']}")
    print(f"Температура : {weather['temperature_2m']} градусов Ц")
    print(f"Влажность : {weather['relative_humidity_2m']}")
    print(f"Скорость ветра : {weather['wind_speed_10m']} км/ч")


if __name__ == "__main__":
    main()