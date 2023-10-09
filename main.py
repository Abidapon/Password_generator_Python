#Importing necessary modules
from random import randint
#All Upper case password
password = ""
for i in range(10):
    i = chr(randint(65, 90)).upper()
    password = str(password) + i


#All Lower case password
password = ""
for j in range(5):
    j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)