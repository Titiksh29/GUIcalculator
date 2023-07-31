import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create the entry field for the calculator display
entry = tk.Entry(root, font=("Helvetica", 20), justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Create the buttons for the calculator
button_symbols = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("=",)
]

for symbol_row in button_symbols:
    frame = tk.Frame(root)
    frame.pack()

    for symbol in symbol_row:
        button = tk.Button(frame, text=symbol, font=("Helvetica", 15), padx=20, pady=10)
        button.pack(side=tk.LEFT)
        button.bind("<Button-1>", on_click)

# Start the main event loop
root.mainloop()
