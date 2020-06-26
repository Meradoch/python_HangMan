from random import randint

print('Welcome to Hangman!')
print('You have 6 guesses.')
print('Make sure Caps Lock is on!\n\n')


with open('sowpods.txt') as scrabble_dict:
    no_of_entries = 0
    words = scrabble_dict.readlines()
    for line in words:
        no_of_entries += 1
    random_word = words[randint(0, no_of_entries)].strip()
    
random_word_list = [letter for letter in random_word]
print('_ ' * len(random_word_list))
guess_word_list = ['_' for i in range(len(random_word_list))]

guess_count = 0

while '_' in guess_word_list and guess_count != 6:
    print('you have {} guesses left.\n'.format(6 - guess_count))
    
    guess = input('Guess a letter: ')
    if guess in random_word_list:
        if guess in guess_word_list:
            print('You already guessed that one.\n')
        else:
            for i in range(len(random_word_list)):
                if random_word_list[i] == guess:
                    guess_word_list[i] = guess
            print(' '.join(guess_word_list))
    else:
        print('Incorrect!\n')
        
    guess_count += 1
    
if random_word_list == guess_word_list:
    print('\nCongrats! You took {} guesses.'.format(guess_count))
else:
    print('\nYou are out of guesses. The word was {}.'.format(random_word))
