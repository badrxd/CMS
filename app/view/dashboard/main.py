import customtkinter as ctk
import tkinter
import tkinter.messagebox
from ..global_style import GStyle
from app.core.Data_Handler.GetHomeData import getStatistic
from .sidebar import Sidebar
from .header import Header
from .sections.home.home import Home
from .sections.users.users_section import UsersSection
from .sections.customers.customers_section import CustomersSection
from .sections.revenues.revenues_section import RevenuesSection
from .sections.reservations.reservation_section import ReservationsSection
from .sections.cars.cars_section import CarsSection

Sections = {
    "Home": Home,
    "UsersSection": UsersSection,
    "CustomersSection": CustomersSection,
    "RevenuesSection": RevenuesSection,
    "ReservationsSection": ReservationsSection,
    "CarsSection": CarsSection,
}


class Main:
    frames = {}

    def __init__(self, master):
        self.master = master
        self.create_main("")

    def create_main(self, section=""):
        """this will make switch mode more dynamic"""
        if section == "":
            section = self.frames["current"].__class__.__name__ if "current" in self.frames else "Home"
        """create main widgets"""
        self.frames[section] = Sections[section](self.master)

        """delete the old widget"""
        if "current" in self.frames:
            attr = "{}_label".format(self.frames["current\
"].__class__.__name__.lower())
            if hasattr(self.master.frames["Sidebar"], attr):
                getattr(self.master.frames["Sidebar"], attr
                        ).configure(fg_color=GStyle.sidebar_bg,
                                    bg_color=GStyle.sidebar_bg)

            self.frames["current"].destroy()
            del self.frames["current"]
        self.frames["current"] = self.frames[section]

        """show the new widget"""
        self.frames[section].grid(column=1, row=1, sticky="news")
        self.loading()
        attr = "{}_label".format(section.lower())
        if hasattr(self.master.frames["Sidebar"], attr):
            nav = getattr(self.master.frames["Sidebar"], attr
                          )
            nav.configure(fg_color=GStyle.buttons_hover_color,
                          bg_color=GStyle.sidebar_bg)
        self.master.frames["Header"].title.configure(text=section)

    def loading(self):
        lt = ctk.CTkFrame(
            self.master.frames["Header"], fg_color=GStyle.header_bg, bg_color=GStyle.header_bg, height=50, width=300)
        lt.grid(row=0, column=0, rowspan=2)
        self.master.after(2000, lt.destroy)
        l = ctk.CTkFrame(self.master, fg_color=GStyle.bg, bg_color=GStyle.bg)
        l.grid(column=1, row=1, sticky="news")
        label = ctk.CTkLabel(l, text="LOADING...", font=(GStyle.font_family, GStyle.xl, "bold"),
                             text_color=GStyle.frames_font_color, bg_color=GStyle.bg, fg_color=GStyle.bg).pack(pady=100)
        self.master.after(2000, l.destroy)
