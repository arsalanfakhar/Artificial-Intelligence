import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# print(dataframe.columns)


# print(dataframe['Make'][i])
initialvelocity = 0


# calculate displacement
def caldisplacement(finalvelocity, acceleration):
    return (math.pow(finalvelocity, 2) - math.pow(initialvelocity, 2)) / (2 * acceleration)


#
# Calculate Force
def force(mass, acceleration):
    return mass * acceleration


#
# Calculate Kinetic Energy
def kinetic_energy(mass, velocity):
    return (1 / 2) * math.pow((mass * velocity), 2)


#
# Gets the input data from dataframe by pandas
def getinput(dataframe):
    dataDic = dict()
    makeList = list()
    modelList = list()
    massList = list()
    accelerationList = list()
    velocityList = list()

    print("Reading Excel Data Started ...")
    for i in range(20):
        makeList.append(dataframe['Make'][i])
        modelList.append(dataframe['Model'][i])
        massList.append(dataframe['Full weight [kg]'][i])
        accelerationList.append(dataframe['Acceleration (0-100 km/h) [second]'][i])
        velocityList.append(dataframe['Max speed [km/h]'][i])
    print("Reading Excel Data Finished ...")
    dataDic["make"] = makeList
    dataDic["model"] = modelList
    dataDic["mass"] = massList
    dataDic["acceleration"] = accelerationList
    dataDic["velocity"] = velocityList

    return (dataDic["make"], dataDic["model"], dataDic["mass"], dataDic["acceleration"], dataDic["velocity"])


#
def compute(mass, acceleration, velocity):
    Displacement = list()
    Force = list()
    KE = list()

    for x in range(len(mass)):
        Displacement.append(caldisplacement(velocity[x], acceleration[x]))
        Force.append(force(mass[x], acceleration[x]))
        KE.append(kinetic_energy(mass[x], velocity[x]))

    return (Displacement, Force, KE)


def outputvalues(make, model, mass, acceleration, velocity, displacement, force, ke):
    cardictionary = dict()
    cardictionary["Make"] = make
    cardictionary["Model"] = model
    cardictionary["Mass"] = mass
    cardictionary["Acceleration"] = acceleration
    cardictionary["Velocity"] = velocity
    cardictionary["Displacement"] = displacement
    cardictionary["Force"] = force
    cardictionary["Kinetic Energy"] = ke
    print("Writing Excel Data Started ...")
    df = pd.DataFrame(cardictionary)
    writer = ExcelWriter('cars_solution.xlsx')
    df.to_excel(writer, 'Sheet1')
    writer.save()
    print("Writing Excel Data Finished ... Solution could be found at cars_solution.xlsv")

dataframe = pd.read_excel('cars.xlsx')

MK, MD, M, A, V = getinput(dataframe)

D, F, KE = compute(M, A, V)
outputvalues(MK, MD, M, A, V, D, F, KE)