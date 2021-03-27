import random
import tkinter

# Generate and return the dice number
# null -> int
def roll_dice():
    return random.randint(1, 6)

# Make the window text
# tkinter object, int, int -> void
def make_text(window, altura, largura, msg):
    t = tkinter.Text(window, height=altura, width=largura)
    t.pack()
    t.insert(tkinter.END, msg)

# Create and configure the window
# String, String -> tkinter object
def create_window(title, msg):
    window = tkinter.Tk()
    window.title(title)
    make_text(window, 5, 52, msg)
    return window

def main():
    # Window variables
    title = "Dice Simulation"
    msg = f'Dice number: {roll_dice()}'

    main_window = create_window(title, msg)
    main_window.mainloop()

if __name__ == '__main__':
        main()