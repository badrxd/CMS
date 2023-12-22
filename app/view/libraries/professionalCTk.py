from typing import Literal, Optional, Tuple, Union
from typing_extensions import Literal
import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont


class ProCTkTable:
    """
        master: (obj)
            the parent wiget that include the table
        transparent: (str)
            the background color of the wiget
            parent wiget
        rpos: (int)
            row position as default is 0
        cpos: (int)
            column position as default is 0
        padx: (int / tuple)
            padding x (padding-left, padding-right)
        pady: (int / tuple)
            padding y (padding-top, padding-bottom)
        title: (str)
            the title of table as defaul id empty
        data: (matrix: list[list[]])
            table data matrix
        title_color: (str)
            color of the title
        title_font: (tuple)
            font style size family...
        radius: (int)
            border-radius
        head_fg_color: (str)
            head foreground color
        head_bg_color: (str)
            head background color
        fg_color: (str)
            head foreground color
        bg_color: (str)
            head background color
        border_row: (bool)
            border row bottom
        global_border: (tuple)
            (border_color, border_size)
        text_color: (str)
            text color
        text_font: (tuple)
            font style size family...
    """
    data = []
    other = {}

    def __init__(self,
                 master,
                 transparent="transparent",
                 rpos=0,
                 cpos=0,
                 padx=0,
                 pady=0,
                 title="",
                 data=[],
                 **other):

        self.data = data
        self.other = other

        box = ctk.CTkFrame(master, fg_color=transparent)
        box.grid(row=rpos, column=cpos, padx=padx, pady=pady, sticky="news")

        box.columnconfigure(0, weight=1)
        box.rowconfigure(0, weight=10)
        box.rowconfigure(1, weight=10)
        title = ctk.CTkLabel(
            box, text=title, anchor="sw",
            text_color=other["title_color"] if "title_color" in other else "black",
            font=other["title_font"] if "title_font" in other else ("", 16, "bold"))
        title.grid(row=0, column=0, padx=20, sticky="news")

        self.create_rows(box, rpos=1, cpos=0,
                         data=self.data, transparent=transparent)

    def create_rows(self, master, **params):
        table = ctk.CTkFrame(
            master,
            fg_color=params["transparent"],
            bg_color=params["transparent"],
        )
        table.grid(row=1, column=0, sticky="news")

        table.columnconfigure(0, weight=1)
        row_number = len(params["data"])
        for i in range(row_number):
            table.rowconfigure(i, weight=1)
            if i == 0:
                r = ctk.CTkFrame(table, width=50, height=20,
                                 corner_radius=self.other["radius"] if "radius" in self.other else 0,
                                 fg_color=self.other["head_fg_color"] if "head_fg_color" in self.other else "gray",
                                 bg_color=self.other["head_bg_color"] if "head_bg_color" in self.other else "gray"
                                 )
            else:
                r = ctk.CTkFrame(table, width=50, height=10,
                                 corner_radius=self.other["radius"] if "radius" in self.other else 0,
                                 fg_color=self.other["fg_color"] if "fg_color" in self.other else "transparent",
                                 bg_color=self.other["bg_color"] if "bg_color" in self.other else "transparent",
                                 )
            r.grid(row=i, column=0, sticky="news")

            column_num = len(params["data"][i])

            for n in range(column_num):
                r.columnconfigure(n, weight=1)
            r.rowconfigure(0, weight=1)
            if "border_row" in self.other and self.other["border_row"]:
                r.rowconfigure(1, weight=1)
                ctk.CTkFrame(r, corner_radius=0, border_color="black",
                             bg_color=params["transparent"], border_width=1, height=1).grid(
                    row=1, columnspan=column_num, sticky="ews")
            for j in range(column_num):
                text_color = self.other["text_color"] if "text_color" in self.other else "black"
                if i == 0:
                    text_color = self.other["head_text_color"] if "head_text_color" in self.other else "black"
                l = ctk.CTkLabel(
                    r, text=params["data"][i][j], width=100,
                    font=self.other["font"] if "font" in self.other else (
                        "", 14),
                    text_color=text_color,
                    wraplength=100,
                    anchor=self.other["text_anchor"] if "text_anchor" in self.other else "w")
                l.grid(row=0, column=j, padx=20,
                       sticky=self.other["text_sticky"] if "text_sticky" in self.other else "ew")


class ProCTkScrollableFrame(ctk.CTkScrollableFrame):

    """this class adds more cutomizing to Scrollable frame CTk class"""

    def __init__(self,
                 master: any,
                 width: int = 200,
                 height: int = 200,
                 corner_radius: int | str | None = None,
                 border_width: int | str | None = None,
                 bg_color: str | Tuple[str, str] = "transparent",
                 fg_color: str | Tuple[str, str] | None = None,
                 border_color: str | Tuple[str, str] | None = None,
                 scrollbar_fg_color: str | Tuple[str, str] | None = None,
                 scrollbar_size: int = 10,
                 scrollbar_hover_size: int = 10,
                 scrollbar_button_color: str | Tuple[str, str] | None = None,
                 scrollbar_button_hover_color: str | Tuple[str,
                                                           str] | None = None,
                 label_fg_color: str | Tuple[str, str] | None = None,
                 label_text_color: str | Tuple[str, str] | None = None,
                 label_text: str = "",
                 label_font: tuple | CTkFont | None = None,
                 label_anchor: str = "center",
                 orientation: Literal['vertical',
                                      'horizontal'] = "vertical"):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, scrollbar_fg_color,
                         scrollbar_button_color, scrollbar_button_hover_color, label_fg_color, label_text_color, label_text, label_font, label_anchor, orientation)
        self.scrollbar_hover_size = scrollbar_hover_size

        if orientation == "vertical":
            self._scrollbar.configure(
                width=scrollbar_size, command=self._yviewConfigure)
        elif orientation == "horizontal":
            self._scrollbar.configure(
                height=scrollbar_size, command=self._xviewConfigure)

    def _yviewConfigure(self, *args):
        self._parent_canvas.yview(*args)

    def _xviewConfigure(self, *args):
        self._parent_canvas.xview(*args)
