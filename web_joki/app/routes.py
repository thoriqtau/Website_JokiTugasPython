from app import app
from app.controller import UserController

@app.route('/')
def home():
    return UserController.index()

@app.route('/login', methods=['GET','POST'])
def login():
    return UserController.login()

@app.route('/register', methods=['GET','POST'])
def register():
    return UserController.register()