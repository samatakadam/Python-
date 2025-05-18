def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()