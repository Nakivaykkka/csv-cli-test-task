from csvtools.aggregators import aggregate_rows

def test_aggregate_avg():
    rows = [
        {"price": "299"},
        {"price": "999"},
        {"price": "1200"},
    ]

    result = aggregate_rows(rows, "price=avg")

    assert round(result, 2) == 832.67
    
def test_aggregate_min():
    rows = [
        {"price": "299"},
        {"price": "999"},
        {"price": "1200"},
    ]

    result = aggregate_rows(rows, "price=min")

    assert result == 299.0

def test_aggregate_max():
    rows = [
        {"price": "299"},
        {"price": "999"},
        {"price": "1200"},
    ]

    result = aggregate_rows(rows, "price=max")

    assert result == 1200.0

def test_aggregate_median():
    rows = [
        {"price": "100"},
        {"price": "500"},
        {"price": "300"},
    ]
    result = aggregate_rows(rows, "price=median")
    assert result == 300
