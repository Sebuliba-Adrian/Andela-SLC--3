from flask import Blueprint
itemslist_blueprint = Blueprint('shoppingList', __name__,template_folder='templates')
from . import views