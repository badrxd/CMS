import customtkinter as ctk
import tkinter
import tkinter.messagebox


class DashboardFrame(ctk.CTkFrame):
    userId = ""

    def __init__(self, master, on_logout, userId):
        super().__init__(master)
        self.on_logout = on_logout
        self.userId = userId
        print(userId)
        logout_button = ctk.CTkButton(
            self, text="Logout", width=50, command=self.on_logout)
        logout_button.pack()
