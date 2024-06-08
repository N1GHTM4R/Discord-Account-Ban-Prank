import tkinter as tk

window = tk.Tk()

window.geometry("400x300")

def on_button_click():
    label.config(text="Sucsessfully banned!")

def check_password():
    entered_password = password_entry.get() #type: ignore
    if entered_password == "Admin56":
        show_widgets()
    else: 
        error_label.config(text="Incorrect password.") 

def show_widgets():
    label.grid(row=2, column=0, columnspan=2, pady=10)
    button.grid(row=3, column=0, columnspan=2, pady=10)
    error_label.grid_forget()

    password_label = tk.Label(window, text="Enter Administrator Password")
    password_label.grid(row=0, column=0, padx=10, pady=10)


    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=0, column=1, padx=10, pady=10)

    submit_button = tk.Button(window, text="Submit", command=check_password)
    submit_button.grid(row=1, column=0, columnspan=2, pady=10)


label = tk.Label(window, text="Ban account?")
label.grid(row=0, column=0, padx=10, pady=10)

button = tk.Button(window, text="Ban Permanently", command=on_button_click)
button.grid(row=1, column=0, padx=10, pady=10)

error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
#end of program