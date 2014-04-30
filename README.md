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
* Python pyOpenSSL module
* Python decorator module
* Twitter Bootstrap
* jQuery



Usage
-------------
Download and unzip the files in a folder of your choice.

Go into the directory.

Ensure that the `virtualenv` package for Python is installed. Type `pip freeze` into terminal and check if `virtualenv` is listed.

Create a virtual environment called 'venv' by typing into terminal `virtualenv venv`.

Retrieve all the dependencies. Run `python setup.py install` to automatically install the needed modules.

Create the database. Run `python ./db_create.py` to create your database with the name specified in config.py.

Generate your own SSL keys. Run `python ssl_create.py` and enter in the information to your liking. Since this is a test application, it does not really matter what you enter in. However, make sure that you _do not_ enter in a password.

In terminal, run `python ./run.py` to start the server.



Customization
-------------
In config.py, you may change your database name; SSL certificate pointers; secret keys (used for encrypting emails); mail settings; email link expiry duration.

In run.py, you may change your host and port numbers.