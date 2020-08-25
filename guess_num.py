import random
import sys
import os


def game():
    print('Guess the Number Game\n')

    top_range = random.randrange(10, 100, 5)
    secret_num = random.randint(1, top_range)
    
    print(f'I\'m thinking of a number betweeen 1 and {top_range}.')
    print('Enter (quit) to exit at any point.')

    guesses = 0

    # Player can make 6 guesses before game over.
    while guesses < 6:
        if guesses == 0:
            print('Take a guess.')
        elif guesses == 5:
            print('This is your LAST guess. Choose wisely.')
        else:
            print('Take another guess.')

        guess = input('> ')

        # Check if there are letters instead of numbers.
        while True:
            if guess.lower() == 'quit':
                sys.exit()
            elif guess.isalpha():
                print('\nThose are letters, please use numbers (e.g. 1, 2, 3...).\n')
                game()
            else:
                guess = int(guess)
                break
        
        os.system('cls')
        # Check if guess is cold/warm
        if str(guess) in guessed:
            print('You\'ve already guessed that number, try another one.')
        elif (guess > top_range) or (guess <= 0):
            print('That\'s not in the range I have gave you.')
        else:
            # If secret number is +/- 10 away
            if guess < (secret_num - 10):
                print(f'{guess} is too low.')
            elif guess > (secret_num + 10):
                print(f'{guess} is too high.')
            # If secret number is +/- 3 away
            elif guess < (secret_num - 3):
                print(f'Almost! {guess} is lower than my number.')
            elif guess > (secret_num + 3):
                print(f'Almost! {guess} is higher than my number.')
            # If guess is very close to secret number
            elif guess < secret_num:
                print(f'You\'re very close! {guess} is lower than my number.')
            elif guess > secret_num:
                print(f'You\'re very close! {guess} is higher than my number.')
            else:
            # Move on if guessed correctly or out of guesses
                break
            
            # Add to total number of guesses
            guesses += 1
            # Track previous guesses into a list
            guessed.append(str(guess))
        
        # Display total guesses took & previous guesses
        print(f'\nYou\'ve used {guesses}/6 tries.')
        print(f'Numbers Guessed:', ', '.join(guessed))
        print(f'\nI\'m thinking of a number betweeen 1 and {top_range}.')
        print('Enter (quit) to exit at any point.')

    os.system('cls')
    if guess == secret_num:
        if guesses == 0:
            print(f'Are you psychic? You got that on your first try!')
        else:
            print(f'Hooray! It took you {guesses + 1} guesses to figure out my number was {secret_num}.')
            print(f'Numbers Guessed:', ', '.join(guessed))
    else:
        print(f'Sorry, the number I was thinking of was {secret_num}.')
        print(f'Numbers Guessed:', ', '.join(guessed))


def again():
    play = input('\nPlay again? Y or N.\n> ')
    if play.lower() == 'y':
        guessed.clear()
        os.system('cls')
    elif play.lower() == 'n':
        sys.exit()
    else:
        print(f'I don\'t understand "{play}"? Please enter Y or N.')
        again()

guessed = []

while True:
    game()
    again()
