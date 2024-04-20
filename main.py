import math


def two_id_calc(shape):
    print("\n")
    if shape == "rectangle":
        length = int(input("Length: "))
        width = int(input("Width: "))
        print("Area = length * width")
        print("Area = ", (length * width), "sq.units")
    elif shape == "triangle":
        base = int(input("Base: "))
        height = int(input("Height: "))
        print("Area = (1/2) * base * height")
        print("Area = ", ((0.5) * base * height), "sq.units")
    elif shape == "trapezoid":
        top_base = int(input("Base One: "))
        bottom_base = int(input("Base Two: "))
        height = int(input("Height: "))
        print("Area = (1/2) * (base_one + base_two) * height")
        print("Area = ", ((0.5) * (top_base + bottom_base) * height), "sq.units")
    elif shape == "circle":
        radius = int(input("Radius: "))
        print("Area = pi * radius * radius")
        print("Area = ", (math.pi * radius * radius), "sq.units")
    print("\n")


def main():
    two_or_three = input("Would you like to analyze a 2D or 3D shape? ")
    shape = input("Which shape would you like to analyze? ")
    two_shapes = ["rectangle", "triangle", "trapezoid", "circle"]
    three_shapes = ["rectangular prism", "cone", "cylinder", "sphere"]

    if two_or_three == "2D":
        two_id_calc(shape)
    elif two_or_three == "3D":
        three_id_calc(shape)
    else:
        print("\n Invalid Input \n")


if __name__=="__main__": 
    main()





    