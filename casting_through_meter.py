units_dict = dict()
units_dict['mile'] = 1609
units_dict['yard'] = 0.9144
units_dict['foot'] = 0.3048
units_dict['inch'] = 0.0254
units_dict['m'] = 1
units_dict['cm'] = 0.01
units_dict['mm'] = 0.001
units_dict['km'] = 1000

str_to_parse = input()
num, from_, _, to = str_to_parse.split(' ')


try:
    v = units_dict[from_]/units_dict[to] * float(num)
except AttributeError as e:
    print('Attr error: ', e)
except IndexError as e:
    print('Index error: ', e)
except KeyError as e:
    print("Key err: ", e)
else:
    print("{:.2e}".format(v))
