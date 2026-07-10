from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    flash("Operation completed successfully")
    return redirect(url_for("index"))

