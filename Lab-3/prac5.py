class Prac6 :
    def __init__(object, List, target) :
        object.List = List
        object.target = target
        print(object.List)
    def __calc__(object) :
        for item in range(0, len(object.List)) :
            if(object.List[item] + object.List[item + 1] == object.target) :
                return str(item) + ", " + str(item  + 1)
            else :
                continue

list = Prac6([10, 20, 10, 40, 50, 60, 70], 50)
print("Output : " + str(list.__calc__()))
