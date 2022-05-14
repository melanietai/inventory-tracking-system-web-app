from flask import (render_template, request, redirect, flash)
from myapp.crud import inventory_crud


def index():
    """Return all inventory items to homepage."""

    all_inventory = inventory_crud.get_all_inventory()

    return render_template("index.html", all_inventory=all_inventory)


def show_create_inventory_page():
    """Return create page to create a new inventory item."""

    return render_template("create.html")


def create_inventory():
    """Create a new inventory."""

    name = request.form.get('name')
    qty = request.form.get('qty')

    inventory_crud.create_inventory(name=name, qty=qty)

    flash("New item successfully added!")

    return redirect("/")



def show_edit_inventory_page(id):
    """Return an inventory item to edit page"""

    inventory = inventory_crud.get_inventory_by_id(id=id)

    return render_template("edit.html", inventory=inventory)
    
    
def edit_inventory(id):
    """Edit an inventory item in database and redirect to homepage."""

    name = request.form.get("name")
    qty = request.form.get("qty")

    inventory_crud.update_inventory(id=id, name=name, qty=qty)
    flash("Item successfuly edited!")

    return redirect("/")


def delete_inventory(id):
    """Delete an inventory item in database and flash message."""

    inventory_crud.delete_inventory_by_id(id=id)
    flash("Item succesfully deleted!")

    return redirect("/")


