import random

# Function to take a file, default is 'animals.txt'.
def take_file(my_file:str='animals.txt'):
    with open (my_file) as mf:
        animals = []
        for animal in mf: # Filtering.
            if ' ' not in animal and 'list' not in animal:
                animals.append(animal.rstrip())
    my_animal = random.choice(animals).lower()
    for letter in my_animal: # Covering letters.
        print('_', end=' ')
    print() # cały ten sektor można usunąć oprócz randoma
    
    guessed_letters = ''
    tries = len(my_animal) + 2 # Creating a number of chances.
    while tries > 0:
        # Validation.
        choice = input('\nGuess a letter: ').lower()
        
        if not choice.isalpha():
            print('Enter only LETTER...')
            continue
        elif len(choice) != 1:
            print('Enter only SINGLE LETTER')
            continue
        elif choice in guessed_letters:
            print('This letter is guessed yet')
            tries -= 1
            print(f'You have only {tries} chances!')
            continue

        if choice in my_animal:
            guessed_letters += choice
        else:
            print(f"Letter {choice} is NOT in the word!")
            tries -= 1 # Reducing the chances if letter is wrong.
            print(f'You have only {tries} chances!')
        
        wrong_letter = 0
        for letter in my_animal:
            if letter in guessed_letters:
                print(f'{letter}', end= ' ')
            else:
                print('_', end=' ')
                wrong_letter += 1
        
        if wrong_letter == 0:
            print('\nYou won')
            break
    else:
        print('\nYou lost')
        print(f"Your's world was '{my_animal.upper()}'")
        
if __name__ == '__main__':
    take_file()