from flask import Flask, request, render_template, redirect
from flask_mongoengine import MongoEngine, Pagination


db = MongoEngine()

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = 'KeepThisS3cret'