def commonletter(firstword,secondword):
   words=set(firstword.lower()) & set(secondword.lower())
   print(*{letter for letter in words},sep=(', '))
commonletter("miracles","messages")
