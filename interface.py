import tkinter as tk
from tkinter import ttk
import covid19tracker as cov
from datetime import datetime as dt 

print("Opening...")

attributes, allFigures = cov.allFigures()

window = tk.Tk()
window.title("Covid 19 Tracker")
window.resizable(False, False)
window.geometry("800x400")

DATE = f"{dt.now():%d/%B/%Y}"

def stateFigures(event):
    """function displays corona figures of the state selected by the user"""
    selection = combo_box.get()
    # print(len(selection))
    if len(selection) > 19 and len(selection) < 28:
        label8["font"] = ("Roman", 15, "bold")
    elif len(selection) > 28:
        label8["font"] = ("Roman", 11, "bold")
    else:
        label8["font"] = ("Roman", 25, "bold")

    label8["text"] = selection
    label9["text"] = attributes[0]+" : "+allFigures[selection][0]
    label10["text"] = attributes[1]+" : "+allFigures[selection][1]
    label11["text"] = attributes[2]+" : "+allFigures[selection][2]
    label12["text"] = attributes[3]+" : "+allFigures[selection][3]
    

# Drawing ALL INDIA section
India_Outer_bg = "gray15"
allindia_outer = tk.Canvas(window, width=500, height=50, bg=India_Outer_bg, highlightthickness=0).place(x=0, y=0)
label1 = tk.Label(allindia_outer, text="All India", bg=India_Outer_bg, fg="white", font=("Constantia", 25, "bold")).place(x=5, y=5) # All India Label
label2 = tk.Label(allindia_outer, text=DATE, bg=India_Outer_bg, fg="white", font=("Constantia", 25, "italic")).place(x=300, y=5)  # Current Date label

India_Inner_bg = "midnight blue"
all_india = tk.Canvas(window, width=500, height=350, highlightthickness=0, bg=India_Inner_bg).place(x=0, y=50)  # All India inner canvas
label3 = tk.Label(all_india, text=attributes[0]+" : "+allFigures["All India"][0], bg=India_Inner_bg, fg="firebrick1", font=("Courier", 25, "bold")).place(x=5, y=80)  # ALl India -> Confirmed attribute and value label
label4 = tk.Label(all_india, text=attributes[1]+" : "+allFigures["All India"][1], bg=India_Inner_bg, fg="deep sky blue", font=("Courier", 25, "bold")).place(x=5, y=150)  # All India -> Active attribute and value label
label5 = tk.Label(all_india, text=attributes[2]+" : "+allFigures["All India"][2], bg=India_Inner_bg, fg="green2", font=("Courier", 25, "bold")).place(x=5, y=220)  # All India -> Recovered attribute and value label
label6 = tk.Label(all_india, text=attributes[3]+" : "+allFigures["All India"][3], bg=India_Inner_bg, fg="gray25", font=("Courier", 25, "bold")).place(x=5, y=290)  # All India -> Deceased attribute and value label
label13 = tk.Label(all_india, text="Data taken from covid19india.org", bg=India_Inner_bg, fg="white").place(x=318, y=375)


# Drawing state wise section
# State wise outer Canvas
State_Outer_bg = "brown3"
states_outer = tk.Canvas(window, width=300, height=50, bg=State_Outer_bg, highlightthickness=0).place(x=500, y=0)
label7 = tk.Label(states_outer, text="Select State: ", bg=State_Outer_bg, fg="black", font=("Times New Roman", 12)).place(x=510, y=10)  # Select state Label
combo_box = ttk.Combobox(states_outer, width=25, values=list(allFigures.keys()))  # Combobox for selecting from the list of states
combo_box.place(x=610, y=10)
combo_box.current(0)
combo_box.bind("<<ComboboxSelected>>", stateFigures)

# State wise inner Canvas
State_Inner_bg = "burlywood4"
state_inner = tk.Canvas(window, width=300, height=350, bg=State_Inner_bg, highlightthickness=0).place(x=500, y=50)

#Dynamic labels -> Their values will change according to the state selected
label8 = tk.Label(state_inner, text=combo_box.get(), font=("Roman", 25, "bold"), bg=State_Inner_bg, fg="orange")  # Label for displaying name of current selection
label8.place(x=510, y=65)
label9 = tk.Label(state_inner, text=attributes[0]+" : "+allFigures["All India"][0], bg=State_Inner_bg, fg="tomato", font=("Roman", 20, "bold"))  # State wie -> Confirmed attribute and value label
label9.place(x=510, y=120)
label10 = tk.Label(state_inner, text=attributes[1]+" : "+allFigures["All India"][1], bg=State_Inner_bg, fg="deep sky blue", font=("Roman", 20, "bold"))  # State wise -> Activae attribute and value label
label10.place(x=510, y=180)
label11 = tk.Label(state_inner, text=attributes[2]+" : "+allFigures["All India"][2], bg=State_Inner_bg, fg="green2", font=("Roman", 20, "bold"))  # State wise -> Recovered attribute and values label
label11.place(x=510, y=240)
label12 = tk.Label(state_inner, text=attributes[3]+" : "+allFigures["All India"][3], bg=State_Inner_bg, fg="black", font=("Roman", 20, "bold"))  # State wise -> Deceased attribute and values label
label12.place(x=510, y=300)

window.mainloop()
