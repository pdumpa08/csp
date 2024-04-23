import math


def two_id_calc(shape):
    
    if shape == "rectangle":
        length = int(input("Length: "))
        width = int(input("Width: "))
        print("\n")
        print("Area = length * width")
        area = length * width
        print("Area = ", (length * width), "sq.units")
    elif shape == "triangle":
        base = int(input("Base: "))
        height = int(input("Height: "))
        print("\n")
        print("Area = (1/2) * base * height")
        area = ((0.5) * base * height)
        print("Area = ", ((0.5) * base * height), "sq.units")
    elif shape == "trapezoid":
        top_base = int(input("Base One: "))
        bottom_base = int(input("Base Two: "))
        height = int(input("Height: "))
        print("\n")
        print("Area = (1/2) * (base_one + base_two) * height")
        area = ((0.5) * (top_base + bottom_base) * height)
        print("Area = ", ((0.5) * (top_base + bottom_base) * height), "sq.units")
    elif shape == "circle":
        radius = int(input("Radius: "))
        print("\n")
        print("Area = pi * radius * radius")
        area = (math.pi * radius**2)
        print("Area = ", (math.pi * radius**2), "sq.units")

    print()
    if area > 50:
        for i in range(10):
            for j in range(int(area/10)):
                print("#", end="")
            print()
    else:
        for k in range(area):
            print("#", end="")
    print("\n")

def three_id_calc(shape):
            if shape == "rectangular prism":
                length = input("Length: ")
                width = input("Width: ")
                height = input("Height: ")
                prism(length, width, height)
            elif shape == "cone":
                radius = input("Radius: ")
                height = input("Height: ")
                cone(radius, height)
            elif shape == "cylinder":
                radius = input("Radius: ")
                height = input("Height: ")
                cylinder(radius, height)
            elif shape == "sphere":
                radius = input("Radius: ")
                sphere(radius)
            if area > 50:
            for i in range(10):
                for j in range(int(area/10)):
                    print("#", end="")
                print()
            else:
                for k in range(area):
                    print("#", end="")
            print("\n")


def main():
    print()
    shape = input("Which shape would you like to analyze? ")
    two_shapes = ["rectangle", "triangle", "trapezoid", "circle"]
    three_shapes = ["rectangular prism", "cone", "cylinder", "sphere"]

    for two_shape in two_shapes:
        if two_shape == shape:
            two_id_calc(shape)

    for three_shape in three_shapes:
        if three_shape == shape:
            three_id_calc(shape)


if __name__=="__main__": 
    main()





    
