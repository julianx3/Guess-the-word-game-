import random

class WordGuessingGame:
    def __init__(self):
        self.words = ["apple", "banana", "orange", "grape", "kiwi", "peach", "watermelon", "strawberry", "blueberry", "pineapple"]
        self.randomWord = random.choice(self.words)
        self.maxAttempts = 6
        self.guessedWord = "_" * len(self.randomWord)
        self.guessedLetters = []

    def displayWord(self):
        return " ".join(self.guessedWord)

    def checkGuess(self, userGuess):
        if len(userGuess) == 1 and userGuess.isalpha():
            if userGuess in self.guessedLetters:
                return "You've already guessed that letter. Try a different one!"
            elif userGuess in self.randomWord:
                self.guessedLetters.append(userGuess)
                indices = []
                for i in range(len(self.randomWord)):
                    if userGuess == self.randomWord[i]:
                        indices.append(i)
                for index in indices:
                    self.guessedWord = self.guessedWord[:index] + userGuess + self.guessedWord[index + 1:]
                if "_" not in self.guessedWord:
                    return f"Congratulations! You guessed the word: {self.randomWord}"
                return "Great! You guessed a letter!"
            else:
                self.guessedLetters.append(userGuess)
                return "Letter was not in the word. Guess again."
        elif userGuess == self.randomWord:
            return f"Congratulations! You guessed the word: {self.randomWord}"
        else:
            return "Please enter a valid letter or the whole word."

    def playGame(self):
        print("Try to guess the correct word! The theme is fruits")

        for _ in range(self.maxAttempts):
            print("\nWord you are trying to guess:", self.displayWord())
            userGuess = input("Guess a letter or try to get the whole word: ").lower()
            result = self.checkGuess(userGuess)
            print(result)

            if "Congratulations! You guessed the word right:" in result:
                return
        else:
            print(f"You are out of attempts! The correct word was: {self.randomWord}")


def main():
    game = WordGuessingGame()
    game.playGame()

if __name__ == '__main__':
    main()
