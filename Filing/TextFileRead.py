f=open("C:\\Users\\Arsalan\\Desktop\\qorkingquery.txt")

# print(f.read())

# print(f.read(3))

print(f.readline())
f.close()

#append data by -a which will overwrite


f=open("C:\\Users\\Arsalan\\Desktop\\qorkingquery.txt","a")

f.write("\n")
f.writelines("My testable text")

f.close()

#append data by -w which will overwrite