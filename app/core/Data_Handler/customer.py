from models.customer import Customer
from models.settings import Settings
from models import storage
from app.core.image_handler import ImageName, SaveImage
from models import storage


def CreatCustomer(args, images):
    """ """
    customer = None
    images_path = None
    session = storage.session()
    try:
        if len(images) > 0:
            for i in range(len(images)):
                key = list(images[i].keys())[0]
                path = images[i].get(key)
                if path != '':
                    args.update({key: ImageName(key, path)})

        customer = Customer(**args)
        # images_path = session.query(Settings).first()
        images_path = 'D:\\crms\\images'

        if hasattr(customer, 'card_id_image'):
            SaveImage(images[0].get('card_id_image'),
                      section="customers", id=customer.id, path=images_path, img_name=customer.card_id_image)
        if hasattr(customer, 'driver_id_image'):
            SaveImage(images[1].get('driver_id_image'),
                      section="customers", id=customer.id, path=images_path, img_name=customer.driver_id_image)
            # customer.save()
        return ({'error': False})
    except Exception as e:
        print(f"Error: {e}")
        return (f"Error: {e}")


CreatCustomer({'full_name': 'badr', 'phone': '2654845548',
               'card_id': '', 'driver_id': ''}, images=[{'card_id_image': r'C:\Users\Badr\Downloads\maxresdefault.jpg'}, {'driver_id_image': r'C:\Users\Badr\Downloads\maxresdefault.jpg'}])


def updateCustomerInfo(args, images, id):
    customer = storage.getById(Customer, id=id)

    try:
        if customer is None:
            raise ValueError(f"Customer with provided id not found.")

        # images_path = session.query(Settings).first()
        images_path = 'D:\\crms\\images'
        if len(images) > 0:
            for i in range(len(images)):
                key = list(images[i].keys())[0]
                path = images[i].get(key)
                if path != '':
                    img_name = ImageName(key, path)
                    args.update({key: img_name})
                    save = SaveImage(path, section="customers",
                                     id=customer.id, path=images_path, img_name=img_name)
                    if save.get('error'):
                        raise Exception(save.get('message'))
        for key, value in args.items():
            if value != '':
                setattr(customer, key, value)
        # customer.save()
        return ({'error': False})
    except Exception as e:
        print(e)
        return {'error': True, 'message': e}
