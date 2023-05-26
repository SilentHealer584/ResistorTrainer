import tkinter as tk
import random

window = tk.Tk()
window.geometry("375x375")
window.title("RRT")
window.iconbitmap("icon.ico")

window.grid_columnconfigure(0, weight=1)

colors = {0:'black', 1:'brown', 2:'red', 3:'orange', 4:'yellow', 5:'green', 6:'blue', 7:'purple', 8:'grey', 9:'white'}

title = tk.Label(window, text='Resistor Reading Trainer', font=("Arial", 20))
title.grid(row = 0, pady=8)

resistor = """_⊥_
/          \\"""

resistor = tk.Label(window, text=resistor)
resistor.grid(row = 2)

label1 = tk.Label(window, text="\\∎∎∎/")
label1.grid(row = 3)
label2 = tk.Label(window, text="|∎∎∎|")
label2.grid(row = 4)
label3 = tk.Label(window, text="|∎∎∎|")
label3.grid(row = 5)
resistor = tk.Label(window, text="|          |")
resistor.grid(row = 6)
label4 = tk.Label(window, text="/∎∎∎\\", fg='gold')
label4.grid(row = 7)
resistor = """\\          /
‾‾T‾‾"""
resistor = tk.Label(window, text=resistor)
resistor.grid(row = 8, pady=3)
resistorV = tk.Label(window)
resistorV.grid(row = 9, pady=3)
entry = tk.Entry(window, width= 15)
entry.focus_set()
entry.grid(row=10, pady=3)
wrong = 0

def new():
    resistorV.configure(text='', fg='black')
    global entry
    entry.delete(0, tk.END)
    first = random.randint(1, 9)
    label1.configure(fg=colors[first])
    second = random.randint(0, 9)
    label2.configure(fg=colors[second])
    third = random.randint(0, 9)
    label3.configure(fg=colors[third])
    window.update()
    
    value = f"{first}{second}{'0'*third}"
    value = int(value)
    
    def verify():
        global entry, wrong
        string= entry.get()
        
        try:
            string = int(string)
        except:
            resistorV.configure(text='Resistor value should be integer')
        
        if string == value:
            resistorV.configure(text='CORRECT', fg='green')
            okay = tk.Button(window, text= "Okay",width= 20, command= verify)
            okay.configure(state="disabled")
            okay.grid(row=11, pady=3)
            wrong = 0
        else:
            if wrong < 3:
                wrong += 1
                resistorV.configure(text=f'{wrong} WRONG', fg='red')
            else:
                resistorV.configure(text=f'WRONG! The answer was {value}Ω', fg='red')
                okay = tk.Button(window, text= "Okay",width= 20, command= verify)
                okay.configure(state="disabled")
                okay.grid(row=11, pady=3)
                wrong = 0
                     
    okay = tk.Button(window, text= "Okay",width= 20, command= verify).grid(row=11, pady=3)
    tk.Button(window, text= "Next",width= 20, command= new).grid(row=12, pady=3)
    
new()

window.mainloop()
