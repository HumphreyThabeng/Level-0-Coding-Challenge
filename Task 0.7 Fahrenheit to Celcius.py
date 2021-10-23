f = float(input("Enter temperature in Fahrenheit: "))


def Fanrenheit_Conv(f):
    celcius = (f - 32) * (5 / 9)
    return celcius


print("The temperature in Celcius is " + str(Fanrenheit_Conv(f)))
