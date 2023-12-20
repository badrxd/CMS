import customtkinter as ctk
import tkinter
import tkinter.messagebox
from ..global_style import GStyle


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.header_bg,
            bg_color=GStyle.header_bg
        )
        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        """app name"""
        username_label = ctk.CTkLabel(
            self, text=f"{master.userInfo['userName']}\n{master.userInfo['role']}", font=(GStyle.font_family, 22), text_color=GStyle.font_color)
        username_label.grid(column=1)
