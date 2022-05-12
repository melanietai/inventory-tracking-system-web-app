"""Script to create database tables."""

import os
import models
import run

os.system("dropdb inventoryboss")
os.system("createdb inventoryboss")

models.connect_to_db(run.app)
models.db.create_all()