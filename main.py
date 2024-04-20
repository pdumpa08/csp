def main():
    two_or_three = input("Would you like to analyze a 2D or 3D shape? ")
    shape = input("Which shape would you like to analyze? ")
    two_shapes = ["rectangle", "triangle", "trapezoid", "circle"]
    three_shapes = ["rectangular prism", "cone", "cylinder", "sphere"]

    if shape == "rectangle":
        length = input("Length: ")
        width = input("Width: ")
        rectangle(length, width)
    elif shape == "triangle":
        base = input("Base: ")
        height = input("Height: ")
        triangle(base, height)
    elif shape == "trapezoid":
        top_base = input("Base One: ")
        bottom_base = input("Base Two: ")
        height = input("Height: ")
        trapezoid(top_base, bottom_base, height)
    elif shape == "circle":
        radius = input("Radius: ")
        circle(radius)
    elif shape == "rectangular prism":
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

    