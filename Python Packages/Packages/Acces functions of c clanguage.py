from ctypes import *

#first we get to the dll of c language
print(windll.kernel32)
print(cdll.msvcrt)
libraryc=cdll.msvcrt


#then we access the printf function from it
print(libraryc.printf)
print(windll.kernel32.GetModuleHandleA)
# print(windll.kernel32.MyOwnFunction)
print(libraryc.time(None))