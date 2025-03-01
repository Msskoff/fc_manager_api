import os
from flask import Flask
from dotenv import load_dotenv

os.getenv("SECRET_KEY")
app = Flask(__name__)

app.config["SECRET_KEY"] = ""
