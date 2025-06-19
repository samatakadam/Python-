class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

def main():
    print("\n--- Number 1 ---")
    obj1 = Numbers()
    obj1.Factors()
    print("Sum of Factors:", obj1.SumFactors())
    print("Is Prime?", obj1.ChkPrime())
    print("Is Perfect?", obj1.ChkPerfect())

    print("\n--- Number 2 ---")
    obj2 = Numbers()
    obj2.Factors()
    print("Sum of Factors:", obj2.SumFactors())
    print("Is Prime?", obj2.ChkPrime())
    print("Is Perfect?", obj2.ChkPerfect())

if __name__=="_main_":
    main()