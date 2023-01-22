def get_product(list) :
    product = []
    mul = 1
    for item in list :
        mul *= item
    product.append(mul)
    return product

List = [1,2,3,4,5]
print("Product of List : " + str(get_product(List)))