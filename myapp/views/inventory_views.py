from flask import (render_template, redirect, flash, request)
from crud import inventory_crud
from myapp import app

@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/inventories")
def get_inventories():
    """Return all inventories."""

    inventories = inventory_crud.get_inventories()

    return render_template("overview.html", inventories=inventories)

