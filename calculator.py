import tkinter as tk
from tkinter import ttk


class Buttons:

    def __init__(self, root_, symbol, row_, column_, columnspan_=1):
        self.symbol = symbol
        self.row = row_
        self.column = column_
        self.root = root_
        self.columnspan = columnspan_
        self.root.columnconfigure(index=self.column, weight=0)
        self.root.rowconfigure(index=self.row, weight=0)

    def __str__(self):
        return self.symbol

    def draw(self):
        button = ttk.Button(text=self.symbol, command=lambda text=self.symbol: Output(text))
        button.grid(row=self.row, column=self.column, ipady=16, padx=1, pady=1, columnspan=self.columnspan)


def Output(button_symbol):
    if button_symbol == 'C':
        label['text'] = ''
    elif button_symbol == '←':
        label['text'] -= button_symbol
    elif button_symbol == 'x':
        label['text'] += '*'
    elif button_symbol == '√':
        label['text'] += '**0.5'
    elif button_symbol == '=':
        label['text'] = eval(label['text'])
        if isinstance(label['text'], int):
            int(label['text'])
    else:
        label['text'] += button_symbol


root = tk.Tk()
root.title('Calculator by B4bah')
width = 312
height = 350
root.geometry(str(width) + 'x' + str(height))
root.attributes('-topmost', True)
root.resizable(height=False, width=False)


buttons_text = [['C', '←', '√', '±'],
                ['7', '8', '9', '/'],
                ['4', '5', '6', 'x'],
                ['1', '2', '3', '-'],
                ['0', '.', '=', '+']]


for row in range(5):
    for column in range(4):
        Buttons(root, buttons_text[row][column], row+1, column+1).draw()


label = tk.Label(text='', font='arial, 24')
label.grid(row=0, column=0, rowspan=1, columnspan=5, pady=6, sticky='e')


root.mainloop()