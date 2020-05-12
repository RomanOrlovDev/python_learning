f = open("test.txt", "w+")
modes = ["r", "w", "a", "r+", "w+"]  # a means add content, r+ - read/write, w+ - creates file
modes_binary_strings = ["br", "bw", "ba", "br"]
f.write("some content\n")
f.write("some another content")
f.close()

f = open("test.txt", "r+")
f.tell()  # read from the end of the file
f.seek(0)  # set file pointer to a specific position
f.readline()
f.readlines()
