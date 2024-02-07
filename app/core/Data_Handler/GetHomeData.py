"""this file for handling the logic of file home.py"""
from models import storage
from models.car import Car
from models.customer import Customer
from models.reservation import Reservation
from models.revenue import Revenue
from sqlalchemy import func


def getStatistic():
    """methode that return the lenght of cars ,
    customer reservations, and the last mouth revenue"""

    session = storage.session()
    data = {'cars': 0, 'reservations': 0,
            'customers': 0, 'mounth_income': 0}

    data['cars'] = session.query(func.count(
        Car.id)).filter(Car.availability == True).scalar()

    data['reservations'] = session.query(func.count(Reservation.id)).scalar()

    data['customers'] = session.query(func.count(Customer.id)).scalar()

    lastRevenue = session.query(
        Revenue).order_by(Revenue.created_at.desc()).first()

    data['mounth_income'] = 0 if lastRevenue == None else lastRevenue['amount']

    return data


def getLastReservations():
    """methode that returns the last 4 reservations"""

    LastReservations = []
    session = storage.session()
    obj = {'carName': '', 'matricule': '', 'carImage': '', 'carId': '',
           'customerId': '', 'customerName': '', 'revAmount': 0, 'revDate': '', 'status': ''}

    Reservations = session.query(Reservation).order_by(
        Reservation.created_at.desc()).limit(4)
    for rev in Reservations:
        data = obj
        customer = storage.getById(Customer, rev.customer_id)
        car = storage.getById(Car, rev.car_id)

        data['carName'] = car.brand
        data['matricule'] = car.matricule
        data['carImage'] = car.image
        data['carId'] = car.id
        data['customerId'] = customer.id
        data['customerName'] = customer.full_name
        data['revAmount'] = rev.amount
        data['status'] = rev.status
        data['revDate'] = rev.created_at
        LastReservations.append(data)
    return LastReservations


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
