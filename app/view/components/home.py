import customtkinter as ctk
import tkinter
import tkinter.messagebox
from ..global_style import GStyle
from ..libraries.professionalCTk import ProCTkTable
from PIL import Image


class Home(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color=GStyle.bg,
            bg_color=GStyle.bg
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        boxes = ctk.CTkScrollableFrame(
            self, fg_color=GStyle.bg, corner_radius=0, scrollbar_button_color=GStyle.header_bg, orientation="horizontal")
        boxes.grid(row=0, column=0, sticky="news")

        self.short_info(boxes)

        tables = ctk.CTkScrollableFrame(
            self, fg_color=GStyle.bg, corner_radius=0, scrollbar_button_color=GStyle.header_bg)
        tables.grid(row=1, column=0, sticky="news")

        self.create_tables(tables)

    def create_box(self, master, **params):
        box = ctk.CTkFrame(master, fg_color=GStyle.frames_bg,
                           border_color=GStyle.frames_border, border_width=1)
        box.grid(row=params["rpos"],
                 column=params["cpos"], sticky="news", padx=50)

        box.columnconfigure(0, weight=1)
        box.rowconfigure(0, weight=1)
        box.rowconfigure(1, weight=1)
        box.rowconfigure(2, weight=1)

        """create an image object"""
        image = ctk.CTkImage(light_image=Image.open(
            f"/home/omarnem/omar/CMS/resources/icons/{params['title']}.png"), size=(200, 200))

        """add the image to a wiget"""
        name_label = ctk.CTkLabel(
            box, text="", image=image)
        name_label.grid(row=0, column=0, padx=5)

        title = ctk.CTkLabel(box, text=params["title"], font=(
            GStyle.frames_font_color, GStyle.large, "bold"), text_color=GStyle.font_color)
        title.grid(row=1, column=0)
        value = ctk.CTkLabel(
            box, text=params["value"], text_color=GStyle.font_color, font=(
                GStyle.frames_font_color, GStyle.small))
        value.grid(row=2, column=0)

    def short_info(self, master):
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=2)
        master.rowconfigure(2, weight=1)
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=3)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=3)
        master.columnconfigure(4, weight=1)
        master.columnconfigure(5, weight=3)
        master.columnconfigure(6, weight=1)
        master.columnconfigure(7, weight=3)
        master.columnconfigure(8, weight=1)

        self.create_box(master, rpos=1, cpos=1,
                        title="income", value="14000MAD")
        self.create_box(master, rpos=1, cpos=3,
                        title="customers", value="39")
        self.create_box(master, rpos=1, cpos=5,
                        title="reservations", value="64")
        self.create_box(master, rpos=1, cpos=7,
                        title="cars", value="23")

    def create_tables(self, master):
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=20)
        master.columnconfigure(2, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=6)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=6)
        master.rowconfigure(4, weight=1)

        ProCTkTable(
            master,
            rpos=1,
            cpos=1,
            pady=(40, 0),
            title="Top Costumers",
            title_color=GStyle.font_color,
            text_color=GStyle.font_color,
            head_fg_color=GStyle.header_bg,
            head_bg_color=GStyle.header_bg,
            head_text_color=GStyle.head_font_color,
            transparent=GStyle.bg,
            border_row=True,
            data=self.json_to_table()
        )
        ProCTkTable(
            master,
            rpos=3,
            cpos=1,
            pady=40,
            text_color=GStyle.font_color,
            title_color=GStyle.font_color,
            head_fg_color=GStyle.header_bg,
            head_bg_color=GStyle.header_bg,
            head_text_color=GStyle.head_font_color,
            border_row=True,
            title="Last Reservations", transparent=GStyle.bg,
            data=self.json_to_table()
        )

    def json_to_table(self):
        json_data = [
            {
                "name": "Laila Boutfilit",
                "spend": 4500,
                "number of reservatons": 7,
                "phone number": "0754682036"
            },
            {
                "name": "brahim Boutrgin",
                "spend": 5180,
                "number of reservatons": 4,
                "phone number": "0754682036"
            },
            {
                "name": "Omar Skoumi",
                "spend": 3200,
                "number of reservatons": 4,
                "phone number": "0754682036"
            },
            {
                "name": "Badr Matnit",
                "spend": 3500,
                "number of reservatons": 3,
                "phone number": "0754682036"
            }
        ]
        # TODO: call fuction that get the tables data
        table = []
        row = []
        for header in json_data[0]:
            row.append(header)
        table.append(row)
        for column in json_data:
            table.append(list(column.values()))
        return table
