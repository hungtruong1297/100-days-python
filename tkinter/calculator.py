from tkinter import *

root = Tk()
root.title("Miles to Km Converter")
root.minsize(width = 250, height= 100)



entry = Entry(width=10)
entry.grid(row=0, column=1)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(row=1, column=0)

label_Miles = Label(text="Miles")
label_Miles.grid(row=0, column=2)

label_Km = Label(text="Km")
label_Km.grid(row=1, column=2)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

def calculate():
    input = entry.get()
    mile_to_km = 1.609344
    output = round(float(input)*mile_to_km, 2)
    label_result.config(text=output)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)










root.mainloop()