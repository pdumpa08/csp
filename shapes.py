import math

two_or_three = input("Would you like to analyze a 2D or 3D shape? ")
shape = input("Which shape would you like to analyze? ")
three_shapes = ["rectangular prism", "cone", "cylinder", "sphere"]

def threeidcalc(shape):
    for x in three_shapes:
        if three_shapes[x] == shape:
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
            
                
def rectangle(length, width):
    print("Area = Width * Height")
    print(length * width)

def trapezoid(topBase, bottomBase, height):
    print("Area = [(topBase + bottomBase)/2] * Height")
    print([(topBase + bottomBase)/2] * height)

def circle(radius):
    print("Area = (radius * radius) * π(3.14...)")
    print(radius**2 * math.pi)
