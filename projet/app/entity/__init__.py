
from flask import Flask, render_template, url_for,flash,redirect,request, jsonify,make_response
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager
from pymongo import MongoClient
#from flask_mail import Mail
from app.config import Config
import os
#from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS
# Initialize Flask App  C:\new services\Constat\projet\app\config.py




cred = credentials.Certificate('C:/new services/Constat/projet/app/key.json')
default_app = initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
bcrypt = Bcrypt()

''' def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    with app.app_context():
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")

   
    bcrypt.init_app(app)
    
    

    from app.entity.Routeur.route import routeur
    
    
    
    app.register_blueprint(routeur)
    
    return app '''

class MongoAPI:
    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:27017/")  
      
        database = data['RouteurBD']
        collection = data['routeur']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data