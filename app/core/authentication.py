from models.user import User
from models import storage


def GetUser(username, password):
    """method for getting the user, and check if the 
    username and password are correct"""

    status = False
    message = 'Username not exist'
    userInfo = ""
    users = storage.all(User)
    for user in users.values():
        if user.userName == username:
            if user.password == password:
                message = ''
                status = True
                userInfo = user.to_dict()
            else:
                message = 'Password incorrect'
            break
    return {'status': status, 'message': message, 'userInfo': userInfo}
