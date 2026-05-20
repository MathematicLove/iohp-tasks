from typing import Dict, List

class UnitConverter:
    CONVERSIONS = {
        "length": {
            "base": "meter",
            "units": {
                "meter": 1.0,
                "kilometer": 1000.0,
                "centimeter": 0.01,
                "millimeter": 0.001,
                "micrometer": 1e-6,
                "inch": 0.0254,
                "foot": 0.3048,
                "yard": 0.9144,
                "mile": 1609.344,
            },
            "label": "Длина"
        },
        "mass": {
            "base": "kilogram",
            "units": {
                "kilogram": 1.0,
                "gram": 0.001,
                "milligram": 1e-6,
                "pound": 0.453592,
                "ounce": 0.0283495,
                "ton": 1000.0,
            },
            "label": "Масса"
        },
        "temperature": {
            "units": ["celsius", "fahrenheit", "kelvin"],
            "label": "Температура"
        },
        "volume": {
            "base": "liter",
            "units": {
                "liter": 1.0,
                "milliliter": 0.001,
                "cubic_meter": 1000.0,
                "gallon": 3.78541,
                "quart": 0.946353,
                "pint": 0.473176,
            },
            "label": "Объём"
        }
    }

    @staticmethod
    def get_categories() -> Dict[str, str]:
        return {k: v["label"] for k, v in UnitConverter.CONVERSIONS.items()}

    @staticmethod
    def get_units(category: str) -> List[str]:
        if category not in UnitConverter.CONVERSIONS:
            return []
        data = UnitConverter.CONVERSIONS[category]
        if "units" in data and isinstance(data["units"], dict):
            return list(data["units"].keys())
        elif category == "temperature":
            return data["units"]
        return []

    @staticmethod
    def convert(category: str, from_unit: str, to_unit: str, value: float) -> float:
        # === НОВАЯ ВАЛИДАЦИЯ ===
        if not isinstance(value, (int, float)) or value != value:  # NaN
            raise ValueError("Значение должно быть числом")
        
        if category in ["length", "mass", "volume"]:
            if value < 0:
                raise ValueError(f"Значение не может быть отрицательным для {category}")
            # Защита от слишком больших/маленьких чисел (Python float limits)
            if abs(value) > 1e308:
                raise ValueError("Слишком большое число (превышен лимит float)")

        if category not in UnitConverter.CONVERSIONS:
            raise ValueError(f"Неизвестная категория: {category}")

        data = UnitConverter.CONVERSIONS[category]

        if category == "temperature":
            return UnitConverter._convert_temperature(from_unit, to_unit, value)
        else:
            factors = data["units"]
            if from_unit not in factors or to_unit not in factors:
                raise ValueError("Неверные единицы измерения")
            base_value = value * factors[from_unit]
            result = base_value / factors[to_unit]
            return round(result, 6)

    @staticmethod
    def _convert_temperature(from_unit: str, to_unit: str, value: float) -> float:
        # ... (оставь как было)
        if from_unit == "celsius":
            c = value
        elif from_unit == "fahrenheit":
            c = (value - 32) * 5 / 9
        elif from_unit == "kelvin":
            c = value - 273.15
        else:
            raise ValueError("Неверная исходная единица температуры")

        if to_unit == "celsius":
            return round(c, 4)
        elif to_unit == "fahrenheit":
            return round(c * 9 / 5 + 32, 4)
        elif to_unit == "kelvin":
            return round(c + 273.15, 4)
        else:
            raise ValueError("Неверная целевая единица температуры")