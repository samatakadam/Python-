class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting the car engine...")
        print("Checking mirrors and seatbelt.")
        print("Car is ready to go!")

def main():
    v = Vehicle()
    c = Car()

    print("Vehicle:")
    v.start()

    print("\nCar:")
    c.start()

if __name__=="_main_":
    main()