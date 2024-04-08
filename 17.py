def get_third_character(word):
    if len(word) >= 3:
        third_character = word[2]
        return third_character
    else:
        return "Слово слишком короткое"


word = "Привет"
third_character = get_third_character(word)
print("Третий символ в слове '{}' - {}".format(word, third_character))   

    

