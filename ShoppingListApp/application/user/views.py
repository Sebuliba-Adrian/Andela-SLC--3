from flask import Blueprint, render_template
user_blueprint = Blueprint('user', __name__,template_folder='templates')

@user_blueprint.route('/user')
def user():
    return render_template('user/index.html')
