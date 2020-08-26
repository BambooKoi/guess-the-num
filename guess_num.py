# Guess the Number Game
# Or
# Reverse Guess the Number Game
# Your choice
# https://github.com/BambooKoi/guess-the-num

import os
import random
import sys


def game_choice():
    while True:
        print('What version of Guess the Number would you like to play?')
        print('Enter (quit) to exit.')
        choice = input('(N)ormal or (R)everse?\n> ')
        choice = choice.lower()
        if choice == 'quit':
            sys.exit()
        elif choice == 'n':
            os.system('cls')
            while True:
                guess()
                again()
        elif choice == 'r':
            os.system('cls')
            while True:
                reverse()
                again()
        else:
            print('Please choose N for normal or R for Reverse.\n')


def guess():
    print('Guess the Number Game')
    print('A game where you try to guess the number that the computer picked.')

    top_range = random.randrange(10, 100, 5)
    secret_num = random.randint(1, top_range)

    print(f'\nI\'m thinking of a number betweeen 1 and {top_range}.')
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
                guess()
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


def reverse():
    print('Reverse Guess the Number')
    print('A game where the computer tries to guess your number instead.')

    print('\nPick a number between 1 and 50. I will only guess whole numbers.')
    input(f'Hit (Enter Key) when you are ready.')
    os.system('cls')

    max_range = 50
    min_range = 1
    guesses = 0

    # Computer has 6 tries to guess.
    while guesses < 6:
        c_guess = random.randint(min_range, max_range)
        # If the min_range and max_range doesn't make sense:
        if (max_range - min_range) == 1:
            print('Hey! I think you cheated.')
            print(f'Your responses were: {responses}')
            print(f'A whole number between {min_range} and {max_range} is impossible.')
            break
        elif max_range == min_range:
            print(f'Well, the only answer left is {min_range}.')
            print(f'Your responses were: {responses}')s
            break
        else:
            pass
        # Prevent the computer from choosing the same number:
        while c_guess in guessed:
            c_guess = random.randint(min_range, max_range)
        else:
            pass
        print('Enter (quit) to exit at any point.')
        answer = input(f'Is the number {c_guess}? (Y)es or (N)o.\n> ')
        answer = answer.lower()
        if answer == 'quit':
            sys.exit()
        elif answer == 'y':
            if guesses == 0:
                print('Whoo! I got it on the first guess.')
            elif guesses <= 3:
                print(f'Yay! It only took me {guesses + 1} tries to figure it out.')
            else:
                print(f'It took me {guesses + 1} tries.')
            break
        elif answer == 'n':
            answer = input('Was my guess (H)igher or (L)ower than your number?\n> ')
            if answer.startswith('l'):
                min_range = c_guess
                responses.append(f'{c_guess} is lower.')
            elif answer.startswith('h'):
                max_range = c_guess
                responses.append(f'{c_guess} is higher')
            else:
                print(f'I did not understand "{answer}"')
            guessed.append(c_guess)
            guesses += 1
            os.system('cls')
        else:
            print(f'I did not understand "{answer}"')

        # if computer couldn't guess it in 6 attempts:
        if guesses == 6:
            print('I could not guess it in 6 tries. I give up.')
            break


def again():
    print('\nPlay again?')
    play = input('(Y)es, (N)o or (P)lay a different version.\n> ')
    if play.lower() == 'y':
        guessed.clear()
        responses.clear()
        os.system('cls')
    elif play.lower() == 'quit' or play.lower() == 'n':
        sys.exit()
    elif play.lower() == 'p':
        game_choice()
    else:
        print(f'I don\'t understand "{play}"? Please enter Y, N, or P.')
        again()


guessed = []
responses = []

game_choice()
