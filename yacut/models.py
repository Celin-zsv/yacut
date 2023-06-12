import random
import re
from datetime import datetime
from re import match

from flask import url_for

from . import db
from .constants import (JSON_KEY_FOR_ORIGINAL, JSON_KEY_FOR_SHORT,
                        REGULAR_EXPRESSION, REQUIRED_FIELD, SHORT_IS_BUSY_API,
                        SHORT_MAX_LENGTH, SHORT_NAME_ERROR, SYMBOLS,
                        SYMBOLS_COUNT, URL_ERROR, URL_MAX_LENGTH,
                        URL_MAX_LENGTH_ERROR, URL_REGULAR_EXPRESSION)
from .error_handlers import InvalidAPIUsage


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(URL_MAX_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_MAX_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Cохранить объект_модели в словарь."""
        return dict(
            url=self.original,
            short_link=url_for('index_view', _external=True) + self.short
        )

    @classmethod
    def save_obj(cls, **data):
        """1)Проверить вх.данные(API), 2)Создать объект, 3)Сохранить в БД."""
        if cls.original.name not in data:  # is API-data
            url_obj = URLMap(
                original=cls.check_url(data),
                short=cls.check_short(data.get(JSON_KEY_FOR_SHORT)))
        else:
            url_obj = URLMap(**data)
        db.session.add(url_obj)
        db.session.commit()
        return url_obj

    @classmethod
    def check_url(cls, data):
        """Проверка оригинальной ссылки."""
        if JSON_KEY_FOR_ORIGINAL not in data:
            raise InvalidAPIUsage(REQUIRED_FIELD)
        url_value = data.get(JSON_KEY_FOR_ORIGINAL)
        if not match(URL_REGULAR_EXPRESSION, url_value):
            raise InvalidAPIUsage(URL_ERROR)
        if len(url_value) > URL_MAX_LENGTH:
            raise InvalidAPIUsage(URL_MAX_LENGTH_ERROR)
        return url_value

    @classmethod
    def check_short(cls, short):
        """Генерация, проверка уникальности /маски: user короткий идентификатор."""
        if not short:
            short = ''.join(random.choice(SYMBOLS) for item in range(SYMBOLS_COUNT))
        if cls.get_url_obj(short).first():
            raise InvalidAPIUsage(SHORT_IS_BUSY_API.format(short=short))
        if not re.match(REGULAR_EXPRESSION, short):
            raise InvalidAPIUsage(SHORT_NAME_ERROR)
        return short

    @staticmethod
    def get_url_obj(short_id):
        """Получить оригинальный url на основе: user короткий идентификатор."""
        return URLMap.query.filter(URLMap.short == short_id)
