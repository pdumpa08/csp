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
                print("Volume = length * width * height")
                volume = (length*width*height)
                print("Volume = ", volume , "cubic.units")
            elif shape == "cone":
                radius = input("Radius: ")
                height = input("Height: ")
                print("\n")
                print("Volume = pi * radius * radius * height / 3")
                volume = ((math.pi*radius**2*height)/3)
                print("Volume = ", volume, "cubic.units")
            elif shape == "cylinder":
                radius = input("Radius: ")
                height = input("Height: ")
                print("\n")
                print("Volume = pi * radius * radius * height")
                volume = (math.pi*radius**2*height)
                print("Volume = ", volume, "cubic.units")
            elif shape == "sphere":
                radius = input("Radius: ")
                print("\n")
                print("Volume = (4/3) * pi * radius * radius * radius")
                volume = ((4/3)*math.pi*radius**3)
                print("Volume = ", volume, "cubic.units")
