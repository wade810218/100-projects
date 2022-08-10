from tkinter import *

def converter():
    miles = miles_input.get()
    kilometers = round(float(miles)*1.609 , 2)
    result_label.config( text = f"{kilometers}" )
    

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=270, height=90)
window.config(padx=10, pady=10)

miles_label = Label(text = "Miles")
is_equal_label =Label(text = "is equal to")
result_label = Label(text = "0")
kilometer_label = Label(text = "Km")

miles_label.grid(row=0,column=2)
is_equal_label.grid(row=1,column=0)
result_label.grid(row=1,column=1)
kilometer_label.grid(row=1,column=2)

calculate_button = Button(text = "Calculate", command= converter)
calculate_button.grid(row=2,column=1)

miles_input = Entry(width= 10)
miles_input.insert(END, string="0")
miles_input.grid(row=0,column=1)
