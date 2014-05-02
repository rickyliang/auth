from setuptools import setup, find_packages

setup(
    name='Authentication',
    version='1.0',
    url='https://github.com/rickyliang/auth',
    license='MIT',
    author='Richard Liang',
    author_email='rickyliang@berkeley.edu',
    description='An authentication application based on Flask and the pursuit of knowledge in internet security',
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