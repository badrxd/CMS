import shutil
import os


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
        return ({'error': False})
    except Exception as e:
        print(e)
        return ({'error': True, 'message': 'There is a problem in saving the photo'})
