dict_of_words_length = dict()
for x in input().split():
    # if len(x) not in dict_of_words_length:
    #     dict_of_words_length[len(x)] = 0
    dict_of_words_length[len(x)] += 1
    # dict_of_words_length[len(x)] = dict_of_words_length.get(len(x), 0) + 1
{print(str(k) + ':', dict_of_words_length[k]) for k in sorted(dict_of_words_length)}

sl = [len(cl) for cl in input().split()]
for n in sorted(set(sl)):
    print(f"{n}: {sl.count(n)}")
