from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    registration_date = db.Column(db.DateTime, server_default=db.func.now())
    categories = db.relationship("category", backref="user")
    wallets = db.relationship("Wallet", backref="user") 

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_name = db.Column(db.String)
    category_type = db.Column(db.Enum("Income", "Expense"))





class Transaction(db.Model):   
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    category_id =db.Column(db.Integer, db.ForeignKey("categories.id"))
    wallet_id = db.Column(db.Integer, db.ForeignKey("wallets.id"))
    amount = db.Column(db.Integer)
    description = db.Column(db.String)

    

class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    wallet_id = db.Column(db.String)
    amount = db.Column(db.Integer)

    transactions = db.relationship("Transaction", backref="wallet")






