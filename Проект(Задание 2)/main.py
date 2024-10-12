import tkinter as tk
from math import sin, cos, sqrt, pow, floor, ceil

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.memory = 0

        # Entry widget for displaying calculations
        self.result_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons configuration
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('√', 5, 2), ('%', 5, 3),
            ('^', 6, 0), ('floor', 6, 1), ('ceil', 6, 2), ('C', 6, 3),
            ('m+', 7, 0), ('mc', 7, 1)
        ]
        # Adding buttons to the calculator
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure grid to make all buttons the same size
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)