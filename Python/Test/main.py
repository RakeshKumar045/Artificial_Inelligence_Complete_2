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


def summ(t):
    r = 0;
    for d in str(t):
        r = r + int(d)
    # return r
    if len(str(r)) == 1:
        return (r)
    else:
        return (summ(r))


n = summ(9999)
print(n)


def ft(transaction, threshold):
    l = []
    for i in transaction:
        for j in set(i.split()[:-1]):
            l.append(j)
    val = {i: l.count(i) for i in l}
    res = dict(sorted(val.items(), key=lambda item: item[1], reverse=True))
    count = 0
    for k, v in res.items():
        if (count < threshold):
            print(k, v)
            count += 1


threshold_value = int(input("Enter the threshold value : "))
# threshold_value = 2

# tran_value = list(input("Enter the trnsaction details : "))

tran_value = ["99 88 500", "99 99 99", "88 99 400", "12 12 800", "12 15 600", "99 99 99", "88 99 400", "12 12 800",
              "12 15 600"]
t = ['99 88 500', '99 99 99', '88 99 400', '12 12 800', '12 15 600']

ft(tran_value, threshold_value)
# ft(t, threshold_value)
