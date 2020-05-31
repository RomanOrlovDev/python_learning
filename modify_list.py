"""
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4] """

t = [3, 5]
t[:] = [1, 5]
# m[0] = 12
print(t)
# print(m)
exit()


def modify_list(l):
    i = 0
    while i < len(l):
        x = l[i]
        if x % 2 == 0:
            l[i] = x // 2
            i += 1
        else:
            del l[i]

    # below doesn't work since delete shifts index in the list
    # for i, x in enumerate(l):
    #     if x % 2 == 0:
    #         l[i] = x // 2
    #     else:
    #         del l[i]
    # [l[i] = x //2 if x % 2 == 0 else del l[i] for i,x in enumerate(l)]


l = [8, 9, 12]
modify_list(l)
print(l)

modify_list(l)
print(l)

modify_list(l)
print(l)


# another solution
# useful to know the following:
# >>> a = [0]
# >>> b = a
# >>> a[:] = [1]
# >>> print(b)
# [1]                 <--- note, change reflected by a and b
# >>> a = [2]
# >>> print(b)
# [1]                 <--- but now a points at something else, so no change to b

def modify_list_2(l):
    l[:] = [(i // 2) for i in l if i % 2 == 0]


l = [8, 9, 12]
modify_list_2(l)
print(l)

modify_list_2(l)
print(l)

modify_list_2(l)
print(l)
