from models.base_model import BaseModel
from models.car import Car
from models.customer import Customer
from models.reservation import Reservation

from models import storage

customer = Customer(full_name="badr eddine",
                    phone="0606060606",
                    card_id="ia14856",
                    driver_id="168214",)
customer.save()

car = Car(brand="dacia",
          image="path",
          matricule="2541-a-465165",
          rent_price=200,)
car.save()
