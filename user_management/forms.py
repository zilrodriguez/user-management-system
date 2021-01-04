from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, Email, EqualTo
from user_management.models import User

class UserForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(), Email(), Length(min=1, max=64)])
    password = PasswordField('Password',
    validators=[DataRequired(), Length(min=6, max=64)])
    confirmPassword = PasswordField('Confirm Password',
    validators=[DataRequired(), EqualTo('password')])
    userRole = SelectField('User Role',
    choices=[('', 'Select'), ('Administrator', 'Administrator'), ('User', 'User')], validators=[DataRequired()])
    submit = SubmitField('Save')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address was already taken.')
    
class LoginForm(FlaskForm):
    email = StringField('Email',
    validators=[DataRequired(), Email()])
    password = PasswordField('Password',
    validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')