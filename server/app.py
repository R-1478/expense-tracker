from flask import Flask
from flask_migrate import Migrate
from models import db

# Create an instance of a flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "<h1>Welcome to my Wallet Tracker</h1>"

@app.route('/<string:username>')
def login(username):
    return f'<h1>Wallet for {username}</h1>'




if __name__ == '__main__':
    app.run(port=5555, debug=True)

