"""
Create a GUI calculator using tkinter that displays numbers and operations
on a screen, with buttons for digits 0-9 and basic operations (+, -, *, /).
Include a clear button (C) to reset the calculator and an equals button (=)
to compute the result.
Add error handling for invalid operations like division by zero,
and make the interface visually appealing with a clean button layout
and a display screen at the top.

"""

import tkinter as tk

class Calculator:
    """
    A simple GUI calculator application using Tkinter.

    This calculator supports basic arithmetic operations (+, -, *, /),
    displays results, and includes a clear button. It also handles
    basic error cases like invalid expressions.
    """
    def __init__(self, root):
        """
        Initializes the Calculator application.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("250x250")
        self.root.configure(bg="#f0f0f0")

        self.display = tk.Entry(root, width=25, justify="right", font=("Helvetica", 14), bg="#ffffff", fg="#333")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        """
        Creates and places all the calculator buttons on the GUI.
        """
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Helvetica", 12),
                               bg="#ffffff", fg="#333", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        """
        Handles button click events.

        Performs actions based on the clicked button:
        - 'C' clears the display.
        - '=' evaluates the expression on the display.
        - Digits and operators are appended to the display.

        Args:
            value (str): The text value of the clicked button.
        """
        if value == 'C':
            self.display.delete(0, tk.END)
        elif value == '=':
            try:
                # Evaluate the expression, handling potential division by zero
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except ZeroDivisionError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error: Div by zero")
            except (SyntaxError, NameError):
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error: Invalid expr")
            except Exception as e:
                # Catch any other unexpected errors
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
