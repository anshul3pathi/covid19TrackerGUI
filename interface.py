import tkinter as tk
from tkinter import ttk
import covid19tracker as cov
from datetime import datetime as dt 

print("Opening...")

# state_figures = cov.stateFigures()

demo_attr = ["Confirmed:", "Active:", "Recovered:", "Deceased:"]
demo_vals = ["300000", "15000", "150000", "10000"]

demo_list = ['a', 'b']

window = tk.Tk()
window.title("Covid 19 Tracker")
window.resizable(False, False)
window.geometry("800x400")

DATE = f"{dt.now():%d/%B/%Y}"

def comboboxEvent(event):
    print(combo_box.get())

# Drawing ALL INDIA section
India_Outer_bg = "gray25"
allindia_outer = tk.Canvas(window, width=500, height=50, bg=India_Outer_bg, highlightthickness=0).place(x=0, y=0)
label1 = tk.Label(allindia_outer, text="All India", bg=India_Outer_bg, fg="white", font=("Constantia", 25, "bold")).place(x=5, y=5) # All India Label
label2 = tk.Label(allindia_outer, text=DATE, bg=India_Outer_bg, fg="white", font=("Constantia", 25, "italic")).place(x=300, y=5)  # Current Date label

India_Inner_bg = "dim gray"
all_india = tk.Canvas(window, width=500, height=350, highlightthickness=0, bg="dim gray").place(x=0, y=50)  # All India inner canvas
label3 = tk.Label(all_india, text=demo_attr[0]+" "+demo_vals[0], bg=India_Inner_bg, fg="firebrick1", font=("Courier", 25, "bold")).place(x=5, y=80)  # ALl India -> Confirmed attribute and value label
label4 = tk.Label(all_india, text=demo_attr[1]+" "+demo_vals[1], bg=India_Inner_bg, fg="deep sky blue", font=("Courier", 25, "bold")).place(x=5, y=150)  # All India -> Active attribute and value label
label5 = tk.Label(all_india, text=demo_attr[2]+" "+demo_vals[2], bg=India_Inner_bg, fg="green2", font=("Courier", 25, "bold")).place(x=5, y=220)  # All India -> Recovered attribute and value label
label6 = tk.Label(all_india, text=demo_attr[3]+" "+demo_vals[3], bg=India_Inner_bg, fg="black", font=("Courier", 25, "bold")).place(x=5, y=290)  # All India -> Deceased attribute and value label

# Drawing state wise section
State_Outer_bg = "pale violet red"
states_outer = tk.Canvas(window, width=300, height=50, bg=State_Outer_bg, highlightthickness=0).place(x=500, y=0)
label7 = tk.Label(states_outer, text="Select State: ", bg=State_Outer_bg, fg="white", font=("Times New Roman", 12)).place(x=510, y=10)  # Select state Label
state = tk.StringVar()
combo_box = ttk.Combobox(states_outer, width=25, values=demo_list)  # Combobox for selecting from the list of states
combo_box.place(x=610, y=10)
combo_box.current(0)
combo_box.bind("<<ComboboxSelected>>", comboboxEvent)



window.mainloop()
