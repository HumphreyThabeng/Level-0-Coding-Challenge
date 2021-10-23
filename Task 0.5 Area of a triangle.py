Side_1 = int(input("Enter Length of Side 1: "))
Side_2 = int(input("Enter Length of Side 2: "))
Side_3 = int(input("Enter Length of Side 3: "))


def Area_of_triangle():
    x = (Side_1, Side_2, Side_3)
    SideLength = sum(x)
    Area = int(0.5 * SideLength)
    return Area


print(Area_of_triangle())