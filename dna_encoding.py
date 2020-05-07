str_test = input()


def encode_dna_string(str_test):

    if len(str_test) == 0:
        return 0

    characters_list = [str_test[0]]
    groups_counters = [0]

    for x in str_test:
        if x == characters_list[len(characters_list)-1]:
            groups_counters[len(groups_counters)-1] += 1
        else:
            characters_list.append(x)
            groups_counters.append(1)

    new_string = ''
    for i in range(0, len(characters_list)):
        new_string += characters_list[i] + str(groups_counters[i])

    return new_string


print(encode_dna_string(str_test))