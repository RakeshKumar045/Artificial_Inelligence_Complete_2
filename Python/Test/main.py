def sum_number(n):
    sum = 0
    while (n > 0):
        res = n % 10
        sum = sum + res
        n = n // 10
    return sum


def sum_total_number(n):
    # print("Number is : ", n)
    result = sum_number(n)
    # if result < 10:
    #     return result
    # else:
    #     return sum_total_number(result)
    return result if result < 10 else sum_total_number(result)


num = 12345999999999999999999999999999999999999999999999999999999999999999999999999999999999999
sum_of_number = sum_total_number(num)
print("Result :", sum_of_number)

l = ["a", "b", "c", "d"]
s = ""
for i in l:
    s = s + i
print(s)


def sum_number_1_method(n):
    sum = 0
    while (n > 0):
        res = n % 10
        sum = sum + res
        n = n // 10
    print("sum = ", sum)
    return sum if sum < 10 else sum_number_1_method(sum)


print("2nd result : ", sum_number_1_method(num))
