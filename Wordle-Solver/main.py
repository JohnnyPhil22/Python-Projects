words=[]
with open('Python-Projects\Wordle-Solver\words.txt') as f:
    for line in f:
        words.append(line.strip())

def play_wordle(words : list) -> None:
    while len(words) > 1:
        letters_in_word = []
        for i in range(5):
            letter = input("Letter in position " + str(i+1) +": ").lower()
            color = input("What color is it (Green, Yellow, Grey): ").lower()
            if color != 'green' and color != 'yellow' and color != 'grey':
                print("Invalid input...")
                return
            words_to_remove = []
            for word in words:
                if color == 'green':
                    if word[i] != letter:
                        words_to_remove.append(word)
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
                elif color == 'yellow':
                    if letter not in word:
                        words_to_remove.append(word)
                    elif word[i] == letter:
                        words_to_remove.append(word)
                    if letter not in letters_in_word:
                        letters_in_word.append(letter)
                elif color == 'grey':
                    if letter in word:
                        if letter not in letters_in_word:
                            words_to_remove.append(word)
                        elif words[i] == letter:
                            words_to_remove.append(word)
            for word in words_to_remove:
                words.remove(word)
        print(words)
        guess = input("Did you guess correctly (Y/N)?: ").lower()
        if guess == 'y':
            print("Congratulations! You win!")
            return
play_wordle(words)