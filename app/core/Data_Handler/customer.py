import os
from models.customer import Customer
from models.settings import Settings
from models import storage
import shutil


def ImageName(key, path, name=None):
    file_name = os.path.basename(path)
    extention = file_name.split('.')[-1]
    name = ''
    if key == 'card_id_image' or key == 'driver_id_image':
        words = key.split('_')
        name = f'{words[0]}-{words[1]}.{extention}'
    return name.capitalize()


def SaveImage(file_path, section, id, path, img_name):
    destination_path = os.path.join(path, section, id, img_name)
    os.makedirs(os.path.join(path, section, id,), exist_ok=True)
    try:
        if section == 'customers':
            shutil.copyfile(file_path, destination_path)
    except Exception as e:
        return (f"Error: {e}")


def CreatUser(args, images):
    customer = None
    images_path = None
    session = storage.session()

    """ """
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

    except Exception as e:
        print(f"Error: {e}")
        return (f"Error: {e}")


CreatUser({'full_name': 'badr', 'phone': '2654845548',
          'card_id': '', 'driver_id': ''}, images=[{'card_id_image': r'C:\Users\Badr\Downloads\maxresdefault.jpg'}, {'driver_id_image': r'C:\Users\Badr\Downloads\maxresdefault.jpg'}])
