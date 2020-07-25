abc = ' abcdefghijklmnopqrstuvwxyz'
shift = int(input())
out = ''
for s in input().strip():
    out += abc[((shift + abc.find(s)) % 27)]
print("Result: \"{}\"".format(out))