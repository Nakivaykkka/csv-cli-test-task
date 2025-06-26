
from csv import DictReader

def read_csv(path: str) -> list[dict[str, str]]:
    # читаем файл и выводим данные из файла 
    with open(path, mode="r", encoding="utf-8") as file:
        reader = DictReader(file)
        rows = list(reader)
        return rows