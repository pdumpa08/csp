import math

def main():
    two_or_three = input("Would you like to analyze a 2D or 3D shape? ")
    shape = input("Which shape would you like to analyze? ")
    three_shapes = ["rectangular prism", "cone", "cylinder", "sphere"]
    
    three_id_calc(shape)

if __name__=="__main__": 
    main()

def three_id_calc(shape):
    for x in three_shapes:
        if x == shape:
            if shape == "rectangular prism":
                length = input("Length: ")
                width = input("Width: ")
                height = input("Height: ")
                print("\n")
                print("Area = (1/2) * base * height")
                area = ((0.5) * base * height)
                print("Area = ", ((0.5) * base * height), "sq.units")
            elif shape == "cone":
                radius = input("Radius: ")
                height = input("Height: ")
                print("\n")
                print("Area = (1/2) * base * height")
                area = ((0.5) * base * height)
                print("Area = ", ((0.5) * base * height), "sq.units")
            elif shape == "cylinder":
                radius = input("Radius: ")
                height = input("Height: ")
                print("\n")
                print("Area = (1/2) * base * height")
                area = ((0.5) * base * height)
                print("Area = ", ((0.5) * base * height), "sq.units")
            elif shape == "sphere":
                radius = input("Radius: ")
                print("\n")
                print("Area = (1/2) * base * height")
                area = ((0.5) * base * height)
                print("Area = ", ((0.5) * base * height), "sq.units")
