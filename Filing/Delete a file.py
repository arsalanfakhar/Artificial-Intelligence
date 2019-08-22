import os

os.remove("C:\\Users\\Arsalan\\Desktop\\qorkingquery1.txt")

if os.path.exists("C:\\Users\\Arsalan\\Desktop\\qorkingquery1.txt"):
    os.remove("C:\\Users\\Arsalan\\Desktop\\qorkingquery1.txt")
else:
    print("The file does not exist")