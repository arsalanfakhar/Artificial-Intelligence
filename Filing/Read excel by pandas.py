import pandas as pd

train=pd.read_excel("C:\\Users\\Arsalan\\Desktop\\cars.xlsx")

print(train.head())

print(train['id_trim'].describe())

