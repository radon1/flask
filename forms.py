from flask_mongoengine.wtf import model_form
from models import UserV


UserForm = model_form(UserV)