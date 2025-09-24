import pytest
from sqlalchemy import create_engine, text


@pytest.fixture(scope="module")
def connection():
    # строка подключения
    engine = (
        create_engine(
            "postgresql+psycopg2://postgres:OblupaSQL@localhost:5432/postgres")
    )

    with engine.connect() as conn:
        # создаём таблицу, если ещё нет
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS students (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """))
        conn.commit()
        yield conn
        # очищаем таблицу после тестов
        conn.execute(text("TRUNCATE TABLE students"))
        conn.commit()
