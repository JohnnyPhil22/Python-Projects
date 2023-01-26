import random

with open('words.txt') as f:
    content=f.read()
    global word_to_guess
    word_to_guess=random.choice(content)

