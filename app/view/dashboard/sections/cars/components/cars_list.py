import customtkinter as ctk
from .....global_style import GStyle
from .....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image


class CarsList(ctk.CTkFrame):
    def __init__(self, master, manager):
        super().__init__(
            master,
            fg_color=GStyle.bg,
            bg_color=GStyle.bg
        )
        self.manager = manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=20)
        self.columnconfigure(2, weight=1)
        for i in range(5):
            self.rowconfigure(i, weight=1)
        self.rowconfigure(3, weight=5)
        head = ctk.CTkFrame(self, fg_color=GStyle.frames_bg,
                            corner_radius=7, height=10)
        head.grid(row=1, column=1, sticky='news', padx=10, pady=10)
        head.rowconfigure(0, weight=1)
        head.columnconfigure(0, weight=10)
        head.columnconfigure(1, weight=1)
        head.columnconfigure(2, weight=1)
        self.search = ctk.CTkEntry(
            head,
            fg_color=GStyle.frames_bg,
            text_color=GStyle.frames_font_color,
            placeholder_text_color=GStyle.frames_font_color,
            placeholder_text="Search for car",
            border_width=0,
            font=(GStyle.font_family,
                  GStyle.meduim)
        )
        self.search.grid(row=0, column=0, rowspan=1, sticky='news', padx=30)

        button = ctk.CTkButton(head, text='search', fg_color="#2b5dff", hover_color="#2958ee", corner_radius=7, height=5, width=50).grid(
            row=0, column=1, rowspan=1, sticky='news', pady=5, padx=3)
        button = ctk.CTkButton(head, text='add', fg_color="#03d084", hover_color="#00c87e", corner_radius=7, height=5, width=50).grid(
            row=0, column=2, rowspan=1, sticky='news', pady=5, padx=(0, 3))
        body = ProCTkScrollableFrame(self, fg_color=GStyle.bg)
        body.grid(row=3, column=1, sticky='news')
        cars = self.getcars()
        for c in cars:
            car = Carinfo(body, c)
            """show cars"""

    def getcars(self):
        """call database for cars"""
        return []


class Carinfo(ctk.CTkFrame):
    def __init__(self, master, car_data):
        super().__init__(
            master,
            fg_color=GStyle.frames_bg,
            bg_color=GStyle.frames_bg
        )
        self.data = car_data
        self.master = master

    def choose_car(self):
        pass
