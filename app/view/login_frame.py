import customtkinter as ctk
import tkinter
import tkinter.messagebox
from app.core.authentication import GetUser


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, on_login):
        super().__init__(master, corner_radius=7,
                         width=220, height=390)
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.master = master
        self.on_login = on_login

        """username input"""
        self.username = ctk.CTkEntry(
            self, placeholder_text="Enter Your Username", width=320, height=40, font=("", 16))
        self.username.pack(pady=(50, 10), padx=20)

        """passworld input"""
        self.password = ctk.CTkEntry(
            self, placeholder_text="Enter Your Password", width=320, height=40, show="*", font=("", 16))
        self.password.pack(pady=(10, 50), padx=20)

        """login button"""
        button = ctk.CTkButton(
            self, text="Login", command=self.login, font=("", 16), height=40)
        button.pack(pady=(10, 50), padx=20)

    def login(self):
        """ database connection"""
        if self.username.get() == "" or self.password.get() == "":
            tkinter.messagebox.showerror(
                "Login Failed", "Please Fill the fields")
        else:
            req = GetUser(self.username.get(), self.password.get())
            if req['status']:
                self.on_login(req['userId'])
            else:
                tkinter.messagebox.showerror(
                    "Login Failed", f"Invalid: {req['message']}")
