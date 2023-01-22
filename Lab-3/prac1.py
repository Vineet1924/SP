def isPanagram(str) :
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet : 
        if char not in str.lower() :
            return False
    return True

string = str(input("Enter String : "))
if(isPanagram(string)) :
    print(string + " is Panagram")
else :
    print(string + " is not Panagram")