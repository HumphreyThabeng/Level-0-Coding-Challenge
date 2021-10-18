f = int(input("Enter temperature in Fahrenheit: "))


def Fanrenheit_Conv(f):
    celcius = (f - 32)*5/9
    print(round(celcius, 2))

print("The temperature in Celcius is ")
Fanrenheit_Conv(f)

