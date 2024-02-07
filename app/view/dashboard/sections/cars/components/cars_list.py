import customtkinter as ctk
from .....global_style import GStyle
from .....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image
from ......core.Data_Handler.car import getcars


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
        button = ctk.CTkButton(head, text='add', command=self.addcar ,fg_color="#03d084", hover_color="#00c87e", corner_radius=7, height=5, width=50).grid(
            row=0, column=2, rowspan=1, sticky='news', pady=5, padx=(0, 3))
        body = ProCTkScrollableFrame(self, fg_color=GStyle.bg)
        body.grid(row=3, column=1, sticky='news')
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=10)
        body.columnconfigure(2, weight=1)
        body.columnconfigure(3, weight=10)
        body.columnconfigure(4, weight=1)
        cars = self.getcars
        i = 0
        for c in cars.values():
            car = Carinfo(body, c)
            """show cars"""
            car.grid(row=int(i / 2), column=(i % 2) * 2 + 1, sticky='news', pady=20)
            i += 1

    @property
    def getcars(self):
        """call database for cars"""
        return getcars()

    def addcar(self):
        self.manager.switch("AddCar")


class Carinfo(ctk.CTkFrame):
    def __init__(self, master, car_data):
        super().__init__(
            master,
            fg_color=GStyle.frames_bg,
            bg_color=GStyle.frames_bg
        )
        self.data = car_data.to_dict()
        self.master = master

        brand = ctk.CTkLabel(self, text="Car info", text_color=GStyle.frames_font_color, font=(GStyle.font_family, GStyle.meduim))
        brand.pack()
        brand = ctk.CTkLabel(self, text=self.data["brand"], text_color=GStyle.frames_font_color, font=(GStyle.font_family, GStyle.meduim))
        brand.pack()
        brand = ctk.CTkLabel(self, text=self.data["matricule"], text_color=GStyle.frames_font_color, font=(GStyle.font_family, GStyle.meduim))
        brand.pack()
        brand = ctk.CTkLabel(self, text=f"{self.data['rent_price']} {self.data['currency']}", text_color=GStyle.frames_font_color, font=(GStyle.font_family, GStyle.meduim))
        brand.pack()
        brand = ctk.CTkLabel(self, text="+" if self.data["availability"] else '-', text_color= "green" if self.data["availability"] else 'red', font=(GStyle.font_family, GStyle.meduim))
        brand.pack()
        but = ctk.CTkButton(self, text='Selecte', text_color=GStyle.frames_font_color, font=(GStyle.font_family, GStyle.meduim), fg_color=GStyle.frames_bg, bg_color=GStyle.frames_bg, hover_color=GStyle.buttons_hover_color)
        but.pack()

    def choose_car(self):
        pass
