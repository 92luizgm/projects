from random import randrange

def play():
    print('Welcome to the guessing game!')
    secret_number = randrange(1,10)
    
    print('''Choose difficulty level:
    (1) easy
    (2) normal
    (3) hard
    ''')
    level = int(input('Difficulty: '))
    if level == 1:
        guesses = 6
    elif level == 2:
        guesses = 4
    elif level == 3:
        guesses = 3
    else:
        guesses = 1
    
    for tries in range(1, guesses + 1):
        print(f'Try {tries} in {guesses}')
        guess = int(input('Pick a number from 1 to 9'))
        print(f'You guessed {guess}')
        if guess < 1 or guess > 9:
            print('A number from 1 to 9')
            continue
        
        right = secret_number == guess
        higher = secret_number > guess
        lower = secret_number < guess

        if right:
            print('Congratilations! You guessed it right!')
            break
        else:
            if tries == guesses:
                print(f'No luck, the secret number was {secret_number}')
            elif higher:
                print('Try again, the secret number is HIGHER')
            elif lower:             
                print('Try again, the secret number is LOWER')
    print('GAME OVER')

if __name__ == '__main__':
    play()
