from tabulate import tabulate


from csvtools.cli import parse_args
from csvtools.reader import read_csv
from csvtools.filters import filter_rows
from csvtools.aggregators import aggregate_rows
from csvtools.sorter import order_rows

def main():
    # Чтение аргументов командной строки
    args = parse_args()

    # Чтение строк из CSV-файла
    rows = read_csv(args.file)
    
    # Применение фильтрации, если указана
    if args.where:
        rows = filter_rows(rows, args.where)
        print(f"Применена фильтрация: {args.where}")
    
    # Применение сортировки, если указана
    if args.order_by:
        rows = order_rows(rows, args.order_by)
        print(f"Применена сортировка: {args.order_by}")
    
    # Вывод отфильтрованных и/или отсортированных строк
    if rows:
        print(tabulate(rows, headers="keys", tablefmt="grid"))
    else:
        print("Нет данных для отображения.")

    
    # Выполнение агрегации, если указана
    if args.aggregate:
        result = aggregate_rows(rows, args.aggregate)
        print(f"Агрегация: {args.aggregate}")
        print(f"Результат: {result}")

# Запуск
if __name__ == "__main__":
    main()
