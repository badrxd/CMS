from models.base_model import BaseModel
from models.user import User
from models import storage

omar = User(userName="omaridhmaid",
            password="dehao",
            fullName="Omar Id Hmaid",
            isBlocked=False,
            role="faunder",
            secretKey="JB61834")
omar.save()
