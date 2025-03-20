
import os
import random

'''
there should be an interface
'''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_grid(grid):
    clear_screen()
    print("\nWordscapes - Terminal Edition\n")
    for row in grid:
        print(" ".join(row))
    print("\n")

def shuffle_letters(letters):
    return "".join(random.sample(letters, len(letters)))

def generate_grid():
    return [
        ["-", "-", "-", "x", "-"],
        ["-", "-", "-", "x", "-"],
        ["-", "x", "x", "x", "x"],
        ["-", "x", "-", "-", "-"],
        ["-", "x", "-", "-", "-"],
        ["x", "x", "x", "x", "-"],
        ["x", "-", "-", "-", "-"],
        ["x", "-", "-", "-", "-"],
        ["x", "-", "-", "-", "-"]
    ]

# shpuld make a generate grid that fetches grids, then returns the grid,
# instead of it being constant, it should be reusable
# and grid should be imported from another file

def update_grid(grid, word):
    positions = {
        "TEAM": [(2, 1), (2, 2), (2, 3), (2, 4)],
        "MEAT": [(5, 0), (5, 1), (5, 2), (5, 3)],
        "MATE": [(5, 0), (6, 0), (7, 0), (8, 0)],
        "TEA": [(0, 3), (1, 3), (2, 3)],
        "TAME": [(2, 1), (3, 1), (4, 1), (5, 1)]
    }
    
    if word in positions:
        for idx, (row, col) in enumerate(positions[word]):
            grid[row][col] = word[idx]
        return True
    return False

def is_valid_guess(guess, level_letters):
    return all(guess.count(letter) <= level_letters.count(letter) for letter in guess)

# Same goes with this function UpdateGrid
# It should allow to get positions
# which are dictionaries

def wordscapes():
    level_letters = "TEAM"
    valid_words = {"TEAM", "MEAT", "MATE", "TEA", "TAME"}
    found_words = set()
    grid = generate_grid()
    
    while found_words != valid_words:
        display_grid(grid)
        print(f"Available letters: {level_letters}")
        print("Commands: [shuffle] to shuffle letters, [exit] to quit\n")
        
        guess = input("Enter a word: ").upper()
        
        if guess == "SHUFFLE":
            level_letters = shuffle_letters(level_letters)
            continue
        elif guess == "EXIT":
            break
        elif guess in valid_words:
            if guess in found_words:
                print("Word already found!")
            elif is_valid_guess(guess, level_letters):
                found_words.add(guess)
                update_grid(grid, guess)
                print("Correct!")
            else:
                print("Invalid word. Check your letters!")
        else:
            print("Word not in list.")
        
        input("Press Enter to continue...")
        '''
        should be timed
        '''
    
    display_grid(grid)
    print("Congratulations! You completed the level.")

if __name__ == "__main__":
    wordscapes()
