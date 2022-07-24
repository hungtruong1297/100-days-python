from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width = 500, height= 300)

#Label

label = Label(text="I am a Label", font=("Airal", 24, "bold"))
label.grid(column=0, row=0)

# label['text'] = 'New Text'



def button_clicked():
    text = input.get()
    label.config(text=text)
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)










window.mainloop()