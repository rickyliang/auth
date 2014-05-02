auth
=====

A Flask web application that can handle logins, registration, forgotten passwords, profile edits, password changes, and DoS attacks.



Pre-Requisites
-------------
Please make sure that these are installed:
* Python 2.7.x
* Python virtualenv



Requirements
-------------
* Flask
* Flask-Login
* Flask-Mail
* Flask-SQLAlchemy
* Flask-WTF
* Python pyOpenSSL
* Python decorator
* Python passlib
* Python sqlalchemy-migrate
* Python libffi-dev
* Twitter Bootstrap
* jQuery



Setup
-------------
1. Download and unzip the files in a folder of your choice.

2. Go into the directory.

3. **Ensure that pip is installed.** For Windows users, see [here](http://flask.pocoo.org/docs/installation/#pip-and-distribute-on-windows) for instructions.

4. **Ensure that the `virtualenv` module for Python is installed.** Type `pip freeze` into terminal and check if `virtualenv` is listed.
    * If it is, update it to the most recent version by typing `sudo pip install --upgrade virtualenv`.
    * If not, simply type into terminal `sudo pip install virtualenv` for Linux and OSX users, or `pip install virtualenv` for Windows users.

5. **Create a virtual environment.** Type into terminal `virtualenv [the name you want]` without the brackets.

6. **Activate the virtual environment.** For Linux users, type into terminal `. [name of virtual env]/bin/activate`. For Windows users, type `[name of virtual env]/scripts/activate`.

7. **Retrieve all the requirements.** Run `pip install -e .` to automatically install the needed dependencies.

8. **Generate your own SSL keys.** Run `python ssl_create.py` and enter in the information to your liking.
    * Since this is a test application, it does not really matter what you enter in. However, make sure that you _do not_ enter in a password.

9. **Create the database.** Run `python db_create.py` to create your database with the name specified in config.py.

10. **Start the server.** Run `python run.py` and enjoy.



Customization
-------------
In config.py, you may change your database name; SSL certificate pointers; secret keys (used for encrypting emails); mail settings; email link expiry duration.

In run.py, you may change your host and port numbers.