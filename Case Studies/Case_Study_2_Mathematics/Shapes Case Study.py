import math


def squareparameter(side):
    return 4 * side


def squarearea(side):
    return side * side


def rectangleparameter(a, b):
    return (2 * a) + (2 * b)


def rectanglearea(a, b):
    return a * b


def circleparameter(radius):
    return 2 * math.pi * radius


def circlearea(radius):
    return math.pi * math.pow(radius, 2)


def triangleperimeter(a, b, c):
    return a + b + c


def trianglearea(breadth, height):
    return (1 / 2) * breadth * height


def paralellogramperimeter(a, b):
    return (2 * a) + (2 * b)


def paralellogramarea(b, h):
    return b * h


def circularringarea(outerradius, innerradius):
    return math.pi * (math.pow(outerradius, 2) - math.pow(innerradius, 2))


def spheresurfacearea(radius):
    return 4 * math.pi * math.pow(radius, 2)


def spherevolume(radius):
    return (4 * math.pi * math.pow(radius, 3)) / 3


def trapezoidperimeter(a, b, c, d):
    return (a + b + c + d)


def trapezoidarea(a, b, height):
    return height * ((a + b) / 2)


def rectangularboxarea(a, b, c):
    return (2 * a * b) + (2 * a * c) + (2 * b * c)


def rectangularboxvolume(a, b, c):
    return a * b * c


def cubearea(length):
    return 6 * math.pow(length, 2)


def cubevolume(length):
    return math.pow(length, 3)


def cylinderarea(radius, height):
    return 2 * math.pi * radius * (radius + height)


def cylindervolume(radius, height):
    return math.pi * radius * radius * height


def getinput():
    shape = input("Enter a shape:\n")
    return shape


# gets the shape name and computes
def compute(shape):
    shapedata = dict()
    shape = str(shape)
    if shape.lower() == "square":
        shapedata["name"] = "Square"
        side = float(input("Enter side:\n"))
        shapedata["Perimeter"] = squareparameter(side)
        shapedata["Area"] = squarearea(side)
        return shapedata
    elif shape.lower() == "rectangle":
        shapedata["name"] = "rectangle"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        shapedata["Perimeter"] = rectangleparameter(a, b)
        shapedata["Area"] = rectanglearea(a, b)
        return shapedata
    elif shape.lower() == "circle":
        shapedata["name"] = "circle"
        r = float(input("Enter values of radius:\n"))
        shapedata["Perimeter"] = circleparameter(r)
        shapedata["Area"] = circlearea(r)
        return shapedata
    elif shape.lower() == "triangle":
        shapedata["name"] = "triangle"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        c = float(input("Enter values for c:\n"))
        shapedata["Perimeter"] = triangleperimeter(a, b, c)
        breadth = float(input("Enter values for breadth:\n"))
        height = float(input("Enter values for height:\n"))
        shapedata["Area"] = trianglearea(breadth, height)
        return shapedata
    elif shape.lower() == "parallelogram":
        shapedata["name"] = "parallelogram"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        shapedata["Perimeter"] = paralellogramperimeter(a, b)
        height = float(input("Enter values for height:\n"))
        shapedata["Area"] = paralellogramarea(b, height)
        return shapedata
    elif shape.lower() == "circular ring":
        shapedata["name"] = "circular ring"
        outerradi = float(input("Enter values of outer radius:\n"))
        innerradi = float(input("Enter values of inner radius:\n"))
        shapedata["Area"] = circularringarea(outerradi, innerradi)
        return shapedata
    elif shape.lower() == "sphere":
        shapedata["name"] = "sphere"
        radi = float(input("Enter values of radius:\n"))
        shapedata["surface area"] = spheresurfacearea(radi)
        shapedata["volume"] = spherevolume(radi)
        return shapedata
    elif shape.lower() == "trapezoid":
        shapedata["name"] = "trapezoid"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        c = float(input("Enter values for c:\n"))
        d = float(input("Enter values for d:\n"))
        shapedata["perimter"] = trapezoidperimeter(a, b, c, d)
        shapedata["area"] = trapezoidarea(a, b, float(input("Enter values for height:\n")))
        return shapedata
    elif shape.lower() == "cube":
        shapedata["name"] = "cube"
        l = float(input("Enter values of length:\n"))
        shapedata["area"] = cubearea(l)
        shapedata["volume"] = cubevolume(l)
        return shapedata
    elif shape.lower() == "cylinder":
        shapedata["name"] = "cylinder"
        r = float(input("Enter values of radius:\n"))
        h = float(input("Enter values of height:\n"))
        shapedata["area"] = cylinderarea(r, h)
        shapedata["volume"] = cylindervolume(r, h)
        return shapedata
    elif shape.lower() == "rectangular box":
        shapedata["name"] = "rectangular box"
        a = float(input("Enter side a:\n"))
        b = float(input("Enter side b:\n"))
        c = float(input("Enter side c:\n"))
        shapedata["area"] = rectangularboxarea(a, b, c)
        shapedata["volume"] = rectangularboxvolume(a, b, c)
        return shapedata
    else:
        shapedata["error"]="The required shape is "

# return a dictionary from compute and then pass it
def outputvalues(data):
    print(data)


S = getinput()
Data = compute(S)
outputvalues(Data)
