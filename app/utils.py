from passlib.hash import sha512_crypt
from datetime import timedelta
from app import app, lm
from models import User
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired



@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

def encrypt_password(password):
        password = str(password)
        passhash = sha512_crypt.encrypt(password, rounds=250000)
        return passhash

def get_max_age():
    return app.config['LINK_DURATION']

# http://flask.pocoo.org/snippets/50/
# A helper function that returns a serializer salted with a
# salt (identified by the salt_name argument that is passed in)
# that is stored in this application's config.
def get_serializer(salt_name):
    secret_key = app.config.get('SECRET_KEY')
    salt = app.config.get('%s_SALT' % salt_name.upper())
    return URLSafeTimedSerializer(secret_key=secret_key, salt=salt)

# Generates a token using data specific from the user and
# a salt from this application's config.
def get_serialized_token(user, salt_name):
    data = user.id
    serializer = get_serializer(salt_name)
    return serializer.dumps(data)

# https://github.com/mattupstate/flask-security/blob/develop/flask_security/utils.py
def unserialize_token(serialized_token, salt_name, max_age=None):
    user, data = None, None
    max_age = get_max_age()
    expired, invalid = False, False
    
    serializer = get_serializer(salt_name)
    try:
        data = serializer.loads(serialized_token, max_age=max_age)
    except SignatureExpired:
        expired = True
    except BadSignature:
        invalid = True
    except TypeError:
        invalid = True
    except ValueError:
        invalid = True
    
    if data:
        user = load_user(data)
    
    return expired, invalid, user