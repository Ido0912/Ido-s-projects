def show_hidden_word(secret_word, old_letters_guessed):
    now_word = list(secret_word)
    k = 0
    flag = True
    for j in secret_word:
        flag = True
        for i in old_letters_guessed:
            if j == i:
                flag = False
        if flag:
            now_word[k] = f"_"
        k += 1
    return ''.join(now_word)


def if_right(secret_word, letter):
    now_word = list(secret_word)
    flag = True
    for j in secret_word:
        if j == letter:
           return  True
    return False


def check_win(secret_word, old_letters_guessed):
    flag = True
    for i in secret_word:
        flag = True
        for j in old_letters_guessed:
            if j == i:
                flag = False
        if flag:
            return False
    return True


def check_valid_input(letter_guessed, old_letters_guessed):
    for i in old_letters_guessed:
        if letter_guessed == i:
            return False
    if 'a' <= letter_guessed <= 'z' or 'A' <= letter_guessed <= 'Z':
        return True
    return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        for i in old_letters_guessed:
            print(i+" ", end="")
        print()
        return False
3

old_letters_gussed = []
index = int(input("enter index: "))
index = index * 2-2
word = ""
with open('word.txt', 'r') as reader:
    for line in reader:
        for i in range(index, len(line)):
            if i % 2 != 0:
                word = word + line[i]
word.lower()
begin = "x-------x"
mazavim = ("|\n|\n|\n|\n|", "|       |\n|       0\n|\n|\n|", "|       |\n|       0\n|       | \n|\n|",
           "|       |\n|       0\n|      /|\ \n|\n|", "|       |\n|       0\n|      /|\ \n|      /\n|",
           "|       |\n|       0\n|      /|\ \n|      / \ \n|")
k = 0
print("lets start: ")
print()
print("x-------x")
while k != 6:
    print(show_hidden_word(word, old_letters_gussed))
    print()
    letter = input("Guess a letter: ")
    letter.lower()
    if if_right(word, letter):
        if try_update_letter_guessed(letter, old_letters_gussed):
            print("good!")
        else:
            print(begin)
            print(mazavim[k])
            print()
            k += 1
    else:
        print(":(")
        try_update_letter_guessed(letter, old_letters_gussed)
        print(begin)
        print(mazavim[k])
        print()
        k += 1
    show_hidden_word(word, old_letters_gussed)

    if check_win(word, old_letters_gussed):
        print(word)
        print("well done! you win")
        break
if k == 6:
    print("you lose!")
