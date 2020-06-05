t = '2a3bB'


def rle_decode(string):
    return decode_series(split_decode_series(string))


def split_decode_series(string):
    n = ''
    for i in string:
        if i.isdigit():
            n += i
            continue
        yield {int(n or 1), i}
        n = ''
        # out.append({int(n or 1), i})


def decode_series(series):
    o = ''
    for s in series:
        s = list(s)
        o += s[0]*s[1]
    return o


print(rle_decode(t))


# number_seq = []
# output = []
# for c in input():
#     if c.isdigit():
#         number_seq.append(c)
#     else:
#         used_number = int((''.join(number_seq))) if len(number_seq) else 1
#         output.append(used_number*c)
#         number_seq = []
# print(''.join(output))


# from forum
# n = ''
# t = '12as3b'
# t = input()
# for c in t:
#     if c.isdigit():
#         n += c
#     else:
#         print(c * int(n or 1), end='')
#         n = ''
