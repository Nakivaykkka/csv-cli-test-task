from csvtools.sorter import order_rows

def test_order_by_numeric_asc():
    rows = [
        {"name": "poco", "price": "299"},
        {"name": "iphone", "price": "999"},
        {"name": "galaxy", "price": "1199"},
    ]
    sorted_rows = order_rows(rows, "price=asc")
    assert sorted_rows[0]["name"] == "poco"
    assert sorted_rows[1]["name"] == "iphone"
    assert sorted_rows[2]["name"] == "galaxy"

def test_order_by_numeric_desc():
    rows = [
        {"name": "poco", "price": "299"},
        {"name": "iphone", "price": "999"},
        {"name": "galaxy", "price": "1199"},
    ]
    sorted_rows = order_rows(rows, "price=desc")
    assert sorted_rows[0]["name"] == "galaxy"
    assert sorted_rows[1]["name"] == "iphone"
    assert sorted_rows[2]["name"] == "poco"

def test_order_by_text_asc():
    rows = [
        {"brand": "xiaomi"},
        {"brand": "apple"},
        {"brand": "samsung"},
    ]
    sorted_rows = order_rows(rows, "brand=asc")
    assert sorted_rows[0]["brand"] == "apple"
    assert sorted_rows[1]["brand"] == "samsung"
    assert sorted_rows[2]["brand"] == "xiaomi"
