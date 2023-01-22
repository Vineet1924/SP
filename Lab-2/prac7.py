def word_count(str) :
    count = dict()
    list = str.split()
    for i in list :
        if i in count :
            count[i] += 1
        else :
            count[i] = 1
    return count
string = str(input("Enter String : "))
print(word_count(string))