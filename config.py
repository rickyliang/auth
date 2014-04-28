import os
from datetime import timedelta
from OpenSSL import SSL
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sample_db.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_ECHO = True


CSRF_ENABLED = True
#REMEMBER_COOKIE_DURATION = timedelta(seconds=10)

# The number of seconds a link that is emailed to the user will be valid.
# Applies for RESET_PASSWORD, ACCOUNT_ACTIVATION thus far.
# Default: 900 (15 minutes)
LINK_DURATION = 900

# The salt used for sending password reset links to emails.
RESET_SALT = 'reset-salt'

# The salt used for sending activation links to emails.
ACTIVATE_SALT = 'activate-salt'

# The key used to encrypt sensitive links that are sent to users via email.
SECRET_KEY = 'Y\xff\x11&}\nA\xe4,2\x1b\x87\x9d\x1dF\xa9S\x03`\x7f\x05\xcdR\xea-@@\x17\xd7\x12\x13e'

CTX = SSL.Context(SSL.SSLv23_METHOD)
CTX.use_privatekey_file('server.key')
CTX.use_certificate_file('server.crt')

# Flask-Mail configuration
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None

ADMINS = ['admin@localhost']