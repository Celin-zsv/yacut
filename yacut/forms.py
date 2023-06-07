from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import REGULAR_EXPRESSION


class URLMap_form(FlaskForm):
    original_link = URLField(
        'Оригинальная длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256),
            URL('Некорректная ссылка')]
    )
    custom_id = StringField(
        'Пользовательский короткий идентификатор',
        validators=[
            Optional(),
            Length(1, 16),
            Regexp(
                regex=REGULAR_EXPRESSION,
                message='Допускаются: буквы a-z A-Z, цифры 0-9'
            )]
    )
    submit = SubmitField()