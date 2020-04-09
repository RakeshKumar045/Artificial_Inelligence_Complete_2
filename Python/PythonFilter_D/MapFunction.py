# map(function_to_apply, list_of_inputs) Example and description

def sqrt(x):
    return x ** 2


def cube(x):
    return x ** 3


list_val = [1, 2, 3, 4, 5]


# Without Map
def testSquare(item):
    new_list = []
    for val in item:
        new_list.append(sqrt(val))
    print("Item : ", item, "Sqaure root Item : ", new_list)
    return new_list


testSquare(list_val)


# With Map function
def testSquareWithMap(item):
    new_list = list(map(sqrt, item))
    print("Item : ", item, "Sqaure root Item : ", new_list)
    return new_list


print("#" * 100)
testSquareWithMap(list_val)
print("#" * 100)

# With Lambda
val_map = list(map((lambda x: x ** 2), list_val))
print("Item with lambda : ", list_val, "Sqaure root Item : ", val_map)
print("#" * 100)


# I can write many no of function with same function , it will work
def sqrt(x):
    return x ** 2


def sqrt(x):
    return x ** 2


def sqrt(x):
    return x ** 2


func = [sqrt, cube]


def testSquareCube(item, function):
    val = map(function, item)
    return val


val_sqaure_cube = testSquareCube(list_val, func)
print("Item : ", list_val, "    Square and cube   : ", val_sqaure_cube)
print("#" * 100)


# With Lambda
def testSquareCubeLambda(function):
    for x in range(5):
        val = list(map(lambda fun: fun(x), function))
        return val


val_sqaure_cube_lambda = testSquareCubeLambda(func)
print("Item : ", list_val, "    Square and cube with Lambda   : ", val_sqaure_cube_lambda)
print("#" * 100)


def square(x):
    return (x ** 2)


def cube(x):
    return (x ** 3)


funcs = [square, cube]
for r in range(5):
    value = list(map(lambda x: x(r), funcs))
    print(" value :", value)

# 2) types of problem
m = [1, 2, 3]
n = [1, 4, 9]
print("#" * 100)
new_tuple = map(None, m, n)
print("Tuple : ", new_tuple)


def multiply(x):
    return (x * x)


def add(x):
    return (x + x)


print("#" * 100)
add_mult_funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), add_mult_funcs))
    print(" value is : ", value)
