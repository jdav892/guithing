from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=150, pady=150)

#label
left_label = Label(text="is equal to")
left_label.grid(column=0, row=1)


#button
output_label = Label(text = 0)
output_label.grid(column=1, row=1)


def button_clicked():
    num = input.get()
    output = float(num) * 1.6
    output_label.config(text=output)
    


button = Button(text="Convert", command=button_clicked)

button.grid(column=1, row=2)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
input = Entry(width=10)
input.get()
input.grid(column=1, row=0)






window.mainloop()
 