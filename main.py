import requests

def difficulty_level():
    while True:
        difficulty_level = int(input('choose the difficulty level.\n1. Easy\n2. Medium\n3. Hard\n>>>'))
        if difficulty_level == 1:
            print('\nYou choose easy mode.\nIn easy mode there will be 3 letters and 5 attempts to guess it.\n')
            return 3
            break
        elif difficulty_level == 2:
            print('\nYou choose medium mode.\nIn medium mode there will be 5 letters and 7 attempts to guess it.\n')
            return 5
            break
        elif difficulty_level == 3:
            print('\nYou choose hard mode.\nIn hard mode there will be 7 letters and 8 attempts to guess it.\n')
            return 7
            break
        else:
            print('\nSomething went wrong.\n')

def get_words_from_api():
    difficulty = difficulty_level() 
    url = f'https://random-word-api.herokuapp.com/word?length={difficulty}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return str(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

word = get_words_from_api()
print(word)

def hangman(guess_word):
    word_length = len(guess_word)
    total_attempts = word_length + 2

    while total_attempts >= 1:
        user_guess = input("Enter your guess : ")

        for j in guess_word:
            if user_guess == j:
                print('right guess')
            else:
                print('wrong guess')
                total_attempts -= 1


# hangman(word)
