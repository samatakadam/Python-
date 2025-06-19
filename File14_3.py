class Book:
    def __init__(self, price):
        self._price = price  # private attribute

    def set_price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative.")

    def get_price(self):
        return self._price

def main():
    b1 = Book(300)
    print("Initial Price:", b1.get_price())

    b1.set_price(450)
    print("Updated Price:", b1.get_price())

    b1.set_price(-100)  # Try setting an invalid price

if __name__=="_main_":
    main()