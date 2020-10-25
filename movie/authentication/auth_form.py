from flask_wtf import FlaskForm
from password_validator import PasswordValidator
from wtforms import StringField, PasswordField, SubmitField, Field
from wtforms.validators import DataRequired, ValidationError


class PasswordValid:
    def __init__(self, message: str = None):
        if not message:
            message = u'Password should have at least 8 letters\n' \
                      u'at least One upper and lower cases'
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        the_schema = PasswordValidator()
        the_schema \
            .min(8) \
            .has().lowercase() \
            .has().digits()
        if not the_schema.validate(field.data):
            raise ValidationError(self.message)


class LoginForm(FlaskForm):

    username = StringField(label='Email or Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Press Login...')


class RegistrationForm(FlaskForm):
    username = StringField(label='Email or Username', validators=[
        DataRequired(message='Please write your username')])

    password = PasswordField(label='Password', validators=[
        DataRequired(message='Please Type your password'), PasswordValid()])

    submit = SubmitField(label='Press Register...')


