import math

# Purpose: To calculate the area of 2D shapes
# Input: The shape the user wants to calculate, and the length/width/base/height/top_base/bottom_base/radius
# Output: The formula to calculate the area, the area, and a representation of the area with hashes
# Acknowledge: Procedure done by partner
def two_id_calc(shape):
    if shape == "rectangle":
        length = float(input("Length: "))
        width = float(input("Width: "))
        print("\n")
        print("Area = length * width")
        area = length * width
        print("Area = ", (length * width), "sq.units")
    elif shape == "triangle":
        base = float(input("Base: "))
        height = float(input("Height: "))
        print("\n")
        print("Area = (1/2) * base * height")
        area = ((0.5) * base * height)
        print("Area = ", ((0.5) * base * height), "sq.units")
    elif shape == "trapezoid":
        top_base = float(input("Base One: "))
        bottom_base = float(input("Base Two: "))
        height = float(input("Height: "))
        print("\n")
        print("Area = (1/2) * (base_one + base_two) * height")
        area = ((0.5) * (top_base + bottom_base) * height)
        print("Area = ", ((0.5) * (top_base + bottom_base) * height), "sq.units")
    elif shape == "circle":
        radius = float(input("Radius: "))
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
        for k in range(int(area)):
            print("#", end="")
    print("\n")


# Purpose: To calculate the volume of 3D shapes
# Input: The shape the user wants to calculate, and the length/width/height/radius
# Output: The formula to calculate the volume, the volume, and a representation of the volume with hashes
# Acknowledge: Procedure done by ME
def three_id_calc(shape):
            if shape == "rectangular prism":
                length = float(input("Length: "))
                width = float(input("Width: "))
                height = float(input("Height: "))
                print("\n")
                print("Volume = length * width * height")
                volume = (length * width * height)
                print("Volume = ", volume , "cubic.units")
            elif shape == "cone":
                radius = float(input("Radius: "))
                height = float(input("Height: "))
                print("\n")
                print("Volume = pi * radius * radius * height / 3")
                volume = ((math.pi * radius**2 * height)/3)
                print("Volume = ", volume, "cubic.units")
            elif shape == "cylinder":
                radius = float(input("Radius: "))
                height = float(input("Height: "))
                print("\n")
                print("Volume = pi * radius * radius * height")
                volume = (math.pi * radius**2 * height)
                print("Volume = ", volume, "cubic.units")
            elif shape == "sphere":
                radius = float(input("Radius: "))
                print("\n")
                print("Volume = (4/3) * pi * radius * radius * radius")
                volume = ((4/3) * math.pi * radius**3)
                print("Volume = ", volume, "cubic.units")
                
            print()
            if volume > 50:
                for i in range(20):
                    for j in range(int(volume/20)):
                        print("#", end="")
                    print()
            else:
                    for k in range(int(volume)):
                        print("#", end="")
            print("\n")

# Purpose: To determine which procedure to use based on the shape the user wants to analyze
# Input: The shape the user wants to calculate
# Output: The ouput of either procedure two_id_calc or procedure three_id_calc
# Acknowledgements: 
# Partner: two_shapes list; iteration, selection, and calling of two_id_calc
# ME: three_shapes list; iteration, selection, and calling of three_id_calc
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
