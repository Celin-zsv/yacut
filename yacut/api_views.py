import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import REGULAR_EXPRESSION
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import check_short, get_short


@app.route('/api/id/', methods=['POST'])
def add_url():
    """Ввод оригинальной ссылки, ввод /генерация user short идентификатора."""
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    custom_id = data.get('custom_id')
    if ('custom_id' not in data) or (custom_id is None) or (custom_id == ''):
        custom_id = data['custom_id'] = get_short()
    if check_short(custom_id):
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    if not re.match(REGULAR_EXPRESSION, custom_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    url_obj = URLMap()
    url_obj.from_dict(data)
    db.session.add(url_obj)
    db.session.commit()
    return jsonify(url_obj.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    """Перейти к оригинальному url на основе: user короткий идентификатор."""
    url_obj = URLMap.query.filter(URLMap.short == short_id).first()
    if not url_obj:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_obj.original}), HTTPStatus.OK
