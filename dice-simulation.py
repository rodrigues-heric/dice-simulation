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
    make_text(window, 5, 52, f'Dice number: {roll_dice()}')
    make_button(window, label)

# Make the window text
# tkinter object, int, int, String -> void
def make_text(window, altura, largura, msg):
    t = tkinter.Text(window, height=altura, width=largura)
    t.pack()
    t.insert(tkinter.END, msg)
    t.config(state='disabled')

# Make the button to roll the dice again
def make_button(window, label):
    b = tkinter.Button(window, text=label, 
                        command=lambda: roll_again(window, label))
    b.pack()

# Create and configure the window
# String, String, String -> tkinter object
def create_window(title, msg, btn_label):
    window = tkinter.Tk()
    window.title(title)
    make_text(window, 5, 52, msg)
    make_button(window, btn_label)
    return window

def main():
    # Window variables
    title = 'Dice Simulation'
    msg = f'Dice number: {roll_dice()}'
    btn_label = 'Roll dice'

    main_window = create_window(title, msg, btn_label)
    main_window.mainloop()

if __name__ == '__main__':
        main()