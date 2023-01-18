from tkinter import *
import random

root=Tk()
root.geometry("350x300")
root.title("Rock Paper Scissors")

computer_value={"0":"Rock","1":"Paper","2":"Scissor"}

def reset_game():
    b1["state"]="active"
    b2["state"]="active"
    b3["state"]="active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

def button_disable():
    b1["state"]="disable"
    b2["state"]="disable"
    b3["state"]="disable"

def player_rock():
    c_v=computer_value[str(random.randint(0, 2))]
    if c_v=="Paper":
        match_result="COMPUTER WINS!"
    elif c_v=="Scissor":
        match_result="PLAYER WINS!"
    elif c_v=="Rock":
        match_result="DRAW"
    l1.config(text="Rock")
    l3.config(text=c_v)
    l4.config(text=match_result)
    button_disable()

def player_paper():
    c_v=computer_value[str(random.randint(0, 2))]
    if c_v=="Rock":
        match_result="PLAYER WINS!"
    elif c_v=="Scissor":
        match_result="COMPUTER WINS!"
    elif c_v=="Paper":
        match_result="DRAW"
    l1.config(text="Paper")
    l3.config(text=c_v)
    l4.config(text=match_result)
    button_disable()

def player_scissor():
    c_v=computer_value[str(random.randint(0, 2))]
    if c_v=="Paper":
        match_result="PLAYER WINS!"
    elif c_v=="Rock":
        match_result="COMPUTER WINS!"
    elif c_v=="Scissor":
        match_result="DRAW"
    l1.config(text="Scissor")
    l3.config(text=c_v)
    l4.config(text=match_result)
    button_disable()

Label(root,text="Rock Paper Scissor",font="normal 20 bold",fg="blue").pack(pady=20)

frame=Frame(root)
frame.pack()

l1=Label(frame,text="Player",font=10)
l1.pack(side=LEFT)

l2=Label(frame,text="VS",font=10)
l2.pack(side=LEFT)

l3=Label(frame, text="Computer", font=10)
l3.pack()

l4=Label(root,text="",font="normal 20 bold",bg="white",width=15,borderwidth=2,relief="solid")
l4.pack(pady=20)

frame1=Frame(root)
frame1.pack()

b1=Button(frame1,text="Rock",font=10,width=7,command=player_rock)
b1.pack(side=LEFT,padx=10)

b2=Button(frame1,text="Paper",font=10,width=7,command=player_paper)
b2.pack(side=LEFT,padx=10)

b3=Button(frame1,text="Scissor",font=10,width=7,command=player_scissor)
b3.pack(padx=10)

Button(root,text="Reset Game",font=10,fg="red",bg="black",command=reset_game).pack(pady=20)

root.mainloop()