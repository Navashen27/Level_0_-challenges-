def common_letters(first_string, second_string):
    print("common letters: ", end="")
    first_string = first_string.lower()
    second_string = second_string.lower()
    remover = "%s"
    output = ""
    
    for letters in first_string:
        for characters in second_string:
                if letters == characters:
                    if letters not in output:
                        output = output + letters
                        print(remover % letters, end = "")
                        remover = ", %s"
                else:
                    continue
        

common_letters("houses","computers")
