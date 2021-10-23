c = int(input("Enter Temperature in Celsius: "))


def celcius_conv(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit


print("The temperature in Fahrenheit is " + str(celcius_conv(c)))
