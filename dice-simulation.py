import random

# Generate and return the dice number
# null -> int
def roll_dice():
    return random.randint(1, 6)

def main():
    dice = roll_dice()
    print(f'Dice number: {dice}')

if __name__ == '__main__':
        main()