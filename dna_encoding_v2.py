str_test = input()


def encode_dna_string(str_test):
    repetitions = 1
    new_str = str_test[0]

    for i in range(1, len(str_test)):
        if str_test[i] == str_test[i-1]:
            repetitions += 1
        else:
            new_str += str(repetitions) + str_test[i]
            repetitions = 1
    return new_str + str(repetitions)


print(encode_dna_string(str_test))
