
from models.car import Car
from models.settings import Settings
from models import storage
from app.core.image_handler import ImageName, SaveImage
from models import storage


def CreatCar(args):
    car = None
    images_path = None
    session = storage.session
    try:
        # images_path = session.query(Settings).first()
        # if images_path is None or type(images_path) is not Settings :
        #     raise ValueError(f"Problem in database")
        images_path = 'D:\\crms\\images'

        car = Car(**args)

        # name = ImageName(car.id, args.get('car_image'))
        # save = SaveImage(args.get('car_image'), section='cars',
        #                  images_path=images_path, name=name)

        # if save.get('error'):
        #     raise IOError(save.get('message'))

        # car.update({'car_image': name})

        car.save()

        return ({'error': False})
    except (IOError, OSError, ValueError) as e:
        return {'error': True, 'message': e}
    except Exception as e:
        print(e)


def updateCar(args, id):
    car = storage.getById(Car, id=id)

    try:
        if car is None:
            raise ValueError(f"Customer with provided id not found.")

        if hasattr(args, 'car_image'):
            pass

        for key, value in args.items():
            if key != 'car_image' and key != 'id':
                setattr(car, key, value)
        # car.save()
    except Exception:
        pass

def getcars():
    """
    get all cars
    """
    return storage.all(Car)
