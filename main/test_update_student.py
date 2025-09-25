from sqlalchemy import text


def test_update_student(connection):
    # вставим студента, чтобы было что обновлять
    connection.execute(
        text("INSERT INTO students (id, name) VALUES (2, 'Bob')")
    )
    # обновим имя
    connection.execute(text("UPDATE students SET name='Bobby' WHERE id=2"))
    result = connection.execute(
        text("SELECT * FROM students WHERE id=2")
    ).mappings().fetchone()

    assert result['name'] == 'Bobby'
