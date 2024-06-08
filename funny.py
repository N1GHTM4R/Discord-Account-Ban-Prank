import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("400x300")

# Define the function to be called when the button is clicked
def on_button_click():
    label.config(text="Account Banned Succsessfully!")

# Define the function to check the password
def check_password():
    entered_password = password_entry.get()
    print(f"Entered Password: {entered_password}")  # Debugging line
    if entered_password == "Admin56":  # Replace "mypassword" with your desired password
        print("Password correct!")  # Debugging line
        show_widgets()
    else:
        print("Password incorrect!")  # Debugging line
        error_label.config(text="Incorrect password. Please try again.")

# Function to display the button and label
def show_widgets():
    label.grid(row=2, column=0, columnspan=2, pady=10)
    button.grid(row=3, column=0, columnspan=2, pady=10)
    error_label.grid_forget()  # Hide the error label if present

# Create and grid a password entry
password_label = tk.Label(window, text="Enter Password:")
password_label.grid(row=0, column=0, padx=10, pady=10)

password_entry = tk.Entry(window, show="*")  # Use show="*" to hide the password characters
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and grid a submit button for the password
submit_button = tk.Button(window, text="Submit", command=check_password)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

# Create a label and button that will be displayed after the correct password is entered
label = tk.Label(window, text="Ban Account?")
button = tk.Button(window, text="Ban Permanently", command=on_button_click)

# Create an error label for incorrect password attempts
error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()

#end of program