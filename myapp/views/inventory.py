from flask import (render_template)
from myapp.crud import inventory_crud


def index():
    """Return all inventories."""

    inventories = inventory_crud.get_inventories()

    return render_template("overview.html", inventories=inventories)

