import random as rd
import tkinter as tk
from tkinter import messagebox

def show_symbols(i, j):
    global first_card
    global previous_X
    global previous_Y
    buttons[i, j]['text'] = str(button_symbols[i, j])
    buttons[i, j].update_idletasks()

    if first_card:
        previous_X = i
        previous_Y = j
        first_card = False
    elif previous_X != i or previous_Y != j:
        if buttons[previous_X, previous_Y]['text'] != buttons[i, j]['text']:
            buttons[previous_X, previous_Y].after(500, lambda: hide_symbols(previous_X, previous_Y, i, j))
        else:
            buttons[previous_X, previous_Y]['state'] = 'disabled'
            buttons[i, j]['state'] = 'disabled'
            check_game_completion()
        first_card = True

def hide_symbols(x1, y1, x2, y2):
    buttons[x1, y1]['text'] = ' '
    buttons[x2, y2]['text'] = ' '

def check_game_completion():
    for i in range(6):
        for j in range(4):
            if buttons[i, j]['state'] != 'disabled':
                return
    messagebox.showinfo("Congratulations!", "You've completed the game!")

window = tk.Tk()
window.background = "red"
window.title("Matchmaker")
window.resizable(width=False, height=False)
window.iconbitmap('C:/Users/Sri Vaishnavi/OneDrive/Desktop/matchmaker/th.ico')
first_card = True
previous_X = 0
previous_Y = 0
buttons = {}
button_symbols = {}

number_list = list(range(1, 13)) * 2  # Use numbers from 1 to 12 twice
rd.shuffle(number_list)

for i in range(6):
    for j in range(4):
        button = tk.Button(master=window, command=lambda i=i, j=j: show_symbols(i, j), width=4, height=2, bg='#ffffff',
                           fg='black', font=('Lucida', '25'))
        button.grid(column=i, row=j)
        buttons[i, j] = button
        button_symbols[i, j] = number_list.pop()

window.mainloop()
