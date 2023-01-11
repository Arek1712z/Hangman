import random
import tkinter as tk

'''Creating main game window.'''
root = tk.Tk()
root.geometry('480x480')
root.title('Hangman')

'''Creating' random word to guess.'''
with open ('animals.txt') as mf:
    animals = []
    for animal in mf: # Filtering.
        if ' ' not in animal and 'list' not in animal:
            animals.append(animal.rstrip())
my_animal = random.choice(animals).lower()
word = tk.Label(root, text=['_' for letter in my_animal], bg='black', fg='white')
word.configure(font=("Times New Roman", 20, "italic"))
word.pack()

guessed_letters = '' # String of guessed letters, on start is empty.
tries = len(my_animal) + 2 # Creating number of tries in game.

'''Main game script.'''
def letter():
    global tries
    global guessed_letters
    
    if tries > 0:
        
        choice = my_box.get() # Changing info from Entry box to string.
        
        if not choice.isalpha():
            answer.config(text='Enter only LETTER...')
            
        elif len(choice) != 1:
            answer.config(text="Enter only SINGLE LETTER")
            
        elif choice in guessed_letters:
            answer.config(text="This letter is guessed yet")
            
        elif choice in my_animal:
            answer.config(text=f"Good, '{choice}' is in the word!")
            guessed_letters += choice # Adding guessed letter to string of guessed letters above.
        
        else:
            answer.config(text=f"Letter '{choice}' is NOT in the word!")
            tries -= 1 # Reducing the chances if letter is wrong.
            warning.config(text=f'You have only {tries} chances')
            if tries == 0:
                my_label.config(text='You lost', fg='red')
                lost_label.config(text=f"Your's world was '{my_animal.upper()}'", fg='red')
            
        ''''On-screen interface upgrade.'''
        wrong_letter = 0 
        word.config(text=[letter if letter in guessed_letters else '_' for letter in my_animal])
        for letter in my_animal: # Verification of how many letters are left to be guessed.
            if letter not in guessed_letters:
                wrong_letter += 1
        print(wrong_letter) # do usunięcia
        
        if wrong_letter == 0:
            tries = -1
    
    if tries == -1:
        my_label.config(text='You won', fg='green')
    
    

my_label = tk.Label(root, text='Guess a letter') # Creating task label.
my_label.pack()
my_box = tk.Entry(root, borderwidth=5) # Creating Entry box.
my_box.pack()

my_button = tk.Button(root, text='Enter a letter', command=letter) # Creating button which activates the function.
my_button.pack()

answer = tk.Label(root, text='') # Creating response label which is updated in the function.
answer.pack()

warning = tk.Label(root, text='') # Creating label which chances info, updated in the function.
warning.pack()

lost_label = tk.Label(root, text='') # Creating label witch world to guess if you lost
lost_label.pack()

'''Main loop of game.'''
root.mainloop()