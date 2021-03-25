def only_ints(value1, value2):
    return type(value1) == int and type(value2) == int

print(only_ints(1, 2))