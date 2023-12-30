import customtkinter as ctk
import tkinter
import tkinter.messagebox
from .global_style import GStyle
from app.core.Data_Handler.GetHomeData import getStatistic
from .components.sidebar import Sidebar
from .components.header import Header
from .components.home import Home
from .components.users_section import UsersSection
from .components.customers_section import CustomersSection
from .components.revenues_section import RevenuesSection
from .components.reservation_section import ReservationsSection
from .components.cars_section import CarsSection

Sections = {
    "Home": Home,
    "UsersSection": UsersSection,
    "CustomersSection": CustomersSection,
    "RevenuesSection": RevenuesSection,
    "ReservationsSection": ReservationsSection,
    "CarsSection": CarsSection,
}


class DashboardFrame(ctk.CTkFrame):
    frames = {}

    def __init__(self, master, userInfo):
        super().__init__(master)

        self.userInfo = userInfo
        self.on_logout = master.show_login
        self.refresh = master.show_dashboard

        """split the width"""
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=50)

        """split the height"""
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=100)

        """create wigets"""
        self.create_sidebar()
        self.create_header()
        self.create_main()

    def create_sidebar(self):
        """create sidebar wigets"""
        self.frames["Sidebar"] = Sidebar(self)
        self.frames["Sidebar"].grid(
            column=0, row=0, rowspan=2, sticky="news")

    def create_header(self):
        """create header wigets"""
        self.frames["Header"] = Header(self)
        self.frames["Header"].grid(column=1, row=0, sticky="news")

    def create_main(self, section=""):
        """this will make switch mode more dynamic"""
        if section == "":
            section = self.frames["current"].__class__.__name__ if "current" in self.frames else "Home"
        """create main widgets"""
        self.frames[section] = Sections[section](self)

        """delete the old widget"""
        if "current" in self.frames:
            attr = "{}_label".format(self.frames["current\
"].__class__.__name__.lower())
            if hasattr(self.frames["Sidebar"], attr):
                getattr(self.frames["Sidebar"], attr
                        ).configure(fg_color=GStyle.sidebar_bg,
                                    bg_color=GStyle.sidebar_bg)

            self.frames["current"].destroy()
            del self.frames["current"]
        self.frames["current"] = self.frames[section]

        """show the new widget"""
        self.frames[section].grid(column=1, row=1, sticky="news")
        attr = "{}_label".format(section.lower())
        if hasattr(self.frames["Sidebar"], attr):
            nav = getattr(self.frames["Sidebar"], attr
                          )
            nav.configure(fg_color=GStyle.buttons_hover_color,
                          bg_color=GStyle.sidebar_bg)
        self.frames["Header"].title.configure(text=section)
