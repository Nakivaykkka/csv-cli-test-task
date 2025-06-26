from csvtools.filters import filter_rows

def test_filter_string_equals():
    rows = [
        {"name": "iphone", "brand": "apple", "price": "999"},
        {"name": "galaxy", "brand": "samsung", "price": "1199"},
        {"name": "redmi", "brand": "xiaomi", "price": "299"},
    ]
    
    result = filter_rows(rows, "brand=xiaomi")
    
    assert len(result) == 1
    assert result[0]["brand"] == "xiaomi"
    assert result[0]["name"] == "redmi"
    assert result[0]["price"] == "299"

def test_filter_price_greater_than():
    rows = [
        {"name": "poco", "brand": "xiaomi", "price": "299"},
        {"name": "iphone", "brand": "apple", "price": "999"},
        {"name": "galaxy", "brand": "samsung", "price": "1199"},
    ]

    result = filter_rows(rows, "price>500")

    assert len(result) == 2
    assert result[0]["name"] == "iphone"
    assert result[1]["name"] == "galaxy"
    

def test_filter_price_less_than():
    rows = [
        {"name": "poco", "brand": "xiaomi", "price": "299"},
        {"name": "iphone", "brand": "apple", "price": "999"},
        {"name": "galaxy", "brand": "samsung", "price": "1199"},
    ]

    result = filter_rows(rows, "price<1000")

    assert len(result) == 2
    assert result[0]["name"] == "poco"
    assert result[1]["name"] == "iphone"
