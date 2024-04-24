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
                length = int(input("Length: "))
                width = int(input("Width: "))
                height = int(input("Height: "))
                print("\n")
                print("Volume = length * width * height")
                volume = (length * width * height)
                print("Volume = ", volume , "cubic.units")
            elif shape == "cone":
                radius = int(input("Radius: "))
                height = int(input("Height: "))
                print("\n")
                print("Volume = pi * radius * radius * height / 3")
                volume = ((math.pi * radius**2 * height)/3)
                print("Volume = ", volume, "cubic.units")
            elif shape == "cylinder":
                radius = int(input("Radius: "))
                height = int(input("Height: "))
                print("\n")
                print("Volume = pi * radius * radius * height")
                volume = (math.pi * radius**2 * height)
                print("Volume = ", volume, "cubic.units")
            elif shape == "sphere":
                radius = int(input("Radius: "))
                print("\n")
                print("Volume = (4/3) * pi * radius * radius * radius")
                volume = ((4/3) * math.pi * radius**3)
                print("Volume = ", volume, "cubic.units")
            if volume > 50:
                for i in range(10):
                    for j in range(int(volume/10)):
                        print("#", end="")
                    print()
            else:
                    for k in range(volume):
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





    
