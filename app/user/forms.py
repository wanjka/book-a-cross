from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.user.models import User


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Запомнить', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form-control'})
    confirm = PasswordField(
        'Повторите пароль',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})

    def validate_username(self, username):
        user_cnt = User.query.filter_by(username=username.data).count()
        if user_cnt > 0:
            raise ValidationError('Пользователь с таким именем уже существует')