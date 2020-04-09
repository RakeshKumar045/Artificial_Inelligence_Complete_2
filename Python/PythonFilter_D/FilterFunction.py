def sqrt(x):
    return x ** 2


list_val = [1, 2, 3, 4, 5]
new_val = range(-5, 5)


# With filter function (Filter is fail), it is example of Map Function
def testSquareWithFilter(item):
    new_list = list(filter(sqrt, item))
    print("Item : ", item, "Sqaure root Item : ", new_list)
    return new_list


print("#" * 100)
testSquareWithFilter(list_val)
print("#" * 100)


def testFilter(val):
    value = list(filter(lambda x: x < 0, val))
    return value


print("Value is : ", new_val, "Check negative value : ", testFilter(new_val))
print("*" * 100)
