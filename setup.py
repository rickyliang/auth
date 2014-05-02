from setuptools import setup, find_packages

setup(
    name='Authentication',
    version='1.0',
    packages=['app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask',
                      'Flask-Login',
                      'Flask-Mail',
                      'Flask-SQLAlchemy',
                      'Flask-WTF',
                      'passlib',
                      'decorator',
                      'sqlalchemy-migrate',
                      'pyOpenSSL']
)