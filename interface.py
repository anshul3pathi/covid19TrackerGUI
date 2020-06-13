from tkinter import *
import covid19tracker as cov

attributes, values = cov.allIndiafigures()

window = Tk()
window.title("Covid 19 Tracker")
window.geometry("800x400")

label1 = Label(window, text=attributes[0]).place(x=10, y=10)




window.mainloop()
