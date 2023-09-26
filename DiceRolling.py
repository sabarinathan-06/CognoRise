import random

def roll_dice(num_sides, num_rolls):
    if num_sides < 2 or num_rolls < 1:
        print("Invalid input. Please use at least 2 sides on the dice and roll it at least once.")
        return
    
    print(f"Rolling a {num_sides}-sided dice {num_rolls} times:")
    
    for _ in range(num_rolls):
        result = random.randint(1, num_sides)
        print(f"Roll {_ + 1}: {result}")

if __name__ == "__main__":
    try:
        num_sides = int(input("Enter the number of sides on the dice: "))
        num_rolls = int(input("Enter the number of rolls: "))
        
        roll_dice(num_sides, num_rolls)
    except ValueError:
        print("Invalid input. Please enter valid numbers for sides and rolls.")
