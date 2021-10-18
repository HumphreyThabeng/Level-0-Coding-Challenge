num = int(input("Please Enter your time in Hours: "))


def conversion():
    minutes = int(num / 60)
    remainder = int(num % 60)
    print(str(minutes) + " hours " + str(remainder) + " minutes")


conversion()
