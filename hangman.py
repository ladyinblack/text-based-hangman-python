import random

# Write your code here
words = ['python', 'java', 'kotlin', 'javascript']
guess = random.choice(words)

incorrect_letters = []
correct_letters = []
your_guessed = []
chances_left = 8  # Number of chances left
correctly_guessed = 0  # Letters correctly guessed by player
current_guesses = 0     # All letters guessed by player


# Check correct guesses
def correct_guesses(gs):
    idx = 0
    all_guesses = 0
    for i in guess:
        if gs != i:
            idx += 1
        else:
            your_guessed[idx] = i
            idx += 1
    idx = 0

    for j in your_guessed:
        if j == guess[idx]:
            all_guesses += 1
            idx += 1
        else:
            idx += 1
    return all_guesses


def incorrect_guesses(gs):
    idx = 0
    all_guesses = 0
    for m in guess:
        if gs != m:
            idx += 1
        else:
            incorrect_letters[idx] = m
            idx += 1


# Display guessed word to show player what they have guessed
for k in guess:
    your_guessed.append("-")

# Start the game
print("H A N G M A N")
play_exit = input("Type \"play\" to play the game, \"exit\" to quit:")

while chances_left > 0 and correctly_guessed != len(guess):
    print()
    guess_str = ''.join(your_guessed)
    print(guess_str)
    your_guess = input("Input a letter:")
    if your_guess in correct_letters or your_guess in incorrect_letters:
        print("You've already guessed this letter")
    elif len(your_guess) > 1:
        print("You should input a single letter")
    elif not your_guess.islower() and len(your_guess) == 1:
        print("Please enter a lowercase English letter")
    elif your_guess in guess:
        correct_letters.append(your_guess)
        correctly_guessed = correct_guesses(your_guess)
        guess_str = ''.join(your_guessed)
    elif your_guess not in guess and your_guess not in incorrect_letters:
        incorrect_letters.append(your_guess)
        print("That letter doesn't appear in the word")
        chances_left -= 1

if correctly_guessed == len(guess):
    print()
    print(guess_str)
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")
