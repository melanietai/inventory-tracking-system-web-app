from flask import (render_template)
from myapp.crud import inventory_crud


def index():
    """Return all inventory items to overview page."""

    all_inventory = inventory_crud.get_all_inventory()

    return render_template("overview.html", all_inventory=all_inventory)


def create_inventory():
    """Return create page to create a new inventory item."""

    return render_template("create.html")


def edit_inventory():
    """Return edit page to edit an inventory item"""

    return render_template("edit.html")