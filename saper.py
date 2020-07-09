import re
n, m = [int(x) for x in input().split(' ')]

try:
    if not 1 <= n <= 100:
        raise ValueError("n is not within allowed range")

    if not 1 <= m <= 100:
        raise ValueError("m is not within allowed range")

    my_matrix = []

    # create multidimensional list/array below
    for x in range(n):
        row = input()
        # check whether . or * withing given chars
        not_allowed_chars = re.search(r'[^\.\*]', row)
        if not_allowed_chars is not None:
            raise ValueError("Only '.' and '*' are allowed characters. '{}' given". format(not_allowed_chars.group()))

        # substitute . with 0
        row = [0 if (v == '.') else v for v in list(row)]
        if len(row) != m:
            raise ValueError("Number of elements '{}' in the row '{}' does not equal to the expected 'm' value: {}"
                             .format(len(row), x+1, m))
        # add row to matrix
        my_matrix.append(row)

    for row in range(len(my_matrix)):
        for col in range(len(my_matrix[row])):
            # if col equal * then need to increment counters in all surrounding non-asterisks cells
            if my_matrix[row][col] == '*':
                counter1 = -1
                while counter1 <= 1:
                    counter2 = -1
                    while counter2 <= 1:
                        try:
                            if my_matrix[counter1 + row][counter2 + col] != '*' \
                             and counter1+row >= 0 and counter2 + col >= 0:
                                my_matrix[counter1 + row][counter2 + col] += 1
                        except IndexError as e:
                            pass
                        counter2 += 1
                    counter1 += 1

    for row in my_matrix:
        print(''.join(str(x) for x in row))

except ValueError as e:
    print("Error occurred: {}".format(e))
