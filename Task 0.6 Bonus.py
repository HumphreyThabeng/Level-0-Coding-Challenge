c = int(input("How Many Numbers Would You Like to compare: "))
x = 1
list=[]


while x <= c:
    Q1 = int(input("Enter your Number: "))
    x += 1
    print(Q1)
    list.append(Q1)
    list.sort()

print("Maximum value is " + str(list[-1]))