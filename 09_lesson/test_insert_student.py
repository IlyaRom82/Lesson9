# внесение изменений
from sqlalchemy import text


def test_insert_student(connection):
    connection.execute(
        text("INSERT INTO students (id, name, age) VALUES (1, 'Alice', 25)")
    )
    result = connection.execute(
        text("SELECT * FROM students WHERE id=1")
    ).mappings().fetchone()  # возвращает dict-подобный объект

    assert result['name'] == 'Alice'
