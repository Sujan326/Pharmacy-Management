import tkinter as tk
from tkinter import messagebox
import hashlib
import uuid
import project


# Function to hash a password using SHA-256
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Function to save the username, hashed password, and ID in a file
def save_user(username, hashed_password, user_id):
    with open("users.txt", "a") as file:
        file.write(f"{user_id}:{username}:{hashed_password}\n")

# Function to check if the entered password matches the stored hashed password
def login(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            stored_id, stored_username, stored_password = line.strip().split(":")
            if stored_username == username:
                hashed_password = hash_password(password)
                if stored_password == hashed_password:
                    return True
                else:
                    return False
        return False

# Function to handle sign-up button click
def sign_up():
    username = entry_username.get()
    password = entry_password.get()

    # Generate a unique ID
    user_id = str(uuid.uuid4())

    # Hash the password
    hashed_password = hash_password(password)

    # Save the username, hashed password, and ID in a file
    save_user(username, hashed_password, user_id)

    messagebox.showinfo("Sign Up", f"Sign up successful!\nHash value: {user_id}")

# Function to handle login button click
def login_button():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the entered password is correct
    if login(username, password):
        messagebox.showinfo("Login", "Login successful!")
        open_main_page()
    else:
        messagebox.showerror("Login", "Invalid username or password!")

# Function to open the main page
def open_main_page():
    # Destroy the login window
    window.destroy()

    # Create the main page window
    main_window = tk.Tk(project)
    main_window.title("Main Page")

    # Add your main page content here

    # Start the main GUI loop for the main page
    main_window.mainloop()

# Create the login window
window = tk.Tk()
window.title("Sign Up and Login")
window.geometry("300x200")

# Create the username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# Create the password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create the sign-up button
button_sign_up = tk.Button(window, text="Sign Up", command=sign_up)
button_sign_up.pack()

# Create the login button
button_login = tk.Button(window, text="Login", command=login_button)
button_login.pack()

# Start the main GUI loop for the login window
window.mainloop()
    