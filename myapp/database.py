"""Script to create database tables."""

import os
from myapp import app, models

os.system("dropdb inventory")
os.system("createdb inventory")

models.connect_to_db(app)
models.db.create_all()