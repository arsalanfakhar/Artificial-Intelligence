import math
Cars = {
    "brand": ["Ford", "Ford", "Ford", "Ford"],
    "model": ["Mustang", "EcoSport", "Endeavour", "Figo"],
    "Displacement": [4951, 1498, 2198, 1194],
    "Mass": [3800, 4230, 3500, 3859],
    "Inclined_Angle": [30, 40, 50, 20],
    "Time": [1, 3, 2, 5]
}
gravity = 9.8
initialvelocity = 0


# Calculate Velocity
def velocity(displacement, time):
    return displacement / time


# Calculate Acceleration
def acceleration(final_velocity, initialvelocity, time):
    return (final_velocity - initialvelocity) / time


# Calculate Force
def force(mass, acceleration):
    return mass * acceleration


# Calculate Kinetic Energy
def kinetic_energy(mass, velocity):
    return (1 / 2) * math.pow((mass * velocity), 2)


# Calculate Power
def power(surface):
    # if use else statement
    # Ask for user input according to surface
    print("Power")


# Calculate Power at plane surface
def plane_power(velocity, force):
    return force * velocity


# Calculate Power an Inclined plane surface
def inclined_power(velocity, force, weight, angle):
    return (force * velocity) + (weight * math.sin(angle) * velocity)


# Calculate Power an Inclined plane surface
def weight(mass, gravity):
    return mass * gravity


# Gets the input data from Dictionary
def getinput(data):
    return (data["Displacement"], data["Mass"], data["Inclined_Angle"], data["Time"])


def compute(displacement,mass,angle,time):
    Velocity=list()
    Acceleration=list()
    Force=list()
    KE=list()
    PP=list()
    IP=list()
    for x in range(len(displacement)):
        Velocity.append(velocity(displacement[x],time[x]))
        Acceleration.append(acceleration(Velocity[x],initialvelocity,time[x]))
        Force.append(force(mass[x],Acceleration[x]))
        KE.append(kinetic_energy(mass[x],Velocity[x]))
        PP.append(plane_power(Velocity[x],Force[x]))
        IP.append(inclined_power(Velocity[x],Force[x],weight(mass[x],gravity),angle[x]))
    return (Velocity,Acceleration,Force,KE,PP,IP)

def outputvalues(velocity,acceleration,force,ke,planepower,inlcinedpower,cardictionary):
    cardictionary["Velocity"]=velocity
    cardictionary["Acceleration"]=acceleration
    cardictionary["Force"]=force
    cardictionary["Kinetic Energy"]=ke
    cardictionary["Plane power"]=planepower
    cardictionary["Inclined Power"]=inlcinedpower
    print(cardictionary)


D, M, A, T = getinput(Cars)
V,A,F,KE,PP,IP=compute(D,M,A,T)
outputvalues(V,A,F,KE,PP,IP,Cars)
