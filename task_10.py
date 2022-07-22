def compare(string_1, string_2):
    empty = 'Common letters: '
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    for char in string_1:
        if char in string_2:
            empty += f'{char}, '
    print(empty[:-2])

compare('hOuse', 'ComputEr')