import customtkinter as ctk
from PIL import Image
import tkinter
import tkinter.messagebox
from ..global_style import GStyle
from PIL import Image


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.sidebar_bg,
            bg_color=GStyle.sidebar_bg,
        )
        self.master = master
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.rowconfigure(0, weight=5)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(4, weight=1)
        # self.rowconfigure(5, weight=1)
        # self.rowconfigure(6, weight=1)
        # self.rowconfigure(7, weight=10)
        # self.rowconfigure(8, weight=10)

        """create an image object"""
        # image = ctk.CTkImage(light_image=Image.open(
        #     "/home/omarnem/omar/CMS/resources/icons/CMSlogo.png"), size=(100, 100))

        # """add the image to a wiget"""
        # name_label = ctk.CTkLabel(
        #     self, text="", image=image)
        # name_label.grid(row=0, column=0)

        """home"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/home.png"), size=(30, 30))
        self.home_label = ctk.CTkButton(self,
                                        text="",
                                        image=icon,
                                        width=10,
                                        anchor="center",
                                        font=(GStyle.font_family,
                                              GStyle.meduim),
                                        text_color=GStyle.sidebar_font_color,
                                        bg_color=GStyle.sidebar_bg,
                                        fg_color=GStyle.sidebar_bg,
                                        hover_color=GStyle.header_bg,
                                        corner_radius=6,
                                        command=self.home_section
                                        )

        # self.home_label.grid(row=1, column=0, sticky="new")
        self.home_label.pack(pady=5)

        """cars"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/cars.png"), size=(30, 30))
        self.carssection_label = ctk.CTkButton(self,
                                               text="",
                                               image=icon,
                                               width=10,
                                               anchor="w",
                                               font=(GStyle.font_family,
                                                     GStyle.meduim),
                                               text_color=GStyle.sidebar_font_color,
                                               bg_color=GStyle.sidebar_bg,
                                               fg_color=GStyle.sidebar_bg,
                                               hover_color=GStyle.header_bg,
                                               corner_radius=6,
                                               command=self.cars_section)

        # self.carssection_label.grid(row=2, column=0, sticky="new")
        self.carssection_label.pack(pady=5)

        """reservations"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/reservations.png"), size=(30, 30))
        self.reservationssection_label = ctk.CTkButton(self,
                                                       image=icon,
                                                       text="",
                                                       width=10,
                                                       anchor="w",
                                                       font=(GStyle.font_family,
                                                             GStyle.meduim),
                                                       text_color=GStyle.sidebar_font_color,
                                                       bg_color=GStyle.sidebar_bg,
                                                       fg_color=GStyle.sidebar_bg,
                                                       hover_color=GStyle.header_bg,
                                                       corner_radius=6,
                                                       command=self.reservations_section)

        # self.reservationssection_label.grid(row=3, column=0, sticky="new")
        self.reservationssection_label.pack(pady=5)

        """revenue"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/revenues.png"), size=(30, 30))
        self.revenuessection_label = ctk.CTkButton(self,
                                                   image=icon,
                                                   text="",
                                                   anchor="w",
                                                   width=10,
                                                   font=(GStyle.font_family,
                                                         GStyle.meduim),
                                                   text_color=GStyle.sidebar_font_color,
                                                   bg_color=GStyle.sidebar_bg,
                                                   fg_color=GStyle.sidebar_bg,
                                                   hover_color=GStyle.header_bg,
                                                   corner_radius=6,
                                                   command=self.revenues_section)

        # self.revenuessection_label.grid(row=4, column=0, sticky="new")
        self.revenuessection_label.pack(pady=5)

        """customers"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/customers.png"), size=(30, 30))
        self.customerssection_label = ctk.CTkButton(self,
                                                    image=icon,
                                                    text="",
                                                    anchor="w",
                                                    width=10,
                                                    font=(GStyle.font_family,
                                                          GStyle.meduim),
                                                    text_color=GStyle.sidebar_font_color,
                                                    bg_color=GStyle.sidebar_bg,
                                                    fg_color=GStyle.sidebar_bg,
                                                    hover_color=GStyle.header_bg,
                                                    corner_radius=6,
                                                    command=self.customers_section)

        # self.customerssection_label.grid(row=5, column=0, sticky="new")
        self.customerssection_label.pack(pady=5)

        """users"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/users.png"), size=(30, 30))
        self.userssection_label = ctk.CTkButton(self,
                                                image=icon,
                                                text="",
                                                anchor="w",
                                                width=10,
                                                font=(GStyle.font_family,
                                                      GStyle.meduim),
                                                text_color=GStyle.sidebar_font_color,
                                                bg_color=GStyle.sidebar_bg,
                                                fg_color=GStyle.sidebar_bg,
                                                hover_color=GStyle.header_bg,
                                                corner_radius=6,
                                                command=self.users_section)

        # self.userssection_label.grid(row=6, column=0, sticky="new")
        self.userssection_label.pack(pady=5)

        """logout button"""
        icon = ctk.CTkImage(light_image=Image.open(
            "resources/icons/sidebar/logout.png"), size=(30, 30))
        self.userssection_label = ctk.CTkButton(self,
                                                image=icon,
                                                text="",
                                                anchor="w",
                                                width=10,
                                                font=(GStyle.font_family,
                                                      GStyle.meduim),
                                                text_color=GStyle.sidebar_font_color,
                                                bg_color=GStyle.sidebar_bg,
                                                fg_color=GStyle.sidebar_bg,
                                                hover_color=GStyle.header_bg,
                                                corner_radius=6,
                                                command=master.on_logout)

        # self.userssection_label.grid(row=6, column=0, sticky="new")
        self.userssection_label.pack(pady=5)

        """create a border right"""
        # ctk.CTkFrame(self, width=1, border_color=GStyle.login_bg, border_width=1,
        #              fg_color=GStyle.login_bg,
        #              bg_color=GStyle.login_bg).grid(
        #     row=0, column=1, rowspan=9, sticky="news")

    def home_section(self):
        self.master.create_main("Home")

    def users_section(self):
        self.master.create_main("UsersSection")

    def customers_section(self):
        self.master.create_main("CustomersSection")

    def cars_section(self):
        self.master.create_main("CarsSection")

    def revenues_section(self):
        self.master.create_main("RevenuesSection")

    def reservations_section(self):
        self.master.create_main("ReservationsSection")
