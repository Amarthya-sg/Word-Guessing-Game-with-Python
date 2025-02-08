import random

# Read words from the file and create a word bank
with open("wordbank.txt", "r") as file:
    word_bank = file.read().splitlines()

# Choose a random word from the word bank
word = random.choice(word_bank)
guessed_word = ["_"] * len(word)
for i in range(len(word)):
    if word[i] == " " or word[i] == "-": 
        guessed_word[i] = "/"
    else:
        print("_", end=" ")

# Initialize guessed letters and incorrect guesses
incorrect_guesses = []

attempts = 10

while attempts > 0:
    # Display the current progress of the guessed word
    print('\n Wrong guesses:', ' '.join(incorrect_guesses))
    print('Attempts left:', attempts)
    print('Current word:', ' '.join(guessed_word))
    guess = input('Guess a letter: ').lower()

    # Check if the letter was already guessed
    if guess in incorrect_guesses or guess in guessed_word:
        print(f'You have already guessed "{guess}". Attempts left: {attempts}')
        continue  # Skip the rest of the loop and prompt for another input

    # Check if the guessed letter is in the word
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else:
        # Deduct an attempt for a wrong guess and store incorrect guesses
        attempts -= 1
        incorrect_guesses.append(guess)
        print(f'Wrong guess! Attempts left: {attempts}')

    # Check if the word is fully guessed
    if "_" not in guessed_word:
        print(f'\n🎉 Congratulations!! You guessed the word: {word}')
        break

# If no attempts are left, reveal the correct word
if attempts == 0:
    print(f'\n❌ You\'ve run out of attempts! The word was: {word}')
