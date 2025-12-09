import pandas as pd

# Функцията получава "raw" данни от API и ги подрежда
def transform_weather(raw_data):

    transformed = {
        "city": raw_data.get("name"),
        "temperature": raw_data["main"].get("temp"),
        "feels_like": raw_data["main"].get("feels_like"),
        "humidity": raw_data["main"].get("humidity"),
        "weather": raw_data["weather"][0].get("description"),
        "wind_speed": raw_data["wind"].get("speed")
    }

    # Превръщаме в DataFrame
    df = pd.DataFrame([transformed])

    return df


if __name__ == "__main__":
    sample = {
        "name": "Sofia",
        "main": {"temp": 5, "feels_like": 3, "humidity": 80},
        "weather": [{"description": "cloudy"}],
        "wind": {"speed": 3.5}
    }
    print(transform_weather(sample))
