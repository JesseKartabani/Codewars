def disemvowel(string_):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in vowels:
        string_ = string_.replace(x, "")
    return string_
