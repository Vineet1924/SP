quantity = int(input("Enter Quantity : "))
totalCost = int(100 * quantity)

if(totalCost >= 1000) :
    discount = (10 * totalCost) / 100
    totalCost -= discount
    
print("Total cost = " + str(totalCost))