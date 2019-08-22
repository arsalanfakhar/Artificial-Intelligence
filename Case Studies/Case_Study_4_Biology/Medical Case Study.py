import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Data = {
#     "symptoms": ["fever", "chills", "headache", "diarrhea", "constipation", "anorexia", "malaise", "cough", "vomiting",
#                  "abdominal pain", "Hepatomegaly", "Gastrointestial bleeding", "Changes in sensorium", "Rashes",
#                  "seizures"],
#     "blood culture": {
#         "sensitivity": [17.3, 49.23],
#         "specificity": [91.1, 100],
#         "ppv": [70.1, 100],
#         "npv": [50.4, 75.1]
#     },
#     "widal test": {
#         "sensitivity": [25.5, 59.26],
#         "specificity": [77.6, 97.0],
#         "ppv": [54.8, 92.9],
#         "npv": [51.3, 77.1]
#     },
#     "typhiod M test": {
#         "sensitivity": [69.4, 94.5],
#         "specificity": [90.1, 100],
#         "ppv": [86.7, 100],
#         "npv": [76.4, 95.9]
#     },
#     "Diazo test": {
#         "sensitivity": [61.6, 90.2],
#         "specificity": [70.6, 93.7],
#         "ppv": [64.4, 92.1],
#         "npv": [68.1, 92.1]
#     }
# }
symptom_dic = {}
standardvalues={}
uservalues={}

# def calcSymptomPercentage(count):
#     return (count / 15) * 100
#
#
# def calcTestPercentage(testcount):
#     return (testcount / 4) * 100


# to get double value of dictinary
# print(Data["blood culture"]["sensitivity"])

def read_symptom_data(df):
    symlist=df['Symptoms']
    newlist=list()
    print(symlist)

    for i in range(1,symlist.__len__()+1):
        newlist.append(symlist[i])

    symptom_dic['Symptoms']=newlist
    print(symptom_dic)

def read_test_values(df):
    senstivitylist=df['SENSITIVITY']
    speicivitylist=df['SPECIFICITY']
    ppvlist=df['PPV']
    npvlist=df['NPV']
    for i in range(1,13):
        print(i)
        i=i+1
        print(i)






def read_excel_values():
    dataframe = pd.read_excel('NormalValues.xlsx')
    # dataframe=dataframe.dropna(axis=0, how='any')
    # print(dataframe['Test Name'])
    # print(dataframe.isnull().sum())
    # dataframe.dropna(axis=0,subset=['Test Name'],how='any')
    # print(dataframe[dataframe['Test Name'].notnull])
    symptomdf=dataframe[dataframe['Symptoms'].notnull()]
    read_symptom_data(symptomdf)
    read_test_values(dataframe)



# def getinput():
#     print("Symptoms for typhoid are given below\nEnter 1 for yes and 0 for no")
#     # Input symptoms
#     count = 0
#     for x in Data["symptoms"]:
#         x = int(input(x))
#         if x == 1:
#             count = count + 1
#
#     user_dic = dict()
#     # Input test results
#     for x in Data:
#         if x == "symptoms":
#             continue
#         #     to skip symptoms one
#         else:
#             print("Enter " + x + " values")
#             user_dic[x] = (input("sensitivity value"), input("specificity"), input("ppv"), input("npv"))
#
#     return (count, user_dic)
#
#
# def compute(symptomCount, user_dic):
#     # print("Count is {}".format(symptomCount))
#     percent = calcSymptomPercentage(symptomCount)
#
#     testResult = dict()
#     # Compute test results
#     for x in Data:
#         if x == "symptoms":
#             continue
#         #     to skip symptoms one
#         else:
#             user_dic_index = 0
#             positive_test_count = 0
#             for y in Data[x]:
#
#                 lowerBound = float(Data[x][y][0])
#                 upperBound = float(Data[x][y][1])
#                 userInput = float(user_dic[x][user_dic_index])
#                 # print(lowerBound)
#                 # print(upperBound)
#
#                 if userInput >= lowerBound and userInput <= upperBound:
#                     positive_test_count = positive_test_count + 1
#                 user_dic_index = user_dic_index + 1
#             print("test count {}".format(positive_test_count))
#             testResult[x] = calcTestPercentage(positive_test_count)
#
#     return (percent, testResult)
#
#
# def output(percent, resultdic):
#     print("The percentage of having typhoid is:" + "{0:.2f}".format(percent))
#     print("The test results are:\n")
#     print(resultdic)
#
#
# C, D = getinput()
# P, R = compute(C, D)
# output(P, R)
read_excel_values()