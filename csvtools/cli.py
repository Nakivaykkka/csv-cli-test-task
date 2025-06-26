import argparse

def parse_args():
    # Создаем парсер и добавляем аргументы 
    parser = argparse.ArgumentParser(description="CSV processor")

    parser.add_argument(
        '--file', 
        required=True,
        help="Путь к CSV-файлу"
    )
    parser.add_argument(
        '--where',
        help="Фильтрация в виде column=value / column>value / column<value"
    )
    parser.add_argument(
        '--aggregate',
        help="Агрегация в виде column=avg / column=min / column=max"
    )
    parser.add_argument(
    '--order-by',
    help='Сортировка в формате column=asc или column=desc'
)
    # Возращаем результаты 
    return parser.parse_args()
