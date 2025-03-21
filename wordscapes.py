import os
import random
from game_levels import level_letters, valid_words, grid, positions

class GameGrid:
    def __init__(self, grid, positions):
        self.grid = grid
        self.positions = positions
    
    def update_grid(self, word):
        if word in self.positions:
            for idx, (row, col) in enumerate(self.positions[word]):
                self.grid[row][col] = word[idx]
            return True
        return False

    def refresh_display(self):
        return os.system('cls' if os.name == 'nt' else 'clear')
    
    def display(self):
        self.refresh_display()
        print("\nWordscapes\n")
        for row in self.grid:
            print(" ".join(row))
        print("\n")



class WordscapesGame:
    def __init__(self, level_letters, valid_words, grid, positions):
        self.level_letters = level_letters
        self.valid_words = valid_words
        self.found_words = set()
        self.grid = GameGrid(grid, positions)
    

    def shuffle_letters(self):
        pass
    
    def is_valid_guess(self, guess):
        return all(guess.count(letter) <= self.level_letters.count(letter) for letter in guess)
    
    def play(self):
        while self.found_words != self.valid_words:
            self.grid.display()
            print(f"Available letters: {self.level_letters}")
            print("Commands: [shuffle] to shuffle letters, [exit] to quit\n")
            
            guess = input("Enter a word: ").upper()
            
            if guess == "SHUFFLE":
                self.shuffle_letters()
                continue

            elif guess == "EXIT":
                # than k u for playing
                break

            elif guess in self.valid_words:
                if guess in self.found_words:
                    print("Word already found!")

                elif self.is_valid_guess(guess):
                    self.found_words.add(guess)
                    self.grid.update_grid(guess)
                    print("Correct!")
    
                else:
                    print("Invalid word.")
            else:
                print("Word not in list.")
            
            input("Press Enter to continue...")
        
        self.grid.display()
        print("Congratulations! You guessed all the words.")

if __name__ == "__main__":
    game = WordscapesGame(level_letters, valid_words, grid, positions)
    game.play()
