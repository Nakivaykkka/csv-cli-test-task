import tempfile
import os
from csvtools.reader import read_csv


def test_read_csv_reads_rows_correctly():
    # Подготовка тестового CSV-файла
    content = "name,brand,price\niphone,apple,999\ngalaxy,samsung,1199\n"

    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv") as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # Тестируем чтения
        rows = read_csv(tmp_path)

        assert len(rows) == 2
        assert rows[0]["name"] == "iphone"
        assert rows[0]["brand"] == "apple"
        assert rows[0]["price"] == "999"
        assert rows[1]["name"] == "galaxy"
    finally:
        os.remove(tmp_path)
