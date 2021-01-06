from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

if __name__ = "__main__":
    app.secret_key = 'fwe9558jffwiru1402mfj35gregw'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run()

# Database

client = MongoClient('mongodb://localhost:27017/')
db = client['user_login_system']

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')