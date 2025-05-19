import yaml, json
from flask import Flask, Blueprint, redirect, Response
from database import get_db
from apps.shortner.routes.create import shortner_app_route
from apps.shortner import models

app = Flask(__name__)



###### Blueprint test ######
root_url = Blueprint('root', __name__)

# test url /test-base/test-url
@root_url.route("/<hash_str>")
def dashboard(hash_str):
    db = get_db()
    tinyurl_obj = db.query(models.URLMapper).filter(models.URLMapper.hash_str==hash_str).first()
    if not tinyurl_obj:
        return Response(json.dumps({
            "message": "Invalid input",
            "success": False
        }), status=400,
        mimetype="application/json")
    return redirect(tinyurl_obj.url,code=302)
#############################

app.register_blueprint(root_url, url_prefix='/')
app.register_blueprint(shortner_app_route, url_prefix='/shortner')


if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=8000, debug=True)