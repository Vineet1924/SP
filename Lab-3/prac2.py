def give_unique(list) :
    unique = []
    for item in list :
        if item not in unique :
            unique.append(item)
    return unique

List = [1,2,3,4,5,5,4,3,2,1]
print("With non-unique : " + str(List))
print("With unique : " + str(give_unique(List)))