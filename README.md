# Weather ETL Project

Този проект събира данни за времето от интернет (OpenWeather API), обработва ги и ги записва в PostgreSQL база данни.

Как работи проектът

1. extract.py – взима данните от API.
2. transform.py – подрежда данните.
3. load.py – записва данните в базата.
4. main.py – стартира целия процес (ETL).

Файлове в проекта

weather-etl/
- src/ (тук е кодът)
- config/ (настройки, API ключове)
- data/ (папки за данни)
- requirements.txt (нужните библиотеки)
- README.md (този файл)

Как се стартира

1. Инсталирай библиотеките:
pip install -r requirements.txt

2. Стартирай ETL процеса:
python src/main.py

Конфигурация (settings.yaml)

Тук се съхранява API ключът и адресът на базата.

weather_api:
base_url: "https://api.openweathermap.org/data/2.5/weather"
api_key: "YOUR_API_KEY"
city: "Sofia"
units: "metric"

database:
url: "postgresql://postgres:password@localhost:5432/weatherdb"

Цел на проекта

Този проект е направен за да видя какво представлява Data Engineering и показва:
- работа с API
- обработка на данни
- запис в база данни
- ETL структура
