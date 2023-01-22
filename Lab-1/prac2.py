a = int(input("Enter Lower Bound : "))
b = int(input("Enter Upper Bound : "))

for i in range(a, int(b) + 1) :
    if i == 1 :
        continue
    for j in range(2, i) :
        if (i % j == 0) :
            break
    else :
        print(i)

