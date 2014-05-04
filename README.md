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
    * If you will have multiple versions of Python, check out [how to install and configure](http://stackoverflow.com/questions/4583367/how-to-run-multiple-python-version-on-windows) and [how to use pip](http://stackoverflow.com/questions/2812520/pip-dealing-with-multiple-python-versions) with another version of Python.

4. **Ensure that non-Python dependencies required for the `cryptography` package are installed**. For Debian/Ubuntu users: `sudo apt-get install build-essential libssl-dev libffi-dev python-dev`. For Windows users, install the latest version of OpenSSL [here](http://slproweb.com/products/Win32OpenSSL.html). Add `C:\OpenSSL-Win64\bin` to your PATH environment variable.

5. **Ensure that the `virtualenv` module for Python is installed.** Type `pip freeze` into terminal and check if `virtualenv` is listed.
    * If it is, update it to the most recent version by typing `sudo pip install --upgrade virtualenv`.
    * If not, simply type into terminal `sudo pip install virtualenv` for Linux and OSX users, or `pip install virtualenv` for Windows users, `pip2.7 install virtualenv` if you have multiple versions.
    * Note: virtualenv version 1.11.x may not work; install `virtualenv==1.10.1` in this case.

6. **Create a virtual environment.** Type into terminal `virtualenv [the name you want]` without the brackets, `virtualenv --python=[path/to/python/python.exe] [the name you want]` if you have multiple versions.

7. **Activate the virtual environment.** For Linux users, type into terminal `. [name of virtual env]/bin/activate`. For Windows users, type `[name of virtual env]\Scripts\activate`.

8. **Windows users ONLY**. This is to install `cryptography`. Run `pip install wheels`. Run `pip install --use-wheel cryptography`.
    * On Windows, if an error about distutils or it being "unable to find vcvarsall.bat", see [this](http://springflex.blogspot.com/2014/02/how-to-fix-valueerror-when-trying-to.html) or [this](http://blog.victorjabur.com/2011/06/05/compiling-python-2-7-modules-on-windows-32-and-64-using-msvc-2008-express/). It is ridiculous, I know; blame Python for not including a C compiler.

9. **Retrieve all the requirements.** Run `pip install -e .` to automatically install the needed dependencies.

10. **Generate your own SSL keys.** Run `python ssl_create.py` and enter in the information to your liking.
    * Since this is a test application, it does not really matter what you enter in. However, make sure that you _do not_ enter in a password.

11. **Create the database.** Run `python db_create.py` to create your database with the name specified in config.py.

12. **Start the server.** Run `python run.py` and enjoy.



Customization
-------------
In `templates/layout.html` and in the various email text templates, change the organization name to your organization's name in the footers.

In `config.py`, you may change your database name; SSL certificate pointers; secret keys (used for encrypting emails); mail settings (necessary for the app to send forgot-password, account-verification emails); email link expiry duration.

In `run.py`, you may change your host and port numbers.
