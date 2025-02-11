from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 150)
window.config(padx = 80, pady = 40)

# Label
equal_to = Label(text = "is equal to", font = ("Arial", 10, "normal"))
equal_to.grid(column = 0, row = 1)

miles = Label(text = "Miles", font = ("Arial", 10, "normal"))
miles.grid(column = 2, row = 0)

kilometer = Label(text = "Km", font = ("Arial", 10, "normal"))
kilometer.grid(column = 2, row = 1)

kilometer_result = Label(text = "0", font = ("Arial", 10, "normal"))
kilometer_result.grid(column = 1, row = 1)

def button_clicked():
    input_miles = int(input.get())
    converted_miles = input_miles * 1.60934
    kilometer_result.config(text = converted_miles)
    
    
# Button
calculate = Button(text = "Calculate", command = button_clicked)
calculate.grid(column = 1, row = 2)

# Entry
input = Entry(width = 10)
input.insert(END, "0")
input.grid(column = 1, row = 0)






window.mainloop()