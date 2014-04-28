auth
=====

A Flask web application that can handle logins, registration, forgotten passwords, profile edits, password changes, and DoS attacks.



Dependencies
-------------
Please make sure that these are installed:
* Python 2.7
* Flask
* Flask-Login
* Flask-Mail
* Flask-SQLAlchemy
* Flask-WTF
* WTForms
* itsdangerous
* OpenSSL
* Python decorator module
* Python passlib module
* Twitter Bootstrap
* jQuery



Usage
-------------
Download and unzip the files in a folder of your choice.

In config.py, you may change your database name; SSL certificate pointers; secret keys (used for encrypting emails); mail settings; email link expiry duration.

In run.py, you may change your host and port numbers.

In terminal within the directory, run `./db_create.py` to create your database with the name specified in config.py.

Generate your own private and public keys and put them in the directory.

In terminal, run `python ./run.py` to start the server.