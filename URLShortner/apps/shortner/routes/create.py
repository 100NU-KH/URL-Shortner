import os
from flask import Blueprint, request

from database import get_db
from services.url_substitute import compute_cheap_hash
from apps.shortner.models import URLMapper

shortner_app_route = Blueprint('shortner', __name__)

@shortner_app_route.route('/create', methods=['POST'])
def create_route():
    data = request.get_json()
    # validate the input
    tiny_url_hash = compute_cheap_hash(data['url'])
    db = get_db()
    tiny_url = os.environ['HOST'] + tiny_url_hash
    url_obj = URLMapper(
        url=data['url'],
        hash_str=tiny_url_hash,
        tiny_url=tiny_url
    )
    db.add(url_obj)
    db.commit()
    db.refresh(url_obj)
    return {"message": "success",
            "status": True,
            "data": {
                "tiny-url": tiny_url
            }
        }