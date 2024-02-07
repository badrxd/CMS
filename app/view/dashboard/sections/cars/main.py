import customtkinter as ctk
from ....global_style import GStyle
from ....libraries.professionalCTk import ProCTkTable, ProCTkScrollableFrame
from PIL import Image
from .components.cars_list import CarsList
from .components.single_car import SingleCar
from .components.add_car import AddCar


class CarsSection:
    components = {
        "CarsList": CarsList,
        "SingleCar": SingleCar,
        "AddCar": AddCar
    }
    current: str
    frames: dict

    def __init__(self, master):
        self.frames = {}
        self.current = "CarsList"
        self.master = master
        self.create()


    def create(self):
        self.frames[self.current] = CarsSection.components[self.current](
            self.master, self)

    def display(self):
        self.frames[self.current].grid(column=1, row=1, sticky="news")

    def destroy(self):
        self.frames[self.current].destroy()

    def switch(self, frame):
        self.destroy()
        self.current = frame
        self.create()
        self.display()
