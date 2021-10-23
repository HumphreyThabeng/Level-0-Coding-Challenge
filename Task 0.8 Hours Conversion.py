num = int(input("Please Enter your time in minutes: "))


def conversion():
    hours = int(num / 60)
    remainder = int(num % 60)
    if hours == 1 and remainder == 1:
        print(str(hours) + " hour " + str(remainder) + " minute")
    elif hours == 1 and remainder != 1:
        print(str(hours) + " hour " + str(remainder) + " minutes")
    elif hours != 1:
        print(str(hours) + " hours " + str(remainder) + " minutes")


conversion()
