import customtkinter as ctk
import tkinter
import tkinter.messagebox


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#A7FBFE",
            bg_color="#A7FBFE"
        )
        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        """app name"""
        username_label = ctk.CTkLabel(
            self, text=f"{master.userInfo['userName']}\n{master.userInfo['role']}", font=("", 22), text_color="white")
        username_label.grid(column=1)
        profile_label = ctk.CTkButton(
            self, text="", font=("", 13), text_color="white", corner_radius=500, height=30, width=30)
        profile_label.grid(row=0, column=2, rowspan=1, sticky="n")
