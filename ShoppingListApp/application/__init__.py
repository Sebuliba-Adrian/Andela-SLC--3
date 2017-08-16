from flask import Flask
app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('flask.cfg')


from application.api.views import api_blueprint
from application.shoppingList.views import itemslist_blueprint
from application.user.views import user_blueprint


app.register_blueprint(api_blueprint, url_prefix ='/api')
app.register_blueprint(itemslist_blueprint)
app.register_blueprint(user_blueprint)

