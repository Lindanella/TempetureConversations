def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def convertToCentigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade

def doConversion(fahrenheit):
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f"Fahrenheit: {fahrenheit} Kelvin: {kelvin:.2f} Centigrade: {centigrade:.2f}")

def repeat():
    while True:
        try:
            num_conversions = int(input("How many conversions would you like to do this time? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for _ in range(num_conversions):
        fahrenheit = getFahrenheit()
        doConversion(fahrenheit)

def controlLoop():
    while True:
        answer = input("Do you want to do some conversions (Yes or No)? ").lower()
        if answer == 'yes':
            repeat()
        elif answer == 'no':
            break
        else:
            print("Please enter 'Yes' or 'No'.")

def getFahrenheit():
    while True:
        try:
            fahrenheit = float(input("Enter Fahrenheit temperature (must be -50 to 130): "))
            if -50 <= fahrenheit <= 130:
                return fahrenheit
            else:
                print("Temperature must be between -50 and 130.")
        except ValueError:
            print("Please enter a valid temperature.")

if __name__ == '__main__':
    main()
