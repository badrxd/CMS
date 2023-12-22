from models.car import Car
from models import storage
from models.customer import Customer
from models.reservation import Reservation
from models.user import User
from models.revenue import Revenue
from datetime import datetime, timedelta
from threading import Thread


def getTopCustomers():
    """methode that return the top 4 Customers
    based in number of Reservations"""
    TopCustomers = []
    session = storage.session()
    customers = session.query(Customer).order_by(
        Customer.num_of_res.desc()).limit(4)
    for cus in customers:
        data = cus.to_dict()
        TopCustomers.append(data)
    print(TopCustomers)
    return TopCustomers


getTopCustomers()
#############################################################################################
# from models import storage

# user = User(userName="omar",
#             password="omarnem",
#             fullName="omar idhmaid",
#             role="adman",
#             secretKey="lhaj")
# user.save()

# customer = Customer(full_name="badr eddine ouydi",
#                     phone="0606060606",
#                     card_id="ia262626",
#                     driver_id="262626",
#                     card_id_image="null",
#                     driver_id_image="null",
#                     )
# customer.save()

# car = Car(brand="Mitsubishi",
#           image="null",
#           matricule="76-a-236584",
#           rent_price="200",
#           currency="MAD",
#           )
# car.save()

#############################################################################################


# def create_res(args, customer):

#     timenow = str(datetime.now())
#     revenues = storage.all(Revenue)
#     list_rev = list(revenues.values())
#     rev_id = ""
#     if list_rev == [] or not timenow.startswith(list_rev[0].time):

#         rev = Revenue(
#             time=timenow[:7],
#             month=timenow.split("-")[1],
#             year=timenow.split("-")[0],
#         )
#         rev_id = rev.id
#         rev.amount = 0
#         storage.new(rev)
#     else:
#         rev = list_rev[0]
#         rev_id = rev.id

#     res = Reservation(**args)
#     res.revenue_id = rev_id
#     storage.new(res)
#     rev.amount += res.amount

#     customer.num_of_res += 1
#     customer.spending += res.amount
#     storage.save()


# args = {"customer_id": "c8a16207-bd8d-42cd-ae81-4b03c24b939f",
#         "car_id": "b52596b9-4e59-4d6f-9b01-d9b400294e7c",
#         "confirmed": True,
#         "amount": 1400,
#         "start_date": datetime.now(),
#         "end_date": datetime.now() + timedelta(weeks=2)}

# session = storage.session()
# customer = session.query(Customer).filter(
#     Customer.id == "c8a16207-bd8d-42cd-ae81-4b03c24b939f").first()

# print(customer.to_dict())
# create_res(args, customer)

#############################################################################################

# objs = {}


# users = storage.all(Reservation)
# for one in users:
#     objs[f"the Revenue of [{one}]"] = users[one].revenue.to_dict()


# print(objs)


#############################################################################################

# from sqlalchemy import func
# from models.car import Car
# from models.user import User
# from models import storage
# from models.customer import Customer
# from models.reservation import Reservation
# from models.revenue import Revenue


# def getStatic():
#     print('yes')
#     session = storage.session()
#     data = {'cars': 0, 'reservations': 0,
#             'customers': 0, 'mounth_income': 0}


#     data['cars'] = session.query(func.count(
#         Car.id)).filter(Car.availability == True).scalar()

#     data['reservations'] = session.query(func.count(Reservation.id)).scalar()

#     data['customers'] = session.query(func.count(Customer.id)).scalar()


#     lastRevenue = session.query(
#         Revenue).order_by(Revenue.created_at.desc()).first()

#     data['mounth_income'] = 0 if lastRevenue == None else lastRevenue['amount']
#     # return data
#     print(data)

#############################################################################################
