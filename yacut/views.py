from flask import flash, redirect, render_template

from . import app
from .constants import SHORT_IS_BUSY_FORM
from .forms import URLMap_form
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Ввод оригинальной ссылки, ввод /генерация user short идентификатора."""
    form = URLMap_form()
    if form.validate_on_submit():  # POST
        short = form.custom_id.data or URLMap.get_short()
        if URLMap.check_short(short):
            flash(SHORT_IS_BUSY_FORM % short, 'flash_short')
            return render_template('index.html', form=form)
        return render_template(
            'index.html',
            url=URLMap.save_obj(original=form.original_link.data, short=short),
            form=form)

    return render_template('index.html', form=form)  # GET


@app.route('/<short_id>')
def follow_link(short_id):
    """Перейти к оригинальному url на основе: user короткий идентификатор."""
    return redirect(
        URLMap.query.filter(URLMap.short == short_id).first_or_404().original)