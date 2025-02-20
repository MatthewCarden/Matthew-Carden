from tkinter import *
from tkinter import ttk

# Initialize Tkinter Window
root = Tk()
root.title("Burger Specials")
root.geometry("800x590")

# State Variables
prime_text = StringVar()
veggie_text = StringVar()
confirmation_text = StringVar()
prime_text.set("(Prime Beef)")
veggie_text.set("(Veggie)")
confirmation_text.set("")

# Function to simulate burger selection
def show_burger(burger_type):
    if burger_type == "Prime":
        prime_text.set("Prime Beef Selected")
        veggie_text.set("")
        btn_veggie.config(state=DISABLED)
    else:
        veggie_text.set("Veggie Selected")
        prime_text.set("")
        btn_prime.config(state=DISABLED)

    btn_select.config(state=NORMAL)

# Function to confirm meal selection
def select_meal():
    confirmation_text.set("Enjoy your burger special!")
    btn_select.config(state=DISABLED)
    btn_prime.config(state=DISABLED)
    btn_veggie.config(state=DISABLED)
    btn_exit.config(state=NORMAL)

# Function to exit the application
def exit_app():
    root.destroy()

# Heading Label
lbl_heading = Label(root, text="Farm Burger Specials", font=("Tahoma", 16, "bold"))
lbl_heading.grid(row=0, column=0, columnspan=3, pady=10)

# Image Frames (Now just placeholders)
image_frame = Frame(root)
image_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Prime Burger Placeholder Label
prime_label = Label(image_frame, textvariable=prime_text, width=30, height=10, relief="solid")
prime_label.grid(row=0, column=0, padx=20)

# Veggie Burger Placeholder Label
veggie_label = Label(image_frame, textvariable=veggie_text, width=30, height=10, relief="solid")
veggie_label.grid(row=0, column=1, padx=20)

# Buttons
btn_prime = ttk.Button(root, text="Prime Beef", command=lambda: show_burger("Prime"), width=15)
btn_prime.grid(row=2, column=0, padx=10, pady=10)

btn_select = ttk.Button(root, text="Select Meal", command=select_meal, state=DISABLED, width=15)
btn_select.grid(row=2, column=1, padx=10, pady=10)

btn_veggie = ttk.Button(root, text="Veggie", command=lambda: show_burger("Veggie"), width=15)
btn_veggie.grid(row=2, column=2, padx=10, pady=10)

# Instruction Label
lbl_instructions = Label(root, text="Choose a burger and then click the Select Meal button", font=("Tahoma", 9))
lbl_instructions.grid(row=3, column=0, columnspan=3, pady=5)

# Confirmation Message Label
lbl_confirmation = Label(root, textvariable=confirmation_text, font=("Tahoma", 9))
lbl_confirmation.grid(row=4, column=0, columnspan=3, pady=5)

# Exit Button
btn_exit = ttk.Button(root, text="Exit Window", command=exit_app, state=DISABLED, width=15)
btn_exit.grid(row=5, column=0, columnspan=3, pady=10)

# Start the application
root.mainloop()
