from flask import (render_template, request, redirect, flash)
from myapp.crud import inventory_crud, warehouse_crud


def show_new_inventory_page():
    """Return new_inventory page to create a new inventory item."""

    warehouses = warehouse_crud.get_all_warehouses()
    return render_template("new_inventory.html", warehouses=warehouses)


def new_inventory():
    """Create a new inventory."""

    name = request.form.get('name')
    qty = request.form.get('qty')
    warehouse_id = request.form.get("warehouse-id") or None
    inventory_crud.create_inventory(name=name, qty=qty, warehouse_id=warehouse_id)
    

    flash("New item successfully added!")

    return redirect("/")


def show_edit_inventory_page(id):
    """Return an inventory item to edit_inventory page"""

    inventory = inventory_crud.get_inventory_by_id(id=id)
    warehouses = warehouse_crud.get_all_warehouses()
    current_warehouse = inventory.warehouse

    return render_template("edit_inventory.html", inventory=inventory, current_warehouse=current_warehouse, warehouses=warehouses)
    
    
def edit_inventory(id):
    """Edit an inventory item in database and redirect to homepage."""

    name = request.form.get("name")
    qty = request.form.get("qty")
    warehouse_id = request.form.get("warehouse-id") or None

    inventory_crud.update_inventory(id=id, name=name, qty=qty, warehouse_id=warehouse_id)
    flash("Item successfuly edited!")

    return redirect("/")


def delete_inventory(id):
    """Delete an inventory item in database and flash message."""

    inventory_crud.delete_inventory_by_id(id=id)
    flash("Item succesfully deleted!")

    return redirect("/")