from colorama import Fore, Back, Style
import tkinter as tk
import random

window = tk.Tk()

colors = {0:'black', 1:'brown', 2:'red', 3:'orange', 4:'yellow', 5:'green', 6:'blue', 7:'purple', 8:'grey', 9:'white'}

resistor = """_⊥_
/          \\"""

resistor = tk.Label(window, text=resistor)
resistor.grid(row = 0)

def new():
    global entry
    first = random.randint(1, 9)
    label1 = tk.Label(window, text="\\∎∎∎/", fg=colors[first])
    label1.grid(row = 1)
    second = random.randint(0, 9)
    label2 = tk.Label(window, text="|∎∎∎|", fg=colors[second])
    label2.grid(row = 2)
    third = random.randint(0, 9)
    label3 = tk.Label(window, text="|∎∎∎|", fg=colors[third])
    label3.grid(row = 3)
    window.update()

    resistor = tk.Label(window, text="|          |")
    resistor.grid(row = 4)

    label3 = tk.Label(window, text="/∎∎∎\\", fg='gold')
    label3.grid(row = 5)

    resistor = """\\          /
‾‾T‾‾"""
    resistor = tk.Label(window, text=resistor)
    resistor.grid(row = 6)
    
    value = f"{first}{second}{'0'*third}"
    value = int(value)
    
    resistorV = tk.Label(window, text=value)
    resistorV.grid(row = 7)
    
    def verify():
        global entry
        string= entry.get()
        resistorV.configure(text=string)
    
    entry = tk.Entry(window, width= 40)
    entry.focus_set()
    entry.grid(row=8)

    tk.Button(window, text= "Okay",width= 20, command= verify).grid(row=9)
    tk.Button(window, text= "Next",width= 20, command= new).grid(row=10)
    
new()

window.mainloop()


















