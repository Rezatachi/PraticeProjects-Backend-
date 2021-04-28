
# Inquire height and width of wall

test_h = int(input("Height of wall:"))
test_w = int(input("height of width:"))
test_price = int(input("how much is a price of a can??"))


def paintcalc(height=test_h, width=test_w, price=test_price):
    price_accumulator = round((width*height) / price)
    print(
        f"Given that you stated your wall is {height} by {width} the cost will be {price_accumulator} dollars  ")


paintcalc()
