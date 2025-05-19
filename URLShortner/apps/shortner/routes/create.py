from flask import Blueprint

shortner_app_route = Blueprint('shortner', __name__)

@shortner_app_route.route('/create')
def create_route():
    return {"voila": "ok"}