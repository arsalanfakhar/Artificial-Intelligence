import math

def squareparameter(side):
    return 4*side
def squarearea(side):
    return side*side

def rectangleparameter(a,b):
    return (2*a)+(2*b)
def rectanglearea(a,b):
    return a*b

def circleparameter(radius):
    return 2*math.pi*radius
def circlearea(radius):
    return math.pi*math.pow(radius,2)

def triangleperimeter(a,b,c):
    return a+b+c
def trianglearea(breadth,height):
    return (1/2)*breadth*height

def paralellogramperimeter(a,b):
    return (2*a) +(2*b)
def paralellogramarea(b,h):
    return b*h

def circularringarea(outerradius,innerradius):
    return  math.pi*(math.pow(outerradius,2)-math.pow(innerradius,2))

def spheresurfacearea(radius):
    return 4*math.pi*math.pow(radius,2)
def spherevolume(radius):
    return (4*math.pi*math.pow(radius,3))/3

def trapezoidperimeter(a,b,c,d):
    return (a+b+c+d)
def trapezoidarea(a,b,height):
    return height*((a+b)/2)

def rectangularboxarea(a,b,c):
    return (2*a*b)+(2*a*c)+(2*b*c)
def rectangularboxvolume(a,b,c):
    return a*b*c

def cubearea(length):
    return 6*math.pow(length,2)
def cubevolume(length):
    return math.pow(length,3)

def cylinderarea(radius,height):
    return 2*math.pi*radius*(radius+height)
def cylindervolume(radius,height):
    return math.pi*radius*radius*height




def getinput():
    shape=input("Enter a shape:\n")
    return shape

#gets the shape name and computes
def compute(shape):
    Shapedata=dict()
    shape=str(shape)
    if shape.lower()=="square":
        Shapedata["name"]="Square"
        side=float(input("Enter side:\n"))
        Shapedata["Perimeter"]=squareparameter(side)
        Shapedata["Area"]=squarearea(side)
        return Shapedata
    elif shape.lower()=="rectangle":
        Shapedata["name"]="rectangle"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        Shapedata["Perimeter"] =rectangleparameter(a,b)
        Shapedata["Area"]=rectanglearea(a,b)
        return Shapedata
    elif shape.lower()=="circle":
        Shapedata["name"] = "circle"
        r = float(input("Enter values of radius:\n"))
        Shapedata["Perimeter"] = circleparameter(r)
        Shapedata["Area"] = circlearea(r)
        return Shapedata
    elif shape.lower()=="triangle":
        Shapedata["name"] = "triangle"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        c = float(input("Enter values for c:\n"))
        Shapedata["Perimeter"] = triangleperimeter(a,b,c)
        breadth = float(input("Enter values for breadth:\n"))
        height = float(input("Enter values for height:\n"))
        Shapedata["Area"] = trianglearea(breadth,height)
        return Shapedata
    elif shape.lower()=="parallelogram":
        Shapedata["name"] = "parallelogram"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        Shapedata["Perimeter"] = paralellogramperimeter(a,b)
        height = float(input("Enter values for height:\n"))
        Shapedata["Area"] = paralellogramarea(b,height)
        return Shapedata
    elif shape.lower()=="circular ring":
        Shapedata["name"] = "circular ring"
        outerradi = float(input("Enter values of outer radius:\n"))
        innerradi = float(input("Enter values of inner radius:\n"))
        Shapedata["Area"] = circularringarea(outerradi,innerradi)
        return Shapedata
    elif shape.lower() == "sphere":
        Shapedata["name"] = "sphere"
        radi = float(input("Enter values of radius:\n"))
        Shapedata["surface area"] = spheresurfacearea(radi)
        Shapedata["volume"] = spherevolume(radi)
        return Shapedata
    elif shape.lower() == "trapezoid":
        Shapedata["name"] = "trapezoid"
        a = float(input("Enter values for a:\n"))
        b = float(input("Enter values for b:\n"))
        c = float(input("Enter values for c:\n"))
        d = float(input("Enter values for d:\n"))
        Shapedata["perimter"] = trapezoidperimeter(a,b,c,d)
        Shapedata["area"] = trapezoidarea(a,b,float(input("Enter values for height:\n")))
        return Shapedata
    elif shape.lower() == "cube":
        Shapedata["name"] = "cube"
        l = float(input("Enter values of length:\n"))
        Shapedata["area"] = cubearea(l)
        Shapedata["volume"] = cubevolume(l)
        return Shapedata
    elif shape.lower() == "cylinder":
        Shapedata["name"] = "cylinder"
        r = float(input("Enter values of radius:\n"))
        h = float(input("Enter values of height:\n"))
        Shapedata["area"] = cylinderarea(r,h)
        Shapedata["volume"] = cylindervolume(r,h)
        return Shapedata
    elif shape.lower()=="rectangular box":
        Shapedata["name"] = "rectangular box"
        a = float(input("Enter side a:\n"))
        b = float(input("Enter side b:\n"))
        c = float(input("Enter side c:\n"))
        Shapedata["area"] = rectangularboxarea(a,b,c)
        Shapedata["volume"] = rectangularboxvolume(a,b,c)
        return Shapedata


#return a dictionary from compute and then pass it
def outputvalues(data):
    print(data)

S=getinput()
Data=compute(S)
outputvalues(Data)
