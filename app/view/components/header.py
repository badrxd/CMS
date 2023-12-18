import customtkinter as ctk
import tkinter
import tkinter.messagebox


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=master.width, height=80,
                         fg_color="#A7FBFE", bg_color="#A7FBFE")

        """app name"""
        # name_label = ctk.CTkLabel(
        #     self, text="CMS", font=("", 22), text_color="white")
        # name_label.place(relx=0.5, rely=0.05, anchor="center")
