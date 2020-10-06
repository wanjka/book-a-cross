from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from app import db
from app.user.forms import LoginForm, RegistrationForm
from app.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for(root.index))

    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process_login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user_is_knocking = User.query.filter(User.username == form.username.data).first()

        if user_is_knocking and user_is_knocking.check_password(form.password.data):
            login_user(user_is_knocking, form.remember_me.data)
            flash('Добро пожаловать, {}!'.format(user_is_knocking.username))
            return redirect(url_for(root.index))

        else:
            flash('Неправильный логин или пароль')
            return redirect(url_for('user.login'))

    else:
        flash('Ты пытаешься залогиниться, но ты делаешь это без уважения...')
        return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(root.index))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for(root.index))
    form = RegistrationForm()
    title = 'Регистрация'
    return render_template('user/register.html', page_title=title, form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))

    else:
        for field, errors in form.errors.items():
            for err in errors:
                flash(f'Ошибка в поле {getattr(form, field).label.text}: {err}')

        return redirect(url_for('user.register'))
    # flash('Пожалуйста, исправьте ошибки в форме')
    # return redirect(url_for('user.register'))
