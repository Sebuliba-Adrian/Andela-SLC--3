from flask import Blueprint, render_template
itemslist_blueprint = Blueprint('shoppingList', __name__,template_folder='templates')

@itemslist_blueprint.route('/shoppingList')
def itemsList():
    return render_template('shoppingList/index.html')