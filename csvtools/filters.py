
def filter_rows(rows: list[dict[str, str]], condition: str) -> list[dict[str, str]]:
    # Разбираем condition 
    for op in ('<','>','='):
        if op in condition:
            column, value = condition.split(op)
            break
            
    #Цикл по строкам
    flitered = []
    for row in rows:
        value_in_row = row[column]
        
        #Условия 
        if op == '>' and float(value_in_row) > float(value):
            flitered.append(row)
        elif op == '<' and float(value_in_row) < float(value):
            flitered.append(row)
        elif op == '=' and value_in_row == value:
            flitered.append(row)
    # Возвращаем список после цикла   
    return flitered 
        
        
        
    
    