def mid(string):
    if (len(string) % 2 == 0):
        return ""
    return string[len(string)//2]

print(mid("abc"))