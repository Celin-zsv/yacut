import random

from flask import flash, redirect, render_template

from . import app, db
from .constants import SYMBOLS, SYMBOLS_COUNT
from .forms import URLMap_form
from .models import URLMap


def check_short(short):
    """Проверка уникальности: пользовательский короткий идентификатор."""
    if URLMap.query.filter(URLMap.short == short).first():
        return True  # is double
    return False


def get_short():
    """Генерация: пользовательский короткий идентификатор."""
    return ''.join(random.choice(SYMBOLS) for item in range(SYMBOLS_COUNT))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Ввод оригинальной ссылки, ввод /генерация user short идентификатора."""
    form = URLMap_form()
    if form.validate_on_submit():  # POST
        short = form.custom_id.data
        if (not short) or (short is None) or (short == ''):
            short = get_short()
        if check_short(short):
            flash(f'Имя {short} уже занято!', 'flash_short')
            return render_template('index.html', form=form)
        url_obj = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_obj)
        db.session.commit()
        return render_template('index.html', url=url_obj, form=form)

    return render_template('index.html', form=form)  # GET


@app.route('/<short_id>')
def follow_link(short_id):
    """Перейти к оригинальному url на основе: user короткий идентификатор."""
    return redirect(
        URLMap.query.filter(URLMap.short == short_id).first_or_404().original)