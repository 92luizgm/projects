from random import randrange

def play():

    game_opening()

    secret_word = define_secret_word()

    guessed_letters = ['_' for letter in secret_word]
    print(f'The secret word has {len(secret_word)} letters')

    hanged = False
    guessed = False
    errors = 0

    print(guessed_letters)
    while(not hanged and not guessed):
        guess = input('Guess a letter: ')
        guess = guess.strip().upper()

        if guess in secret_word:
            good_guess(secret_word, guessed_letters, guess)
        else:
            errors += 1
            print(f'You still have {6 - errors} tries')
            draw_hangman(errors)
    
        hanged = errors == 6
        guessed = '_' not in guessed_letters
        print(guessed_letters)
    
    final_message(guessed, secret_word)

def game_opening():
    print('Welcome to the hangman game')
    print('***************************')

def define_secret_word():
    file = open('lista2.txt', 'r')
    list = []
    for word in file:
        word = word.strip()
        list.append(word)
    file.close
    i = randrange(0, len(list))
    secret_word = list[i].upper()
    return secret_word

def good_guess(secret_word, guessed_letters, guess):
    index = 0
    for letter in secret_word:
        if guess == letter:
            guessed_letters[index] = letter
        index += 1

def final_message(guessed, secret_word):
    if  guessed:
        print('Congratulations, you have guessed the secret word and got free!')
    else:
        print(f'You got hanged! The secret word was {secret_word}')

def draw_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      /     ")

    if (errors == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      / \   ")

    print("_|___         ")
    print()

if __name__ == '__main__':
    play()