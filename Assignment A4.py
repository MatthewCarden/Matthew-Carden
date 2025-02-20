# Matthew Carden
# Assignment A4
# GUI Development Spring 2025


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Importing PIL for image handling

# Initialize Tkinter Window
root = Tk()
root.title("Burger Specials")
root.geometry("800x590")

# Load Images (Ensure they exist in the same directory)
try:
    prime_img = Image.open("prime.jpg").resize((260, 250))
    veggie_img = Image.open("veggie.jpg").resize((260, 250))

    prime_img_tk = ImageTk.PhotoImage(prime_img)
    veggie_img_tk = ImageTk.PhotoImage(veggie_img)

    blank_img = ImageTk.PhotoImage(Image.new("RGB", (260, 250), (255, 255, 255)))  # Blank image
    print("Images loaded successfully!")  # Debugging check
except FileNotFoundError:
    print("Error: Ensure prime.jpg and veggie.jpg exist in the same folder as this script.")
    exit()

# State Variables
confirmation_text = StringVar()
confirmation_text.set("")

# Function to display burger images
def show_burger(burger_type):
    if burger_type == "Prime":
        prime_label.config(image=prime_img_tk)  # Show Prime Beef image
        veggie_label.config(image=blank_img)  # Hide Veggie image
        btn_veggie.config(state=DISABLED)
    else:
        veggie_label.config(image=veggie_img_tk)  # Show Veggie image
        prime_label.config(image=blank_img)  # Hide Prime image
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

# Image Frames
image_frame = Frame(root)
image_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Prime Burger Image Frame (Starts as blank image)
prime_label = Label(image_frame, width=260, height=250, relief="solid", image=blank_img)
prime_label.grid(row=0, column=0, padx=20)

# Veggie Burger Image Frame (Starts as blank image)
veggie_label = Label(image_frame, width=260, height=250, relief="solid", image=blank_img)
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
()

