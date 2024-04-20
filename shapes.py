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
                    for i in range(int(area/10)):
                        print("#", end="")
                    print()
                else:
                for k in range(area):
                    print("#", end="")
