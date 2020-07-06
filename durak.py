values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = {'C', 'D', 'H', 'S'}

first_value, first_suit, second_value, second_suit = sum([(lambda x: [x[:len(x)-1], x[-1]])(x) for x in input().split()], [])
trump = input()

try:
    if trump not in suits:
        raise Exception("not correct suit")

    if first_suit == second_suit:
        # compare values
        first_index = values.index(first_value)
        second_index = values.index(second_value)
        if first_index == second_index:
            out = 'Error'
        else:
            out = 'First' if first_index > second_index else 'Second'
    elif first_suit == trump:
        # this wins
        out = 'First'
    elif second_suit == trump:
        out = 'Second'
    else:
        out = 'Error'

    # print("first index: {}, second index: {}".format(first_index, second_index))
    print(out)
except Exception as e:
    print("Error occurred: ", e)
