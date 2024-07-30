import requests

print("Welcome to Hangman!")


def difficulty_level():
    while True:
        difficulty_level = int(
            input("Choose the difficulty level.\n1. Easy\n2. Medium\n3. Hard\n>>>")
        )
        if difficulty_level == 1:
            print(
                "\nYou choose easy mode.\nIn easy mode there will be 3 letters and 5 attempts to guess it.\n"
            )
            return 3

        elif difficulty_level == 2:
            print(
                "\nYou choose medium mode.\nIn medium mode there will be 5 letters and 7 attempts to guess it.\n"
            )
            return 5

        elif difficulty_level == 3:
            print(
                "\nYou choose hard mode.\nIn hard mode there will be 7 letters and 8 attempts to guess it.\n"
            )
            return 7

        else:
            print("\nSomething went wrong.\n")


difficulty = difficulty_level()


def get_words_from_api():
    url = f"https://random-word-api.herokuapp.com/word?length={difficulty}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return str(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")


word = str(get_words_from_api())


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman(word, difficulty_level):
    guessed_letters = set()
    attempts = difficulty_level + 2  # Number of allowed incorrect guesses
    guessed_word = display_word(word, guessed_letters)

    print("Try to guess the word.")
    print(guessed_word)

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        guessed_word = display_word(word, guessed_letters)
        print(guessed_word)

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word.")
    else:
        print(f"Game over! The word was '{word}'.")


hangman(word, difficulty)
