import random
import re
from datetime import datetime
from re import match

from flask import url_for

from yacut import db

from .constants import (REGULAR_EXPRESSION, REQUIRED_FIELD, SHORT_IS_BUSY_API,
                        SHORT_MAX_LENGTH, SHORT_NAME_ERROR, SYMBOLS,
                        SYMBOLS_COUNT, URL_ERROR, URL_MAX_LENGTH,
                        URL_MAX_LENGTH_ERROR, URL_REGULAR_EXPRESSION)
from .error_handlers import InvalidAPIUsage


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(URL_MAX_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_MAX_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    JSON_KEY_FOR_ORIGINAL = 'url'
    JSON_KEY_FOR_SHORT = 'custom_id'

    def to_dict(self):
        """Cохранить объект_модели в словарь."""
        return dict(
            url=self.original,
            short_link=url_for('index_view', _external=True) + self.short
        )

    @staticmethod
    def save_obj(**data):
        """Создать объект_модели + сохранить в БД."""
        url_obj = URLMap(**data)
        db.session.add(url_obj)
        db.session.commit()
        return url_obj

    @classmethod
    def check_url(cls, data):
        """Проверка оригинальной ссылки."""
        if cls.JSON_KEY_FOR_ORIGINAL not in data:
            raise InvalidAPIUsage(REQUIRED_FIELD)
        url_value = data.get(cls.JSON_KEY_FOR_ORIGINAL)
        if not match(URL_REGULAR_EXPRESSION, url_value):
            raise InvalidAPIUsage(URL_ERROR)
        if len(url_value) > URL_MAX_LENGTH:
            raise InvalidAPIUsage(URL_MAX_LENGTH_ERROR)
        return url_value

    @staticmethod
    def get_short():
        """Генерация: пользовательский короткий идентификатор."""
        return ''.join(random.choice(SYMBOLS) for item in range(SYMBOLS_COUNT))

    @classmethod
    def check_short(cls, short):
        """Проверка уникальности: пользовательский короткий идентификатор."""
        if cls.query.filter(cls.short == short).first():
            return True  # is double
        return False

    @classmethod
    def check_custom_id(cls, data):
        """Проверка: пользовательский короткий идентификатор."""
        custom_id_value = data.get(cls.JSON_KEY_FOR_SHORT)
        if not custom_id_value:
            custom_id_value = data[cls.JSON_KEY_FOR_SHORT] = cls.get_short()
        if cls.check_short(custom_id_value):
            raise InvalidAPIUsage(SHORT_IS_BUSY_API % custom_id_value)
        if not re.match(REGULAR_EXPRESSION, custom_id_value):
            raise InvalidAPIUsage(SHORT_NAME_ERROR)
        return custom_id_value
