from flask import Flask, redirect, render_template, request, url_for, abort
import sqlite3

app = Flask(__name__)

@app.route("/") # controlador
def root():
    return render_template(template_name_or_list="base.html") #view

@app.route("/index")  # controlador
def index():
    connection = sqlite3.connect("basedatos.db")
    cur = connection.cursor()
    posts = cur.execute("SELECT * FROM posts;").fetchall()

    return render_template("index.html", post_list=posts)

@app.route("/home") # controlador
def home():
    return render_template(template_name_or_list="home.html") #view


