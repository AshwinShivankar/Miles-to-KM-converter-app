from tkinter import *

def action():
    new = input.get()
    km = round(int(new) * float(1.609))
    label_3.config(text = km)

window = Tk()
window.title("Mile to Km Conveter")
# window.minsize(width=300, height=150)
window.config(padx = 20, pady=20)



#
label = Label(text= "Miles")
label.grid(column=3,row=0)


label_2 = Label(text="is equal to")
label_2.grid(column=1,row=1)

label_3 = Label(text="0")
label_3.grid(column=2,row=1)

label_4 = Label(text="KM")
label_4.grid(column=3,row=1)

input = Entry(width=10)
input.grid(column=2, row=0)

button = Button(text="Calculate", command=action)
button.grid(column=2, row=3)


window.mainloop()















# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# def action():
#     print("I got clicked")
#     new = input.get()
#     label.config(text = new)
#
# #Labels
# label = Label(text=" text")
# label.config(text= "button")
# label.grid(column=0,row=0)
#
# #Button
# button = Button(text="Click Me", command=action)
# button.grid(column=1,row=1)
#
#
# new_button = Button(text="buttons")
# new_button.grid(column=3,row=0)
#
#
# # input
# input = Entry(width=10)
# input.grid(column=4,row=4)
#
#
#
# window.mainloop()