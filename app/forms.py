from passlib.hash import sha512_crypt
from flask.ext.wtf import Form
from wtforms import fields, validators
from app import db
from models import User



class Form(Form):
    def get_user(self):
        if self.login:
            return User.query.filter_by(login=self.login.data).first()
        if self.email:
            return User.query.filter_by(email=self.email.data).first()
    
    def dispose_password(self):
        self.password = None
    
    
    
# Define login and registration forms (for Flask-Login)
class LoginForm(Form):
    login = fields.StringField('Username', validators=[validators.InputRequired()])
    password = fields.PasswordField('Password', \
                                    validators=[validators.InputRequired()])
    
    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user.')
            
    def validate_password(self, field):
        user = self.get_user()
        if user is not None and not sha512_crypt.verify(str(field.data), user.passhash):
            raise validators.ValidationError('Invalid password.')
    


class RegistrationForm(Form):
    login = fields.StringField('Username', validators=[validators.InputRequired(), validators.Length(min=4, max=25, message=(u'Username must have at least 4 characters.'))])
    first_name = fields.StringField('First name', validators=[validators.InputRequired()])
    last_name = fields.StringField('Last name', validators=[validators.InputRequired()])
    email = fields.StringField('Email', validators=[validators.InputRequired(), \
                validators.Email(message=(u'Not a valid email address.'))])
    password = fields.PasswordField('Password', \
                                    validators=[validators.InputRequired(), \
                                    validators.Length(min=8), \
                                    validators.EqualTo('confirm_password', \
                                                       message='Passwords do not match.')])
    confirm_password = fields.PasswordField('Repeat Password')
    
    def validate_login(self, field):
        if User.query.filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username.')



class EditForm(Form):
    login = fields.HiddenField('Username')
    first_name = fields.StringField('First name', validators=[validators.InputRequired()])
    last_name = fields.StringField('Last name', validators=[validators.InputRequired()])
    email = fields.StringField('Email', validators=[validators.InputRequired(), \
                validators.Email(message=(u'Not a valid email address.'))])
    old_password = fields.PasswordField('Password', \
                validators=[validators.InputRequired(), validators.Length(min=8)])
    password = fields.PasswordField('New Password', \
                                    validators=[\
                                    validators.EqualTo('confirm_password', \
                                                        message='Passwords do not match.')])
    confirm_password = fields.PasswordField('Repeat Password')
    
    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user.')
    
    def validate_old_password(self, field):
        user = self.get_user()
        if not sha512_crypt.verify(str(field.data), user.passhash):
            raise validators.ValidationError('Invalid old password.')
            
    def validate_password(self, field):
        password = str(field.data)
        if password != 'None' and password != '':
            if len(password) < 8:
                raise validators.ValidationError('Password is too short.')
            
            
            
class SettingsForm(Form):
    login = fields.HiddenField('Username')
    setting1 = fields.StringField('Setting 1', validators=[validators.InputRequired()])
    setting2 = fields.StringField('Setting 2', validators=[validators.InputRequired()])
    
    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user.')
            
            
            
class ForgotPasswordForm(Form):
    login = None
    email = fields.StringField('Email', validators=[validators.InputRequired(), \
                validators.Email(message=(u'Not a valid email address.'))])
    
    def validate_email(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('No user with the entered email exists.')
    
    
    
class ResetPasswordForm(Form):
    login = fields.HiddenField('Username')
    password = fields.PasswordField('New Password', \
                                    validators=[\
                                    validators.EqualTo('confirm_password',
                                                       message='Passwords do not match.')])
    confirm_password = fields.PasswordField('Repeat Password')
    
    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user.')
            
    def validate_password(self, field):
        password = str(field.data)
        if password != 'None' and password != '':
            if len(password) < 8:
                raise validators.ValidationError('Password is too short.')