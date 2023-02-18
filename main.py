# the user sets the beginning and end, print in one line the sequence in which elements multiple of 5 and 2

a = int(input("Enter the beginning of the sequence: "))
b = int(input("Enter the end of the sequence: "))


def mult_5(a, b):
    list1 = []
    for i in range(a, b + 1):
        if i % 5 == 0:
            list1.append(i)
    return list1


def mult_2(a, b):
    list1 = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            list1.append(i)
    return list1


print(mult_5(a, b))
print(mult_2(a, b))
