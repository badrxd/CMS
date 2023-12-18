import customtkinter as ctk
import tkinter
import tkinter.messagebox


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, on_login):
        super().__init__(master, corner_radius=7, width=220, height=390)
        self.place(relx=0.5, rely=0.5, anchor="center")

        self.on_login = on_login

        """username input"""
        username = ctk.CTkEntry(
            self, placeholder_text="Enter Your Username", width=180, height=20)
        username.pack(pady=(50, 10), padx=20)

        """passworld input"""
        password = ctk.CTkEntry(
            self, placeholder_text="Enter Your Password", width=180, height=20, show="*")
        password.pack(pady=(10, 50), padx=20)

        """login button"""
        button = ctk.CTkButton(
            self, text="login", command=self.on_login)
        button.pack(pady=(10, 50), padx=20)
