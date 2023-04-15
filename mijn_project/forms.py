from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from mijn_project.models import User

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    naam = StringField("Naam", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Password Must Match")])
    pass_confirm = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Leg vast")

    def validate_email(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Deze gebruikersnaam is al gebruikt, probeer een ander")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    naam = StringField("Naam")
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Inloggen")