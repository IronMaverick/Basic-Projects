from random import randint as random
from functools import reduce
import tkinter as tk
from functools import reduce
import tkinter.messagebox
from os import system


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guesses = 6
game_ongoing = True  # Variable to track if the game is ongoing
game_won = False

def file():
    file = open("words.txt", 'r')
    list_of_words = file.read().split()
    return list_of_words

def secret_word(list_of_words):
    index_of_word = random(0, len(list_of_words)-1)
    secret_word = list_of_words[index_of_word]
    return secret_word

def list_of_(secret_word):
    # Create a list of empty dashes based on the length of the secret word
    return ['_'] * len(secret_word)

def main(secret_word, list_of_list):
    global alpha, guesses
    def list_of_secret_word(secret_word):
        return list(secret_word)

    def change_alpha(user):
        global alpha
        if user not in alpha:
            print("you have used that alphabet")
        else:
            alpha.pop(alpha.index(user))

    def screen(list_of_list):
        print(reduce(lambda m, n: m+n, list_of_list))

    def user_input(lst_of_):
        print("Number of Guesses are: ", guesses)
        print(reduce(lambda m, n: m + n, lst_of_))
        print("The number of alphabet remaining are:", end=" ")
        print(reduce(lambda m, n: m+','+n, alpha))
        user = input("Enter the alphabet: ").lower()
        if len(user) == 1:
            return user
        else:
            print("Enter only one character: ")
            user_input(list_of_list)
    def condition_1(user, secret_word):
        if user in secret_word:
            return True
        else:
            return False
    def count(user, secret_word):
        count_of_user = secret_word.count(user)
        return count_of_user

    def output(user, list_of_li, lis, count):
        if count == 1:
            index = lis.index(user)
            lis.pop(index)
            list_of_li.pop(index*2)
            list_of_li.insert(index*2, user)
            return list_of_li
        elif count == 2:
            index = lis.index(user)
            lis.pop(index)
            list_of_li.pop(index*2)
            list_of_li.insert(index*2, user)
            indexed = lis.index(user)
            lis.pop(indexed)
            list_of_li.pop((indexed+1)*2)
            list_of_li.insert((indexed+1)*2, user)
            return list_of_li

    user = user_input(list_of_list)
    list_of_secret_word = list_of_secret_word(secret_word)
    condition = condition_1(user, secret_word)
    if condition:
        count_of_user = count(user, secret_word)
        list_of = output(user, list_of_list, list_of_secret_word, count_of_user)
        change_alpha(user)
        ff = reduce(lambda m, n: m+n, reduce(lambda m, n: m + n, list_of).split())
        if ff == secret_word:
            screen(list_of)
            print("Well done")
        else:
            main(secret_word, list_of_list)
    else:
        print("Your word is not in my Word")
        guesses -= 1
        if guesses == 0:
            print("You ran out of guesses")
        else:
            change_alpha(user)
            main(secret_word, list_of_list)

# Initialize the Hangman game
list_of_words = file()
secret_word = secret_word(list_of_words)
list_of_list = list_of_(secret_word)
guesses = 6

# Create the main game window
root = tk.Tk()
root.title("Hangman Game")

# Adjust the window size
root.geometry("400x200")

# Create GUI elements
word_label = tk.Label(root, text="Word: ")
word_label.pack()

word_display = tk.Label(root, text="", font=("Helvetica", 20))
word_display.pack()

input_label = tk.Label(root, text="Enter a letter: ")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

output_label = tk.Label(root, text="", font=("Helvetica", 14))
output_label.pack()

def update_gui(list_of_list):
    word_display.config(text=' '.join(list_of_list))  # Join dashes with spaces
    output_label.config(text="Number of Guesses: " + str(guesses))
    
    # Check for a win condition
    if '_' not in list_of_list:
        output_label.config(text="Well done! You won!")

# Function to handle user input
def guess_letter(event=None):
    global game_ongoing, game_won, guesses
    if not game_ongoing or game_won:
        return  # If the game is not ongoing or already won, do nothing
    user = input_entry.get().lower()
    input_entry.delete(0, tk.END)
    if len(user) == 1:
        if user.isalpha():
            if guesses > 0:
                if user in secret_word:
                    count_of_user = secret_word.count(user)
                    for i, char in enumerate(secret_word):
                        if char == user:
                            list_of_list[i] = user
                    if reduce(lambda m, n: m + n, list_of_list) == secret_word:
                        #Update the word with the displayed word
                        game_won = True
                        word_display.config(text=secret_word)
                        tkinter.messagebox.showinfo("Congratulations", "You have won!")
                        input_entry.config(state=tk.DISABLED)  # Disable the input field
                        guess_button.config(state=tk.DISABLED)  # Disable the "Guess" button
                    else:
                        update_gui(list_of_list)
                else:
                    guesses -= 1
                    if guesses == 0:
                        word_display.config(text=secret_word)
                        output_label.config(text="Game Over! You ran out of guesses.")
                        game_ongoing = False  # Set game_ongoing to False when the game is lost
                        input_entry.config(state=tk.DISABLED)  # Disable the input field
                        guess_button.config(state=tk.DISABLED)  # Disable the "Guess" button
                    else:
                        output_label.config(text=f"Your word is not in my Word\nNumber of Guesses: {guesses}")
                    return
            else:
                output_label.config(text="Your word is not in my Word\nNumber of Guesses: " + str(guesses))
        else:
            output_label.config(text="Select only alphabet")
            guesses -= 1
            if guesses == 0:
                word_display.config(text=secret_word)
                output_label.config(text="Game Over! You ran out of guesses.")
                game_ongoing = False
                input_entry.config(state=tk.DISABLED)  # Disable the input field
                guess_button.config(state=tk.DISABLED)  # Disable the "Guess" button
            return
    else:
        output_label.config(text="Enter only one character")

# Create a "Guess" button
guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

####Create a "New Game" button
##new_game_button = tk.Button(root, text="New Game") #command=start_new_game)
##new_game_button.pack()

# Allow "Enter" key as selection for "Guess" button
root.bind('<Return>', guess_letter)

# Initialize the GUI with the initial game state
update_gui(list_of_list)

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

# Start the GUI main loop
root.mainloop()










