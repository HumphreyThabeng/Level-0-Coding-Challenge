
c = int(input("How Many Numbers Would You Like to compare? "))
a = 0
max_num = 0

while a != c:
    num1 = int(input("Enter a Number: "))
    if max_num < num1:
        max_num = num1
        a += 1

    print('Maximum number is ' + str(max_num))





