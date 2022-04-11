def common_letters(str1, str2):
    common = []
    s = ", "

    for i in str1:
        for j in str2:
            if j == i:
                if i in common:
                    continue
                else:
                    common.append(i)
    print(s.join(common))
