import customtkinter as ctk
import tkinter
import tkinter.messagebox


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=200, height=master.height,
                         fg_color="#3DF8FE", bg_color="#3DF8FE")

        """app name"""
        name_label = ctk.CTkLabel(
            self, text="CMS", font=("", 22), text_color="white")
        name_label.place(relx=0.5, rely=0.05, anchor="center")
