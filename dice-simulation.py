import random
import tkinter

# Generate and return the dice number
# null -> int
def roll_dice():
    return random.randint(1, 6)

# Roll the dice again and show on the window
# tkinter object, String -> void
def roll_again(window, label):
    # Clear the widgets
    for widget in window.winfo_children():
        widget.destroy()

    # Recreate the widgets
    dice = roll_dice()
    make_text(window, f'Dice number: {dice}', 14)
    make_img(window, dice, 54)
    make_button(window, label)

# Return the dice unicode
# int -> String
def dice_face(number):
    faces = {
        1: u'\u2680',
        2: u'\u2681',
        3: u'\u2682',
        4: u'\u2683',
        5: u'\u2684',
        6: u'\u2685'
    }
    return faces[number]

# Make the window text
# tkinter object, String, int -> void
def make_text(window, msg, font_size):
    t = tkinter.Label(window, 
                        justify=tkinter.CENTER, 
                        pady=20,
                        text=msg, 
                        font=(None, font_size)).pack()

# Make the button to roll the dice again
def make_button(window, label):
    b = tkinter.Button(window, text=label, 
                        command=lambda: roll_again(window, label))
    b.pack()

# Insert the dice "image"
# tkinter object, Int -> void
def make_img(window, dice, size):
    make_text(window, dice_face(dice), 54)

# Create and configure the window
# String, Int, String, String -> tkinter object
def create_window(title, dice_num, msg, btn_label):
    window = tkinter.Tk()
    window.geometry('300x300')
    window.title(title)
    make_text(window, msg, 14)
    make_img(window, dice_num, 54)
    make_button(window, btn_label)
    return window

def main():
    # Window variables
    title = 'Dice Simulation'
    btn_label = 'Roll dice'
    dice_num = roll_dice()
    msg = f'Dice number: {dice_num}'

    main_window = create_window(title, dice_num, msg, btn_label)
    main_window.mainloop()

if __name__ == '__main__':
        main()