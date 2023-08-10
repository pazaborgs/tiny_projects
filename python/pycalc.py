from tkinter import *


class Calculator:

    def __init__(self):
        self.operation = ""
        self.history=["212", "213", "432", "500"]
    
    def btn_click(self, item):
        self.operation += str(item)
        display_text.set(self.operation)

    def btn_clear(self):
        self.operation=""
        self.history=[]
        display_text.set(self.operation)

    def btn_clear_last(self):
        self.operation= self.history[-2]
        self.history.pop()
        display_text.set(self.history[-1])

    def btn_erase_to_left(self):
        self.operation = self.operation[:-1]
        display_text.set(self.operation)

Calc = Calculator()

labels = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

operators = ["/", "*", "-", "+"]
    
# Stuff


window = Tk()
window.title("Python Calculator")
window.geometry("312x312")


display_text = StringVar(value = Calc.operation)


display_frame = Frame(window, width=312, height=50, bg='Red')
display_frame.pack(side=TOP)

display_entry = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=display_text, bg='#fff', justify=RIGHT)
display_entry.grid(row = 0, column=0)

btn_frame = Frame(window, width=312, height=262, bg='Blue')
btn_frame.pack()


# 1 to 9

for r in range(len(labels)):
    for c in range(len(labels)):
        btn = Button(btn_frame, text = labels[r][c], fg = "black", bg = "#fff", cursor = "hand2", width=10, command = lambda item=labels[r][c]: Calc.btn_click(item))

        btn.grid(row =r + 1, column=c)

# Operators

for item in range(len(operators)):
    btn = Button(btn_frame, text = operators[item], fg = "black", bg = "#fff", cursor = "hand2", width=10, command = lambda item=operators[item]: Calc.btn_click(item))
    btn.grid(row = item, column=4)

# C, CE, Delete

btn_C = Button(btn_frame, text = "C", fg = "black", bg = "#fff", cursor = "hand2", width=10, command = lambda: Calc.btn_clear()).grid(row = 0, column=0)
btn_CE = Button(btn_frame, text = "CE", fg = "black", bg = "#fff", cursor = "hand2", width=10, command = lambda: Calc.btn_clear_last()).grid(row = 0, column=1)
btn_erase = Button(btn_frame, text = "⌫", fg = "black", bg = "#fff", cursor = "hand2", width=10, command = lambda: Calc.btn_erase_to_left()).grid(row = 0, column=2)













# Row 1

#one = Button(btn_frame, text = 1, fg = "black", bg = "#fff", cursor = "hand2", command = lambda: Calc.btn_click(1)).grid(row = 1, column=0)
#two = Button(btn_frame, text = 2, fg = "black", bg = "#fff", cursor = "hand2", command = lambda: Calc.btn_click(2)).grid(row = 1, column=1)
#three = Button(btn_frame, text = 3, fg = "black", bg = "#fff", cursor = "hand2", command = lambda: Calc.btn_click(3)).grid(row = 1, column=2)

# Row 2

#four = Button(btn_frame, text = 4, fg = "black", bg = "#fff", cursor = "hand2", command = lambda: Calc.btn_click(4)).grid(row = 2, column=0)
#five = Button(btn_frame, text = 5, fg = "black", bg = "#fff", cursor = "hand2", command = lambda: Calc.btn_click(5)).grid(row = 2, column=1)
#six = Button(btn_frame, text = 6, fg = "black", bg = "#fff", cursor = "hand2", command = lambda: Calc.btn_click(6)).grid(row = 2, column=2)     
    
    

window.mainloop()





    