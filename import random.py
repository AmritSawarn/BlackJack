import random
import tkinter


mainWindow = tkinter.Tk()
mainWindow.title("Ludo")
mainWindow.geometry("800x800")
mainWindow.configure(background="white", border="1")



def roll():
    run = random.randint(1,7)
    return run


card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)
player_token_frame = tkinter.Frame(card_frame, background="green")
player_token_frame.grid(row=1, column=1, sticky='ne', rowspan=6)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=5, column=1, columnspan=6, sticky='w')

dealer_button = tkinter.Button(button_frame, text="roll")
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player",)
player_button.grid(row=0, column=1)







mainWindow.mainloop()

