import itertools

def is_valid_word(word, valid_words):
    return word in valid_words

def get_possible_words(letters, valid_words):
    possible_words = set()
    for i in range(3, len(letters) + 1):  # Words of length 3 or more
        for combo in itertools.permutations(letters, i):
            word = "".join(combo)
            if word in valid_words:
                possible_words.add(word)
    return possible_words

def wordscapes_game():
    print("Welcome to Wordscapes!")
    letters = "tree"
    valid_words = {"tree", "tee", "ere", "ret"}  # Replace with a larger word set if needed
    found_words = set()
    possible_words = get_possible_words(letters, valid_words)
    
    print(f"Your letters: {', '.join(letters)}")
    print("Find as many words as you can! (Type 'exit' to quit)")
    
    while found_words != possible_words:
        user_input = input("Enter a word: ").strip().lower()
        
        if user_input == "exit":
            print("Game over! Here were the possible words:", possible_words)
            break
        
        if user_input in found_words:
            print("You already found that word!")
        elif is_valid_word(user_input, valid_words):
            found_words.add(user_input)
            print(f"Good job! {len(possible_words) - len(found_words)} words left.")
        else:
            print("Invalid word. Try again!")
    
    if found_words == possible_words:
        print("Congratulations! You found all words!")

if __name__ == "__main__":
    wordscapes_game()
