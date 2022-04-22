def common_letters(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    output = " " + "," . join(set(string1).intersection(string2))
    return output

x = common_letters("Miracles", "messages")
print(f"Common letters: {x}")
