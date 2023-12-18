import customtkinter as ctk
import tkinter
import tkinter.messagebox


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, on_logout):
        super().__init__(master)
        self.on_logout = on_logout

        logout_button = ctk.CTkButton(
            self, text="Logout", width=50, command=self.on_logout)
        logout_button.pack()
