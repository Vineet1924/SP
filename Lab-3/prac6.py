class __reverse__ :
    def __init__(object, str) :
        object.str = str
    def __reverse_string__(object) :
        string = object.str[::-1]
        return string

string = str(input("Enter String : "))
object1 = __reverse__(string)
print("Reversed String = " + str(object1.__reverse_string__())) 