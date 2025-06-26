def order_rows(rows: list[dict[str, str]], ordering: str) -> list[dict[str, str]]:
    if '=' not in ordering:
        raise ValueError("Неверный формат сортировки. Используй column=asc|desc")

    column, direction = ordering.split('=')

    reverse = direction.lower() == 'desc'

    try:
        # Пытаемся привести к числу — если можно
        return sorted(rows, key=lambda row: float(row[column]), reverse=reverse)
    except ValueError:
        # Если не число — сортируем как строки
        return sorted(rows, key=lambda row: row[column], reverse=reverse)
