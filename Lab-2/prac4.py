number = int(input("Enter number of operation : "))

print("1 for search | 2 for delete")

countyDic = {
    "India" : "Delhi",
    "England" : "London",
    "Nepal" : "Katmandu",
    "Itly" : "Rome",
    "Australia" : "Canbbera",
    "Newzealand" : "Wellington",
}

for i in range(1,number + 1) :    
    choice = int(input("Enter Choice : "))
    if(choice == 1) :
        key = str(input("Search : "))
        capital = countyDic.get(key)
        print("Capital = " + str(capital))
    if(choice == 2) :
        key = str(input("Delete : "))
        capital = countyDic.pop(key)
        print(str(capital) + " is Deleted")
        print(countyDic)