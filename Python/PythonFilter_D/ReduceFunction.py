from functools import reduce

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
# def laregValue():

f_max = lambda a, b: a if (a > b) else b
maximum = reduce(f_max, [47, 11, 42, 102, 13])
print("maximum value : ", maximum)

f_min = lambda a, b: a if (a < b) else b
minimum = reduce(f_min, [47, 11, 42, 102, 13])
print("minimum value : ", minimum)

print("*" * 10)

# Without Reduce Fucntion
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print("product : ", product)


# Reduce Function
def testReduce(list_val):
    product = (reduce(lambda x, y: x * y, list_val))
    return product


print("*" * 100)
print("Product With Reduce : ", testReduce(list))
print("*" * 200)
