import customtkinter as ctk
from .....global_style import GStyle
from .....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image
from ......core.Data_Handler.car import CreatCar


class AddCar(ctk.CTkFrame):
    def __init__(self, master, manager):
        super().__init__(
            master,
            fg_color=GStyle.bg,
            bg_color=GStyle.bg
        )
        self.manager = manager
        self.brand = ctk.CTkEntry(
            self,
            fg_color=GStyle.frames_bg,
            text_color=GStyle.frames_font_color,
            placeholder_text_color=GStyle.frames_font_color,
            placeholder_text="brand of car",
            border_width=0,
            font=(GStyle.font_family,
                  GStyle.small)
        )
        self.brand.pack(pady=(40, 5))

        self.matricule = ctk.CTkEntry(
            self,
            fg_color=GStyle.frames_bg,
            text_color=GStyle.frames_font_color,
            placeholder_text_color=GStyle.frames_font_color,
            placeholder_text="matricule of car",
            border_width=0,
            font=(GStyle.font_family,
                  GStyle.small)
        )
        self.matricule.pack(pady=5)

        self.rent_price = ctk.CTkEntry(
            self,
            fg_color=GStyle.frames_bg,
            text_color=GStyle.frames_font_color,
            placeholder_text_color=GStyle.frames_font_color,
            placeholder_text="rent price of car",
            border_width=0,
            font=(GStyle.font_family,
                  GStyle.small)
        )
        self.rent_price.pack(pady=5)

        self.currency = ctk.CTkOptionMenu(self, values=['MAD', 'USD', 'EURO'])
        self.currency.pack(pady=5)

        self.availability = ctk.CTkCheckBox(self, text='availabile')
        self.availability.pack(pady=5)

        but = ctk.CTkButton(self, text='add', command=self.addcar ,fg_color="#03d084", hover_color="#00c87e", corner_radius=7).pack(pady=(10,5))
        back = ctk.CTkButton(self, text='back', command=self.back ,fg_color=GStyle.buttons_bg, hover_color=GStyle.buttons_hover_color, corner_radius=7).pack(pady=5)

    def addcar(self):
        default = {
            'brand': self.brand.get(),
            'car_image': 'null',
            'currency': self.currency.get(),
            'matricule': self.matricule.get(),
            'rent_price': self.rent_price.get(),
            'availability': self.availability.get(),
        }
        CreatCar(default)

    def back(self):
        self.manager.switch('CarsList')
