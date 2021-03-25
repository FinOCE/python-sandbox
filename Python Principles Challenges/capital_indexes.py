def capital_indexes(string):
    return [i for i, letter in enumerate(string) if letter.isupper()]

print(capital_indexes("AbCdEfG"))