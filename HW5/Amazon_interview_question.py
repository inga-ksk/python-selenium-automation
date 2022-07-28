def find_unique_letter():
    word = "google"
    list_1 = list(word)
    unique_letters = []
    for i in list_1:
        if list_1.count(i) == 1:
            unique_letters.append(i)
    print(unique_letters[0])

find_unique_letter()
