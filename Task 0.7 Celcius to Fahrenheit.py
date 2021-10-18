c = int(input("Enter Temperature in Celcius: "))


def celcius_conv(c):
    fahrenheit = (c * 9 / 5) + 32
    print(fahrenheit)

print("The in Fahrenheit is ")
celcius_conv(c)
