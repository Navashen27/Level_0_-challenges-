vowels = ["a", "e", "i", "o", "u"]
word = "pizza"
empty_string = ""
for letter in word:
    if letter not in vowels:
        empty_string += letter

print(empty_string)
