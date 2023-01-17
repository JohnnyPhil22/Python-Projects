import tkinter,time,winsound #(any else needed?)

root = tkinter.Tk()
root.title("Timer")

# Create button/input field for duration

# Create countdown method
t=int(input('Enter time to count from (in seconds): '))
def countdown():
    for i in range(t,-1,-1):
        print(i)
        time.sleep(1)
        if t==0:
            winsound.PlaySound('', winsound.SND_ASYNC)

countdown()

# Create GUI
# Put countdown in GUI

root.mainloop()