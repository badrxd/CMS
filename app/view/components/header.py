import customtkinter as ctk
import tkinter
import tkinter.messagebox
from ..global_style import GStyle


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.header_bg,
            bg_color=GStyle.header_bg,
            corner_radius=0
        )
        self.dashboard = master
        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        """app name"""

        bt = ctk.CTkButton(
            self, width=20, text="light mode", corner_radius=500, fg_color=GStyle.bg, hover_color=GStyle.buttons_hover_color,
            command=self._change_mode)
        bt.grid(column=1, row=0, sticky="ns", pady=(10, 0))

        username_label = ctk.CTkLabel(
            self, text=f"{master.userInfo['fullName']}", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color)
        username_label.grid(column=2, row=0, sticky="en")
        username_label = ctk.CTkLabel(
            self, text=f"{master.userInfo['role']}", font=(GStyle.font_family, GStyle.small), text_color=GStyle.head_font_color)
        username_label.grid(column=2, row=1, sticky="en")

    def _change_mode(self):
        GStyle.switch_mode()
        self.dashboard.refresh(self.dashboard.userInfo)
