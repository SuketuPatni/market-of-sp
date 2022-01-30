from market import db, login_manager
from flask_login import UserMixin
# bcrypt doesn't work lol
from hashlib import sha1

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    email_address = db.Column(db.String(length = 50), nullable = False, unique = True)
    # Flask's default hash algorithm returns 60 character string
    password_hash = db.Column(db.String(length=40), nullable = False)
    budget = db.Column(db.Integer(), nullable = False, default = 105000)
    items = db.relationship("Item", backref = "owned_user", lazy = True)

    # password hashing and stuff
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = sha1(plain_text_password.encode()).hexdigest()

    def check_password_correction(self, attempted_password):
        return sha1(attempted_password.encode()).hexdigest() == self.password_hash

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    barcode = db.Column(db.String(length = 12))
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(length=100), nullable = False, unique = True)
    owner = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __repr__(self):
        # to change how "Item.query.all()" is formatted
        return f"Item {self.name}"