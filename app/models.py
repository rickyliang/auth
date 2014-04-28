from app import db

ROLE_USER = 0
ROLE_ADMIN = 1
UNACTIVATED = 0
ACTIVATED = 1



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    passhash = db.Column(db.String(128))
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    status = db.Column(db.SmallInteger, default=UNACTIVATED)
    last_seen = db.Column(db.DateTime)
    failed_login_attempts = db.Column(db.SmallInteger, default=0)
    
    # Flask-Login integration
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
    
    def is_activated(self):
        return self.status == ACTIVATED
        
    def get_id(self):
        return self.id
    
    # Used primarily in templates (specifically pre-filled ones) to access a
    # user's data based on the field's name.
    def attr(self, attribute):
        try:
            if attribute.lower() == 'first_name':
                return self.first_name
            if attribute.lower() == 'last_name':
                return self.last_name
            if attribute.lower() == 'email':
                return self.email
        except TypeError:
            return "TYPEERROR OMFGOMFGOFMGOFMGOGMOGMOGMGOGMOGMGOMGGGGGGGGGGGGGGG!!!!!!!!!!!"
    
    def activate(self):
        self.status = ACTIVATED
        db.session.commit()
        
    def failed_to_login(self):
        if self.failed_login_attempts == None:
            self.failed_login_attempts = 0
        self.failed_login_attempts += 1
        db.session.commit()
        
    def reset_failed_login_attempts(self):
        self.failed_login_attempts = 0
        db.session.commit()
        
    def __unicode__(self):
        return self.login
    
    def __repr__(self):
        return '<User %r>' % (self.first_name + ' ' + self.last_name)