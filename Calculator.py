import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def clear_entry():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ")

def add_to_expression(symbol):
    entry.insert(tk.END, symbol)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget for expressions
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=1, column=0, columnspan=4)

# Create number buttons
for i in range(10):
    row = 3 - i // 3
    col = i % 3
    tk.Button(root, text=str(9 - i), command=lambda num=i: add_to_expression(str(9 - num))).grid(row=row + 2, column=col, padx=5, pady=5)

# Create operator buttons
operators = ['/', '*', '-', '+']
for i, operator in enumerate(operators):
    tk.Button(root, text=operator, command=lambda op=operator: add_to_expression(op)).grid(row=i + 2, column=3, padx=5, pady=5)

# Create other buttons
tk.Button(root, text='=', command=evaluate_expression).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text='C', command=clear_entry).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text='.', command=lambda: add_to_expression('.')).grid(row=5, column=3, padx=5, pady=5)

root.mainloop()
