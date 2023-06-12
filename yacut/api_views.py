from http import HTTPStatus

from flask import jsonify, request

from . import app
from .constants import (JSON_KEY_FOR_ORIGINAL, REQUEST_BODY_ERROR,
                        URL_OBJ_NOT_FOUND)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_url():
    """Ввод оригинальной ссылки, ввод /генерация user short идентификатора."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(REQUEST_BODY_ERROR)
    return jsonify(URLMap.save_obj(**data).to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """Перейти к оригинальному url на основе: user короткий идентификатор."""
    url_obj = URLMap.get_url_obj(short_id).first()
    if not url_obj:
        raise InvalidAPIUsage(URL_OBJ_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify({JSON_KEY_FOR_ORIGINAL: url_obj.original}), HTTPStatus.OK
