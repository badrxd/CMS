from models import storage
from models.car import Car
from models.customer import Customer
from models.reservation import Reservation
from models.revenue import Revenue
from sqlalchemy import func


def getStatistic():
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
    print(data)
    # return data


# getStatic()
