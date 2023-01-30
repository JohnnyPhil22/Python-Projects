import tkinter, random
from tkinter import messagebox

dark_grey,yellow,green,light_grey,white,black='#777b7d','#c9b458','#6aaa64','#d3d6da','#ffffff','#000000'

class Button:
    def change_colour(self,colour):
        if colour == light_grey:
            self.button.configure(bg=colour,fg=black)  
        else:
            self.button.configure(bg=colour,fg=white)  

    def get_letter(self,row:int,column:int):
        return [x for x in self.form.letters if x.row == row and x.column == column][0]
		
    def get_word(self,row:int):
        letters = [x.square["text"] for x in self.form.letters if x.row == row and x.column <= 5]
        return "".join(letters)

    def colour_current_row(self,target:str,word:str,row:int):
        new_word = ""
        new_target = ""
        for position in range(0,5):
            if word[position] == target[position]:
                new_word += "*"
                new_target += "*"
            else:
                new_word += word[position]
                new_target += target[position]
        newest_target = ""
        for position in range(0,5):
            letter = new_target[position]
            if letter != "*":
                for this_postion, guess_letter in enumerate(new_word):
                    if guess_letter == letter:
                        new_word = new_word[:this_postion] + "?" + new_word[this_postion+1:]
                        break
        for position in range(0,5):
            letter = new_word[position]            
            this_letter = self.get_letter(row,position + 1)
            if letter == "*":                        
                this_letter.change_colour(green)
            elif letter == "?":
                this_letter.change_colour(yellow)
            else:
                this_letter.change_colour(dark_grey)
        if new_word.count("*") == 5:
            tkinter.messagebox.showinfo("Congratulations!","Congratulations on guessing the word correctly!")
        else:
            if row >= 6:
                tkinter.messagebox.showinfo("End of game","Out of guesses! The word to be guessed was " + self.form.target_word.upper() + ".")
				
    def colour_letter_buttons(self,guesses,buttons):
        guessed_letters = "".join(guesses).upper()
        guessed_letters = list(set(guessed_letters))
        for button in buttons:
            if button.letter not in guessed_letters:
                continue
            if button.letter not in self.form.target_word.upper():
                button.change_colour(dark_grey)
                continue
            correct_position = self.form.target_word.find(button.letter)
            for guess in guesses:
                if guess[correct_position].upper() == button.letter.upper():
                    button.change_colour(green)
                    continue
                else:
                    button.change_colour(yellow)
                    break
    
    def ok_clicked(self):
        if self.letter.lower() == "back":
            if self.form.current_column > 1:
                last_letter = self.get_letter(self.form.current_row,self.form.current_column - 1)
                last_letter.square["text"] = ""
                last_letter.change_colour(white)
                self.form.current_column -= 1
            return
        if self.letter.lower() == "enter":
            if self.form.current_column > 5:
                this_word = self.get_word(self.form.current_row).lower()
                if this_word not in self.form.words:
                    tkinter.messagebox.showerror("Not a valid word",this_word.upper()+" isn't a valid word")
                    return
                self.colour_current_row(self.form.target_word.upper(),this_word.upper(),self.form.current_row)
                self.form.current_column = 1
                self.form.current_row += 1
                self.form.guesses.append(this_word)
                self.colour_letter_buttons(self.form.guesses,self.form.letter_buttons)
            return
        if self.form.current_column > 5:
            return
        if self.form.current_row > 6:
            return
        current_letter = self.get_letter(self.form.current_row,self.form.current_column)
        current_letter.square["text"] = self.letter
        current_letter.change_colour(light_grey)
        self.form.current_column += 1

    def __init__(self,form,*,left:int,top:int,width:int,letter:str):
        self.id = "button_" + letter.lower()
        self.form = form
        self.letter = letter
        self.button = tkinter.Button(form,text=letter,command=self.ok_clicked,width=width,height=2,relief="flat")
        self.change_colour(black)
        self.button
        self.button["padx"] = 5
        self.button["pady"] = 5
        self.button.place(x=left, y=top+370)

class Letter:
    def change_colour(self,colour):
        if colour == light_grey:
            self.square.configure(bg=colour,fg=black)  
        else:
            self.square.configure(bg=colour,fg=white)
    
    def __init__(self,form,*,left:int,top:int,row:int,col:int):
        self.row = row
        self.column = col
        self._letter = None
        self.square = tkinter.Label(form,font=("Arial", 10, "bold"),text="",width=8,height=4,borderwidth=1,relief="ridge",anchor="center")
        self.change_colour(white)
        self.square
        self.square.place(x=left, y=top)

def create_main_window():
    wordle_form = tkinter.Tk()
    wordle_form.title("Wordle")
    wordle_form.tk_setPalette(black)
    form_width = 600
    form_height = 700
    screen_width = wordle_form.winfo_screenwidth()
    screen_height = wordle_form.winfo_screenheight()
    horizontal_offset = int((screen_width/2) - (form_width/2))
    vertical_offset = int((screen_height/2) - (form_height/2))
    wordle_form.geometry('{0}x{1}+{2}+{3}'.format(form_width,form_height,horizontal_offset,vertical_offset))
    wordle_form.resizable(False,False)
    return wordle_form

def add_letter_buttons(wordle_form):
    letter_buttons = []
    first_row = "QWERTYUIOP"
    second_row = "ASDFGHJKL"
    third_row = "ZXCVBNM"
    start_top = 130
    start_left = 45
    for letter in first_row:
        letter_buttons.append(Button(wordle_form,left=start_left,top=start_top,width=4,letter=letter))
        start_left += 50
    start_left = 70
    for letter in second_row:
        letter_buttons.append(Button(wordle_form,left=start_left,top=start_top + 55,width=4,letter=letter))
        start_left += 50
    letter_buttons.append(Button(wordle_form,left=50,top=start_top + 110,width=7,letter="ENTER"))
    start_left = 120
    for letter in third_row:
        letter_buttons.append(Button(wordle_form,left=start_left,top=start_top + 110,width=4,letter=letter))
        start_left += 50
    letter_buttons.append(Button(wordle_form,left=470,top=start_top + 110,width=7,letter="BACK"))
    return letter_buttons

def add_letters(wordle_form):
    letters = []
    for r in range(1,7):
        for c in range(1,6):
            letters.append(Letter(wordle_form,left=45 + c * 70,top= -30 + r * 70,row=r,col=c))
    return letters

def get_target_word(path:str):
    words = []
    with open(path + "\wordle_targets.txt") as target_words:
        words = target_words.read().splitlines()[1:]
    number_words = len(words)
    word_number = random.randint(0, number_words-1)
    _number, this_word = words[word_number].split(",")
    return this_word

def get_allowed_word_guesses(path:str):
    with open(path + "\words.txt") as target_words:
        words = target_words.read().splitlines()
    return words

def play_game(if_debug:bool,this_target=None):
    wordle_form = create_main_window()
    wordle_form.letter_buttons = add_letter_buttons(wordle_form)
    wordle_form.letters = add_letters(wordle_form)
    wordle_form.current_row = 1
    wordle_form.current_column = 1
    if this_target == None:
        wordle_form.target_word = get_target_word('Python-Projects\Wordle')
    else:
        wordle_form.target_word = this_target
    if if_debug:
        print(wordle_form.target_word)
    wordle_form.words = get_allowed_word_guesses('Python-Projects\Wordle')
    wordle_form.guesses = []
    wordle_form.mainloop() 
                
play_game(if_debug=False,this_target=None)