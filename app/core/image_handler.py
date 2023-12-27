import shutil
import os


def ImageName(name, path):
    file_name = os.path.basename(path)
    extention = file_name.split('.')[-1]
    img_name = ''
    if name == 'card_id_image' or name == 'driver_id_image':
        words = name.split('_')
        img_name = f'{words[0]}-{words[1]}.{extention}'
    else:
        img_name = f'{name}.{extention}'
    return img_name.capitalize()


def SaveImage(file_path, section, path, img_name, id=''):
    destination_path = ''
    os.makedirs(os.path.join(path, section, id,), exist_ok=True)
    try:
        if section == 'customers':
            destination_path = os.path.join(path, section, id, img_name)
        elif section == 'cars':
            destination_path = os.path.join(path, section, img_name)
        else:
            pass

        shutil.copyfile(file_path, destination_path)

        return ({'error': False})
    except Exception as e:
        print(e)
        return ({'error': True, 'message': 'There is a problem in saving the photo'})
