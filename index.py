import random

letter = "abcdefg"
number = "1234"

string = letter + number
length = 20

password = "".join(random.sample(string,length))

print("The Password Is: " + password)