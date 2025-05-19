from flask import Flask, Blueprint
import database
from apps.shortner.routes.create import shortner_app_route
from apps.shortner import models

app = Flask(__name__)

###### Blueprint test ######
test_blue = Blueprint('test', __name__)

# test url /test-base/test-url
@test_blue.route("/test-url")
def dashboard():
    return {"message": "ok"}
#############################

app.register_blueprint(test_blue, url_prefix='/test-base')
app.register_blueprint(shortner_app_route, url_prefix='/shortner')


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=8000, debug=True)