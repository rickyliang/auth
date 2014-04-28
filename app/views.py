from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, session, g
from flask.ext.login import login_user, logout_user, login_required, fresh_login_required, current_user

from app import app, db, lm
from forms import LoginForm, RegistrationForm, EditForm, SettingsForm, ForgotPasswordForm, ResetPasswordForm
from models import User, ROLE_USER, ROLE_ADMIN
from emails import send_verification_mail, send_reset_password_email
from utils import encrypt_password, get_serialized_token, unserialize_token
from messages import messages as msgs



@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('.login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('.admin_index'))
    
    form = LoginForm()
    enable_delay = False
    user = User.query.filter_by(login=form.login.data).first()
    if form.validate_on_submit():
        login_user(user)
        user.reset_failed_login_attempts()
        flash(msgs['LOGIN_SUCCESS'])
        return redirect(request.args.get('next') or url_for('.admin_index'))
    elif user is not None:          # Hits this case only when password is wrong.
        if user.failed_login_attempts > 4:
            enable_delay = True     # Triggers javascript login delay in template.
        user.failed_to_login()      # Increments the user's failed_login_attempts
        
    for field in form.errors:
        flash('<strong>' + field.capitalize() + '</strong>' + ': ' + form.errors[field][0], 'error')
    
    register_link = '<p>Don\'t have an account? <a href="' + url_for('.register') + '">Click here to register.</a></p>'
    forgot_password_link = '<p>Forgot your password? <a href="' + url_for('.forgot_password') + '">Click here to reset.</a></p>'
    return render_template('login.html', form=form, register=register_link, forgot_password=forgot_password_link, enable_delay=enable_delay)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        
        form.populate_obj(user)
        
        encrypted_password = encrypt_password(form.password.data)
        user.passhash = encrypted_password
        
        db.session.add(user)
        db.session.commit()
        
        form.dispose_password()
        
        # http://flask.pocoo.org/snippets/50/
        serialized_token = get_serialized_token(user, 'activate')
        send_verification_mail(user, serialized_token)
        flash(msgs['CREATE_ACCOUNT_SUCCESS'])
        return redirect(url_for('.login'))
    
    for field in form.errors:
        flash('<strong>' + field.capitalize() + '</strong>' + ': ' + form.errors[field][0], 'error')
        
    login_link = '<p>Already have an account? <a href="' + url_for('.login') + '">Click here to log in.</a></p>'
    return render_template('register.html', form=form, login=login_link)


@app.route('/resend_verification/<login>')
@login_required
def resend_verification(login):
    user = User.query.filter_by(login=login).first()
    if user == None:
        flash('User ' + login + ' not found.', 'error')
        return redirect(url_for('.admin_index'))
    
    serialized_token = get_serialized_token(user, 'activate')
    send_verification_mail(user, serialized_token)
    flash(msgs['SEND_ACTIVATE_EMAIL'])
    return redirect(url_for('.admin_profile', login=login))


@app.route('/activate/<serialized_token>')
def activate(serialized_token):
    expired, invalid, user = unserialize_token(serialized_token, 'activate')
    if expired:
        flash(msgs['LINK_EXPIRED'], 'error')
        return redirect(url_for('.index'))
    if invalid:
        flash(msgs['LINK_INVALID'], 'error')
        return redirect(url_for('.index'))
    user.activate()
    flash(msgs['ACTIVATION_SUCCESS'])
    login_user(user)
    return redirect(url_for('.admin_index'))


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        serialized_token = get_serialized_token(user, 'reset')
        send_reset_password_email(user, serialized_token)
        flash(msgs['SEND_RESET_EMAIL'])
        return redirect(url_for('.login'))
    
    for field in form.errors:
        flash('<strong>' + field.capitalize() + '</strong>' + ': ' + form.errors[field][0], 'error')
    
    login_link = '<p>Remembered your password? <a href="' + url_for('.login') + '">Click here to log in.</a></p>'
    return render_template('forgot_password.html', form=form, login=login_link)


@app.route('/reset_password/<serialized_token>', methods=['GET', 'POST'])
def reset_password(serialized_token):
    expired, invalid, user = unserialize_token(serialized_token, 'reset')
    if expired:
        flash(msgs['LINK_EXPIRED'], 'error')
        return redirect(url_for('.index'))
    if invalid:
        flash(msgs['LINK_INVALID'], 'error')
        return redirect(url_for('.index'))
    
    form = ResetPasswordForm()
    form.login.data = user.login
    if form.validate_on_submit():
        encrypted_password = encrypt_password(form.password.data)
        user.passhash = encrypted_password

        db.session.add(user)
        db.session.commit()

        form.dispose_password()

        flash(msgs['RESET_PASSWORD_SUCCESS'])
        return redirect(url_for('.login'))
    
    for field in form.errors:
        flash('<strong>' + field.capitalize() + '</strong>' + ': ' + form.errors[field][0], 'error')
    
    return render_template('reset_password.html', form=form, serialized_token=serialized_token)


@app.route('/logout')
def logout():
    logout_user()
    flash(msgs['LOGOUT_SUCCESS'])
    return redirect(url_for('.index'))



# Administrative pages (templates/admin/)
@app.route('/admin/')
#@app.route('/admin/index')
@login_required
def admin_index():
    return render_template('admin/index.html', user=g.user)

@app.route('/admin/users')
@login_required
def admin_users():
    if g.user.is_activated():
        return render_template('admin/users.html', user=g.user)
    else:
        flash(msgs['NOT_ACTIVATED'])
        return redirect(url_for('.admin_index'))

@app.route('/admin/profile/<login>', methods=['GET', 'POST'])
@login_required
def admin_profile(login):
    user = User.query.filter_by(login=login).first()
    if user == None:
        flash('User ' + login + ' not found.', 'error')
        return redirect(url_for('admin_index'))
    
    form = EditForm()
    if request.method == 'POST':
        form.login.data = user.login;
        if form.validate():
            if form.password.data == '':
                user.first_name = form.first_name.data
                user.last_name = form.last_name.data
                user.email = form.email.data
            else:
                form.populate_obj(user)
                user.passhash = encrypt_password(form.password.data)
                form.dispose_password()
                
            db.session.add(user)
            db.session.commit()
            flash(msgs['EDIT_SUCCESS'])
            return redirect(url_for('admin_profile', login=login))
        
    for field in form.errors:
        flash('<strong>' + field.capitalize() + '</strong>' + ': ' + form.errors[field][0], 'error')
        
    return render_template('admin/profile.html', form=form, user=user)

@app.route('/admin/settings')
@login_required
def admin_settings():
    if g.user.is_activated():
        form = SettingsForm()
        return render_template('admin/settings.html', form=form, user=g.user)
    else:
        flash(msgs['NOT_ACTIVATED'])
        return redirect(url_for('.admin_index'))