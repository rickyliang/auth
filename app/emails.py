# Thank you to http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support

from flask import render_template, url_for
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS
from messages import messages as msgs

from decorators import async

@async
def send_async_mail(msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    send_async_mail(msg)
    
def send_verification_mail(user, serialized_token):
    activation_url = url_for('.activate', serialized_token=serialized_token, _external=True)
    send_mail(msgs['EMAIL_SUBJECT'],
              ADMINS[0],
              [user.email],
              render_template('verification_email.txt',
                              user=user, activation_url=activation_url))
    
def send_reset_password_email(user, serialized_token):
    reset_url = url_for('.reset_password', serialized_token=serialized_token, _external=True)
    send_mail(msgs['EMAIL_SUBJECT'],
              ADMINS[0],
              [user.email],
              render_template('reset_password_email.txt',
                              user=user, reset_url=reset_url))