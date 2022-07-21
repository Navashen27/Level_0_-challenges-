def common_letters(first_word, second_word):
    common = []
    for letter in first_word.lower():
        if letter in second_word.lower():
            common.append(letter)

    print(f"Common letters: {', '.join(set(common))}")


if __name__ == "__main__":
    common_letters("House", "Computer")
