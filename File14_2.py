class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def main():
    rect = Rectangle(10, 5)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())

if __name__=="_main_":
    main()