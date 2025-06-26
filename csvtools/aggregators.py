import statistics

def aggregate_rows(rows: list[dict[str, str]], instruction: str) -> float:
    #Разбираем instruction

    column, operation = instruction.split('=')
    AGGREGATORS = {
    'avg': lambda values: sum(values) / len(values),
    'min': min,
    'max': max,
    'median': statistics.median
}
    values = [float(row[column]) for row in rows]
    result = AGGREGATORS[operation](values)
    return result

    
 