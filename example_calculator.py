import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.master = root
        root.title("My Calculator")

        self.result = tk.Entry(root, width=20)
        self.result.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1),('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 1), ('C', 4, 0), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, command=lambda t=text: self.on_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def on_click(self, text):
        if text == '=':
            try:
                self.result.insert(tk.END, " = " + str(eval(self.result.get())))
            except Exception as e:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, "Error")
        elif text == 'C':
            self.result.delete(0, tk.END)
        else:
            self.result.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
