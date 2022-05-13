from flask import (render_template, request, redirect)
from myapp.crud import inventory_crud


def index():
    """Return all inventory items to homepage."""

    all_inventory = inventory_crud.get_all_inventory()

    return render_template("index.html", all_inventory=all_inventory)


def create_inventory():
    """Return create page to create a new inventory item."""



    return render_template("create.html")


def view_inventory(id):
    """Return an inventory item to edit page"""

    inventory = inventory_crud.get_inventory_by_id(id)

    return render_template("edit.html", inventory=inventory)
    
    
def edit_inventory(id):
    """Edit inventory in database and redirect to homepage."""

    name = request.form.get("name")
    qty = request.form.get("qty")

    inventory_crud.update_inventory(id=id, name=name, qty=qty)

    return redirect ("/")