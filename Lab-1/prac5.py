no1 = int(input("Enter no 1 : "))
no2 = int(input("Enter no 2 : "))
no3 = int(input("Enter no 3 : "))

if(no1 > no2 and no1 > no3) :
    print("Largest is " + str(no1))
elif(no2 > no1 and no2 > no3) :
    print("Largest is " + str(no2))
else :
    print("Largest is " + str(no3)) 

