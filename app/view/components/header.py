import customtkinter as ctk
import tkinter
import tkinter.messagebox


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#A7FBFE",
            bg_color="#A7FBFE",
            height=70
        )

        """app name"""
        # name_label = ctk.CTkLabel(
        #     self, text="CMS", font=("", 22), text_color="white")
        # name_label.place(relx=0.5, rely=0.05, anchor="center")
