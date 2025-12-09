import yaml
from sqlalchemy import create_engine

# Зарежда конфигурацията
def load_config():
    with open("config/settings.yaml", "r") as file:
        return yaml.safe_load(file)

# Зарежда данните в PostgreSQL
def load_to_postgres(df):
    config = load_config()
    db_url = config["database"]["url"]

    # Прави връзка към базата
    engine = create_engine(db_url)

    # Пише таблицата в PostgreSQL
    df.to_sql(
        name="weather_data",
        con=engine,
        if_exists="append",  # добавя нови записи
        index=False
    )

    print("Data successfully loaded into PostgreSQL!")


if __name__ == "__main__":
    import pandas as pd
    sample = pd.DataFrame([{"city": "Sofia", "temperature": 5}])
    load_to_postgres(sample)

