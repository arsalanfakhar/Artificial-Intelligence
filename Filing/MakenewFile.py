#Create
#it will throw error if it will not exists


try:
    f = open("C:\\Users\\Arsalan\\Desktop\\qorkingquery.txt", "x")

except:
    print("error")
    f = open("C:\\Users\\Arsalan\\Desktop\\qorkingquery.txt", "r")
    print(f.read())