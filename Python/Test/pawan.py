def func(filepath):
    with open(filepath) as f:
        str = ""
        count = 0
        data = f.read()
        print(data)
        d = data.replace(",", " ")
        print(d)
        l = d.split()
        print(l)
        for i in l:
            str = str + i
        for j in str:
            count += 1
    return count
    # f.close()


print(func("abc.txt"))
