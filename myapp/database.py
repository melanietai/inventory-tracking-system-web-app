"""Script to create database tables."""

import os
import models
from myapp import app

os.system("dropdb inventoryboss")
os.system("createdb inventoryboss")

models.connect_to_db(app)
models.db.create_all()