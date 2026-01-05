import tkinter as tk
from tkinter import messagebox
import auth
from snake_game import start_game

root = tk.Tk()
root.title("Pac-Man Snake Login")
root.geometry("300x260")

username_var = tk.StringVar()
password_var = tk.StringVar()

def do_login():
    if auth.login(username_var.get(), password_var.get()):
        root.destroy()
        start_game(username_var.get(), auth.update_score)
    else:
        messagebox.showerror("Error", "Invalid username or password")

def do_signup():
    if auth.signup(username_var.get(), password_var.get()):
        messagebox.showinfo("Success", "Account created. Please login.")
    else:
        messagebox.showerror("Error", "User already exists")

tk.Label(root, text="Username").pack(pady=5)
tk.Entry(root, textvariable=username_var).pack()
tk.Label(root, text="Password").pack(pady=5)
tk.Entry(root, textvariable=password_var, show="*").pack()

tk.Button(root, text="Login", width=20, command=do_login).pack(pady=5)
tk.Button(root, text="Sign Up", width=20, command=do_signup).pack()

root.mainloop()
