from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db= SQLAlchemy()

cart = db.Table(
    'cart',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), nullable=False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    cart = db.relationship('Product',
        secondary = cart,
        backref = db.backref('cart', lazy='dynamic'),
        lazy = 'dynamic'
    )
    def add(self, user):
        self.cart.append(user)
        db.session.commit()
    
    def empty(self):
        self.cart.clear()
        db.session.commit()

    def remove(self, user):
        self.cart.remove(user)
        db.session.commit()

    def clearCart(self):
        self.cart = []
        db.session.commit()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password) 
        #self.password = password   ---OLD  not hashed

    def saveUser(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    image = db.Column(db.String)
    category = db.Column(db.String)
    rating = db.Column(db.Integer)
    rating_count= db.Column(db.Integer)

    def __init__(self, title, price, description, image, category, rating, rating_count):
        self.title = title
        self.price = price
        self.description = description
        self.image = image
        self.category = category
        self.rating = rating
        self.rating_count = rating_count

    def saveProduct(self):
        db.session.add(self)
        db.session.commit()

    def removeProduct(self):
        db.session.remove()
        db.session.commit()