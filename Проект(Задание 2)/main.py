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
