def isVowel_upper(c):
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return c

def isVowel_lower(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return c

def vowels_checker(str):
    vowels = []
    s = ''
    i = 0
    while i < len(str):
        if str[i] == isVowel_upper(str[i]) or str[i] == isVowel_lower(str[i]):
            vowels.append(str[i])
        i = i + 1
    print(s.join(vowels))
