messages = {
    'BAD_USERNAME': 'Invalid username.',
    'NOT_ACTIVATED': 'Your account is not activated. Please verify your email to activate your account.',
    'LINK_EXPIRED': 'Link expired. Please try again.',
    'LINK_INVALID': 'Invalid link or other error. Please try again.',
    'ACTIVATION_SUCCESS': 'Activation successful.',
    'CREATE_ACCOUNT_SUCCESS': 'Successfully created your account. Please check your email to activate your account.',
    'LOGIN_SUCCESS': 'Successfully logged in.',
    'LOGOUT_SUCCESS': 'Successfully logged out.',
    'EDIT_SUCCESS': 'Your changes have been saved.',
    'RESET_PASSWORD_SUCCESS': 'Your password has been changed.',
    'SEND_ACTIVATE_EMAIL': 'Activation email successfully sent. Please check your email.',
    'SEND_RESET_EMAIL': 'Password reset email successfully sent. Please check your email.',
    'EMAIL_SUBJECT': 'Your account.'
}

def add_message(name, msg):
    messages[name] = msg
    return True
