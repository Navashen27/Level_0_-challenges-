def common_letter(firstword,secondword):
       words=set(firstword.lower()) & set(secondword.lower())
       print(*{letter for letter in words},sep=(', '))
common_letter("miracles","messages")
