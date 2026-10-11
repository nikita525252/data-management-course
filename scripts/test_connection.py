# scripts/test_connection.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from faker import Faker

load_dotenv()

DB_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DB_URL)
fake = Faker("ru_RU")

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS lab01_healthcheck (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(150),
            email VARCHAR(150),
            created_at TIMESTAMP DEFAULT now()
        )
    """))
    for _ in range(10):
        conn.execute(
            text("INSERT INTO lab01_healthcheck (full_name, email) VALUES (:n, :e)"),
            {"n": fake.name(), "e": fake.unique.email()}
        )
    conn.commit()

    result = conn.execute(text("SELECT count(*) FROM lab01_healthcheck"))
    print("Строк в таблице lab01_healthcheck:", result.scalar())
print("Подключение и запись в PostgreSQL работают.")
