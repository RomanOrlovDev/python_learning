some_dict = {"this_is_my_dict": [123, 44], "second_prop": "new_val", "third_prop": 383838}

print(some_dict)

print(some_dict.get("second_prop"))
print(some_dict.pop("second_prop"))
print(some_dict)
print(some_dict.get("second_prop"))

some_dict.setdefault("third_prop", "def_val_for_third_prop")  # this will not be set
some_dict.setdefault("fourth_prop", "def_val_for_fourth_prop")
print(some_dict)

some_another_dict = some_dict
some_another_dict["fourth_prop"] = "new_value_4"
print(some_another_dict)
print(some_dict)
