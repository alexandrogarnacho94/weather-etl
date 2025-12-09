import requests
import yaml

# Чете настройките от settings.yaml
def load_config():
    with open("config/settings.yaml", "r") as file:
        return yaml.safe_load(file)

# Извлича прогнозата от сайта 
def extract_weather():
    config = load_config()
    api = config["weather_api"]

    url = api["base_url"]
    params = {
        "q": api["city"],
        "appid": api["api_key"],
        "units": api["units"]
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

if __name__ == "__main__":
    print(extract_weather())
