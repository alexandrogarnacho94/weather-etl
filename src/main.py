from extract import extract_weather
from transform import transform_weather
from load import load_to_postgres

def main():
    print("Starting ETL pipeline...")

    #  EXTRACT
    print("Extracting weather data...")
    raw_data = extract_weather()

    #  TRANSFORM
    print("Transforming data...")
    df = transform_weather(raw_data)

    #  LOAD
    print("Loading data into PostgreSQL...")
    load_to_postgres(df)

    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    main()

