# from models.base_model import BaseModel
from models.car import Car
from models.customer import Customer
from models.reservation import Reservation
from models.user import User
from models.revenue import Revenue
from datetime import datetime, timedelta

from models import storage

# user = User(userName="Moha",
#             password="mohhhhhhhh",
#             fullName="Mohamed ben jamaa",
#             role="adman",
#             secretKey="siiMO")
# user.save()

# car = Car(brand="dacia",
#           image="path",
#           matricule="2541-a-465165",
#           rent_price=200,
#           currency="MAD")
# car.save()

# cus = Customer(full_name="omar Ouydir",
# phone="0756300302")
# cus.save()



def create_res(**args):
    timenow = str(datetime.now())
    revenues = storage.all(Revenue)
    list_rev = list(revenues.values())
    rev_id = ""
    if list_rev == [] or not timenow.startswith(list_rev[0].time):
        print(timenow[:7])
        rev = Revenue(time = timenow[:7],
                        month = timenow.split("-")[1],
                        year = timenow.split("-")[0],
                        )
        rev_id = rev.id
        rev.save()
    else:
        rev = list_rev[0]
        rev_id = rev.id

    res = Reservation(**args)
    # setattr(res, "revenue_id", rev_id)
    res.revenue_id = rev_id
    res.save()
    rev.amount += res.amount
    rev.save()

args = {"customer_id": "cd72b533-35b4-4bae-ac3d-da2fdd9c21d4",
"car_id": "cc00b4a7-b18e-44f9-95a1-1c3656966f11",
"confirmed": True,
"amount": 1400,
"start_date": datetime.now(),
"end_date": datetime.now() + timedelta(weeks=2)}

# create_res(**args)

objs = {}

# users = storage.all(Reservation)
# for one in users:
#     objs[one] = users[one].to_dict()

users = storage.all(Reservation)
for one in users:
    objs[f"the Revenue of [{one}]"] = users[one].revenue.to_dict()




print(objs)
