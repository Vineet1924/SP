string = str(input("Enter String : "))
list = string.split(" ")
print(list)
list[2] = "cute"
new_string = ""
for i in list :
    new_string += i + " "
print(new_string)
