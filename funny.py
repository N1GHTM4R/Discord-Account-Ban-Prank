import tkinter as tk

window = tk.Tk()

window.geometry("800x600")

def on_button_click():
    label.config(text="omg it works")


label = tk.Label(window, text="Click it")
label.grid(row=0, column=0, padx=10, pady=10)

button = tk.Button(window, text="click me!", command=on_button_click)
button.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()