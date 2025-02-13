# Matthew Carden
# Assignment P1
# GUI Development Spring 2025

from tkinter import *
from tkinter import ttk


def show_french(word):
    lblFrench.config(text=word)
    lblFrench.pack()

# Create main window
root = Tk()
root.title("French Numbers")
root.geometry("600x400")
root.resizable(False, False)

# Instructions labels
lblTitle = Label(root, text="Do you know the French words for the numbers 1 through 5?", font=("Arial", 12))
lblTitle.pack(pady=10)

lblInstructions = Label(root, text="Click the buttons below to see them.", font=("Arial", 12))
lblInstructions.pack(pady=5)

# Number buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

buttons = [
    ("1", "Un"),
    ("2", "Deux"),
    ("3", "Trois"),
    ("4", "Quatre"),
    ("5", "Cinq")
]

for idx, (text, word) in enumerate(buttons):
    btn = Button(button_frame, text=text, command=lambda w=word: show_french(w), width=5)
    btn.grid(row=0, column=idx, padx=20, pady=5)

# Center the button frame
button_frame.pack(anchor=CENTER)

# French word label
lblFrench = Label(root, text="", font=("Arial", 16, "bold"), fg="blue", bg="lightyellow")
lblFrench.pack(pady=20)

# Exit button
btnExit = Button(root, text="Exit", command=root.destroy)
btnExit.pack(pady=20)

root.mainloop()
