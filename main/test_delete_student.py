from sqlalchemy import text


def test_delete_student(connection):
    # вставим студента, чтобы было что удалять
    connection.execute(
        text("INSERT INTO students (id, name) VALUES (3, 'Charlie')")
    )
    # удаляем
    connection.execute(text("DELETE FROM students WHERE id=3"))
    result = connection.execute(
        text("SELECT * FROM students WHERE id=3")).fetchone()
    assert result is None
