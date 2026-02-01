import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
        
        self.expression = ""
        
        # Display
        self.display = tk.Entry(root, font=font.Font(size=20), 
                                justify="right", bd=2)
        self.display.grid(row=0, column=0, columnspan=4, 
                         padx=10, pady=20, ipady=10, sticky="nsew")
        
        # Button layout
        buttons = [
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons, start=1):
            for j, btn_text in enumerate(row):
                self.create_button(btn_text, i, j)
        
        # Clear button
        clear_btn = tk.Button(root, text="C", font=font.Font(size=14),
                             command=self.clear)
        clear_btn.grid(row=5, column=0, columnspan=4, 
                      padx=10, pady=5, ipady=10, sticky="nsew")
    
    def create_button(self, text, row, col):
        btn = tk.Button(self.root, text=text, font=font.Font(size=16),
                       command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, padx=5, pady=5, 
                ipady=20, sticky="nsew")
    
    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression.replace('×', '*').replace('÷', '/'))
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""
    
    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()