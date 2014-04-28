#!/usr/bin/env python
#
# Richard Liang
#
# Authentication with localhost server example

import os, sqlite3
from OpenSSL import SSL
from wtforms import form, fields, validators
from flask import Flask, request, redirect, url_for, escape, render_template, flash
from flask.ext import login
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy



# Initialize SSL certificate
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.use_privatekey_file('server.key')
ctx.use_certificate_file('server.crt')

# Create Flask application
app = Flask(__name__)

# Create secret key for session management
app.config['SECRET_KEY'] = 'Y\xff\x11&}\nA\xe4,2\x1b\x87\x9d\x1dF\xa9S\x03`\x7f\x05\xcdR\xea-@@\x17\xd7\x12\x13e'

# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)



# Create admin user model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))
    
    """def __init__(self, fname, lname, login, email, pw):
        self.first_name = fname
        self.last_name = lname
        self.login = login
        self.email = email
        self.password = pw"""
    
    # Flask-Login integration
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
        
    def get_id(self):
        return self.id
        
    def __unicode__(self):
        return self.username
    
    def __repr__(self):
        return '<Admin %r>' % (self.first_name + ' ' + self.last_name)



# Define login and registration forms (for Flask-Login)
class LoginForm(Form):
    login = fields.StringField('Username', [validators.InputRequired()])
    password = fields.PasswordField('Password', [validators.InputRequired()])
    
    def validate_login(self, field):
        user = self.get_user()
        
        if user is None:
            raise validators.ValidationError('Invalid user.')
            
        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password.')
            
    def get_user(self):
        return db.session.query(Admin).filter_by(login=self.login.data).first()
    


class RegistrationForm(Form):
    login = fields.StringField('Username', [validators.InputRequired(), \
                                    validators.Length(min=4, max=25, message=(u'Username must have at least 4 characters.'))])
    first_name = fields.StringField('First name', [validators.InputRequired()])
    last_name = fields.StringField('Last name', [validators.InputRequired()])
    email = fields.StringField('Email', [validators.InputRequired(), \
                                    validators.Email(message=(u'Not a valid email address.'))])
    password = fields.PasswordField('Password', [validators.InputRequired(), \
                                    validators.Length(min=6, max=50)])
    
    def validate_login(self, field):
        if db.session.query(Admin).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')



# Function to initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.session_protection = "strong"
    login_manager.init_app(app)
    
    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(Admin).get(int(user_id))
    
        
        
# Create views that handle login & registration
@app.route('/admin/')
@login.login_required
def admin_index():
    print current_user.is_authenticated()
    if not login.current_user.is_authenticated():
        return redirect(url_for('.login_view'))
    return render_template('index.html')
    
@app.route('/', methods=('GET', 'POST'))
@app.route('/login', methods=('GET', 'POST'))
def login_view():
    form = LoginForm(request.form)
    print 'here'
    if form.validate_on_submit():
        user = Admin()
        
        form.populate_obj(user) # populates obj attributes with form data
        
        db.session.add(user)
        db.session.commit()
        
        login.login_user(user)
        return redirect(url_for('.admin_index'))
    link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
    return render_template('login.html', form=form, register=link)
    
@app.route('/register', methods=('GET', 'POST'))
def register_view():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = Admin()
        
        form.populate_obj(user)
        
        db.session.add(user)
        db.session.commit()
        
        login.login_user(user)
        return redirect(url_for('.login_view'))
    link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
    return  render_template('register.html', form=form, login=link)
    
@app.route('/logout')
def logout_view():
    login.logout_user()
    return redirect(url_for('.index'))
        


# Initialize flask-login
init_login()

# Initialize database




if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run(host='127.0.0.1', port=4444)
