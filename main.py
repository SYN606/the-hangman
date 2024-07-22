import requests


def get_words_from_api():
    url = 'https://random-word-api.herokuapp.com/word?length=5'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return str(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

word = get_words_from_api()


def hangman(guess_word):
    word_length = len(guess_word)
    total_attempts = word_length

    while total_attempts >= 1:
        user_guess = input("Enter your guess : ")

        for j in guess_word:
            if user_guess == j:
                print('right guess')
            else:
                print('wrong guess')
                total_attempts -= 1


hangman(word)
