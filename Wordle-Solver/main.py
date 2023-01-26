with open('words.txt') as f:
    content=f.read()

allowed_letters=input('Enter allowed (yellow box) letters: ')
valid_letters=input('Enter valid (green box) letters: ')
allowed_list,valid_list=[]=[]
for i in content:
    if allowed_letters