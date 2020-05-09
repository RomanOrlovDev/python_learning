matrix = [
    [9, 5, 3],
    [0, 7, -1],
    [-5, 2, 9],
    'end'
]

# output = [
#     [3, 21, 22],
#     [10, 6, 19],
#     [20, 16, -1]
# ]

output = []

for key_top_level, i in enumerate(matrix):
    if i == 'end':
        break
    buf = []
    for key_inner_level, j in enumerate(i):
        left_sibling = i[-1] \
            if key_inner_level == 0 \
            else i[key_inner_level - 1]
        right_sibling = i[0] \
            if key_inner_level == len(i) - 1 \
            else i[key_inner_level + 1]
        bottom_sibling = matrix[0][key_inner_level] \
            if key_top_level == len(matrix) - 2 \
            else matrix[key_top_level+1][key_inner_level]
        upper_sibling = matrix[-2][key_inner_level] \
            if key_top_level == 0 \
            else matrix[key_top_level - 1][key_inner_level]
        # print(left_sibling, right_sibling, bottom_sibling, upper_sibling)
        buf.append(left_sibling + right_sibling + bottom_sibling + upper_sibling)

    output.append(buf)

print(output)
