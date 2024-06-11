import tkinter as tk


window = tk.Tk()
window.geometry("400x300")
window.title("Acount Ban Admin")
window.iconbitmap("logo.ico")



def on_button_click():
    print("Button clicked!")


def check_credentials():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    print(f"Entered Username: {entered_username}")  # Debugging line
    print(f"Entered Password: {entered_password}")  # Debugging line

    if entered_username == "Nightmare" and entered_password == "Admin56":  # Replace with your desired username and password
        print("Credentials correct!")  # Debugging line
        show_ban_widgets()
    else:
        print("Credentials incorrect!")  # Debugging line
        error_label.config(text="Incorrect username or password. Please try again.")

# Function to display the ban widgets
def show_ban_widgets():
    print("Showing ban widgets!")  # Debugging line
    ban_username_label.grid(row=4, column=0, padx=10, pady=10)
    ban_username_entry.grid(row=4, column=1, padx=10, pady=10)
    ban_button.grid(row=5, column=0, columnspan=2, pady=10)
    error_label.grid_forget()  # Hide the error label if present


def ban_account():
    friend_username = ban_username_entry.get()
    status_label.config(text=f"Account '{friend_username}' has been banned.")
    status_label.grid(row=6, column=0, columnspan=2, pady=10)


username_label = tk.Label(window, text="Enter Your Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=10)


password_label = tk.Label(window, text="Enter Your Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(window, show="*")  
password_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(window, text="Submit", command=check_credentials)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)


error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2, pady=10)


ban_username_label = tk.Label(window, text="Enter Account Username:")
ban_username_entry = tk.Entry(window)
ban_button = tk.Button(window, text="Ban Account", command=ban_account)


status_label = tk.Label(window, text="")


window.mainloop()
# end of program