from models.customer import Customer
from models.settings import Settings
from models import storage
from app.core.image_handler import ImageName, SaveImage
from models import storage

"WORNING : THERE IS SOME INFINISHED LOGIC"


# def handelImageAtt(args, images, id, images_path):

#     if len(images) > 0:
#         for i in range(len(images)):
#             key = list(images[i].keys())[0]
#             path = images[i].get(key)
#             if path != '':
#                 img_name = ImageName(key, path)
#                 args.update({key: img_name})
#                 save = SaveImage(path, section="customers",
#                                  id=id, path=images_path, img_name=img_name)
#                 if save.get('error'):
#                     raise Exception(save.get('message'))


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
                      section="customers",  path=images_path, img_name=customer.card_id_image, id=customer.id,)
        if hasattr(customer, 'driver_id_image'):
            SaveImage(images[1].get('driver_id_image'),
                      section="customers", path=images_path, img_name=customer.driver_id_image, id=customer.id)
            # customer.save()
        return ({'error': False})
    except Exception as e:
        print(f"Error: {e}")
        return {'error': True, 'message': e}


def updateCustomerInfo(args, images, id):
    customer = storage.getById(Customer, id=id)
    session = storage.session()

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
                                     path=images_path, img_name=img_name, id=customer.id)
                    if save.get('error'):
                        raise IOError(save.get('message'))
        for key, value in args.items():
            if value != '':
                setattr(customer, key, value)
        # customer.save()
        return ({'error': False})
    except (IOError, OSError, ValueError) as e:
        return {'error': True, 'message': e}
    except Exception as e:
        print(e)
