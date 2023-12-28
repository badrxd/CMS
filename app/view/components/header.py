import customtkinter as ctk
import tkinter
import tkinter.messagebox
from PIL import Image
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
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=50)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        """app name"""
        self.title = ctk.CTkLabel(self,
                                  text="",
                                  width=50,
                                  font=(GStyle.font_family,
                                        GStyle.large),
                                  text_color=GStyle.head_font_color,
                                  fg_color=GStyle.header_bg,
                                  bg_color=GStyle.header_bg
                                  )
        self.title.grid(row=0, column=0, rowspan=2)

        """create an image object"""
        image = ctk.CTkImage(light_image=Image.open(
            GStyle.icon))

        bt = ctk.CTkButton(
            self, width=2, image=image, text="", corner_radius=500, fg_color=GStyle.header_bg, hover_color=GStyle.header_bg,
            command=self._change_mode)
        bt.grid(column=2, row=0, sticky="ns", pady=(10, 0))

        username_label = ctk.CTkLabel(
            self, text=f"{master.userInfo['fullName']}", font=(GStyle.font_family, GStyle.meduim), text_color=GStyle.head_font_color)
        username_label.grid(column=3, row=0, padx=(0, 20), sticky="en")
        username_label = ctk.CTkLabel(
            self, text=f"{master.userInfo['role']}", font=(GStyle.font_family, GStyle.small), text_color=GStyle.head_font_color)
        username_label.grid(column=3, row=1, padx=(0, 20), sticky="en")

    def _change_mode(self):
        GStyle.switch_mode()
        self.dashboard.refresh(self.dashboard.userInfo)
