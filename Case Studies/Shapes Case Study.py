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
    4*math.pi*math.pow(radius,2)
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

def compute(shape):
    Shapedata=dict()
    shape=str(shape)
    if shape.lower()=="square":
        Shapedata["name"]="Square"
        side=int(input("Enter side:\n"))
        Shapedata["Perimeter"]=squareparameter(side)
        Shapedata["Area"]=squarearea(side)
        return Shapedata

def outputvalues(data):
    print(data)

S=getinput()
Data=compute(S)
outputvalues(Data)
#return a dictionary from compute and then pass it