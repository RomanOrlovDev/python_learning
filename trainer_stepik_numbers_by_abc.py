a1 = ' -- '
a2 = '|  |'
a3 = '    '
a4 = '   |'
a5 = '|   '
a_dash = '----'

d = {'0': [a1, a2, a2, a3, a2, a2, a1],
     '1': [a3, a4, a4, a3, a4, a4, a3],
     '2': [a1, a4, a4, a1, a5, a5, a1],
     '3': [a1, a4, a4, a1, a4, a4, a1],
     '4': [a3, a2, a2, a1, a4, a4, a3],
     '5': [a1, a5, a5, a1, a4, a4, a1],
     '6': [a1, a5, a5, a1, a2, a2, a1],
     '7': [a1, a4, a4, a3, a4, a4, a3],
     '8': [a1, a2, a2, a1, a2, a2, a1],
     '9': [a1, a2, a2, a1, a4, a4, a1]}

mm = [d[x][:] for x in input() if x in d]

do_not_print = False
if not len(mm):
    do_not_print = True


for x in mm:
    x.append(a_dash)
    x.insert(0, a_dash)

mm.insert(0, ['x', '|', '|', '|', '|', '|', '|', '|', 'x'])
mm.append(['x', '|', '|', '|', '|', '|', '|', '|', 'x'])

du = zip(*mm)

if not do_not_print:
    for x in zip(*mm):
        if x[0] == 'x':
            # print(*x, sep='')
            for index in range(0, len(x)):
                if index == 0:
                    print(x[index], sep='', end='')
                elif index == (len(x) - 2):
                    print(x[index], sep='', end='')
                elif index == (len(x) - 1):
                    print(x[index])
                else:
                    print(x[index], end='-')
        else:
            for index in range(0, len(x)):
                if index == 0:
                    print(x[index], sep='', end='')
                elif index == (len(x) - 2):
                    print(x[index], sep='', end='')
                elif index == (len(x) - 1):
                    print(x[index])
                else:
                    print(x[index], end=' ')
