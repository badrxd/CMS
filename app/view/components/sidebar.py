import customtkinter as ctk
from PIL import Image
import tkinter
import tkinter.messagebox
from ..global_style import GStyle


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.sidebar_bg,
            bg_color=GStyle.sidebar_bg
        )
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=2)

        """create an image object"""
        image = ctk.CTkImage(light_image=Image.open(
            "/home/omarnem/omar/CMS/resources/icons/CMSlogo.png"), size=(100, 100))

        """add the image to a wiget"""
        name_label = ctk.CTkLabel(
            self, text="", image=image)
        # name_label.pack(pady=10, padx=40)
        name_label.grid(row=0, column=0)

        """home"""
        home_label = ctk.CTkButton(
            self, text="home", font=(GStyle.font_family, 16), text_color="white", bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.bg, corner_radius=0)
        # home_label.pack(pady=20, padx=0)
        home_label.grid(row=1, column=0, sticky="news")

        """cars"""
        cars_label = ctk.CTkButton(
            self, text="cars", font=(GStyle.font_family, 16), text_color="white", bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.bg, corner_radius=0)
        # cars_label.pack(pady=20, padx=0)
        cars_label.grid(row=2, column=0, sticky="news")

        """reservations"""
        res_label = ctk.CTkButton(
            self, text="reservations", font=(GStyle.font_family, 16), text_color="white", bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.bg, corner_radius=0)
        # res_label.pack(pady=20, padx=0)
        res_label.grid(row=3, column=0, sticky="news")

        """revenue"""
        res_label = ctk.CTkButton(
            self, text="revenue", font=(GStyle.font_family, 16), text_color="white", bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.bg, corner_radius=0)
        # res_label.pack(pady=20, padx=0)
        res_label.grid(row=4, column=0, sticky="news")
        """customers"""
        res_label = ctk.CTkButton(
            self, text="customers", font=(GStyle.font_family, 16), text_color="white", bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.bg, corner_radius=0)
        # res_label.pack(pady=20, padx=0)
        res_label.grid(row=5, column=0, sticky="news")

        """users"""
        res_label = ctk.CTkButton(
            self, text="users", font=(GStyle.font_family, 16), text_color="white", bg_color=GStyle.sidebar_bg, fg_color=GStyle.sidebar_bg, hover_color=GStyle.bg, corner_radius=0)
        # res_label.pack(pady=10, padx=0)
        res_label.grid(row=6, column=0, sticky="news")

        logout_button = ctk.CTkButton(
            self, text="Logout", width=50, fg_color=GStyle.buttons_bg, hover_color=GStyle.buttons_hover_color, command=master.on_logout)
        logout_button.place(relx=0.5, rely=0.95, anchor="s")
