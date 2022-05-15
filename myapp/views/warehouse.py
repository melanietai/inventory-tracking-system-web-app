from flask import (render_template, request, redirect, flash)
from myapp.crud import warehouse_crud


def show_new_warehouse_page():
    """Return new_warehouse page to create a new warehouse."""

    return render_template("new_warehouse.html")


def new_warehouse():
    """Create a new warehouse."""

    name = request.form.get('name')

    warehouse_crud.create_warehouse(name=name)

    flash("New warehouse successfully added!")

    return redirect("/")



def show_edit_warehouse_page(id):
    """Return a warehouse to edit_inventory page"""

    warehouse = warehouse_crud.get_warehouse_by_id(id=id)

    return render_template("edit_warehouse.html", warehouse=warehouse)
    
    
def edit_warehouse(id):
    """Edit a warehouse in database and redirect to homepage."""

    name = request.form.get("name")

    warehouse_crud.update_warehouse(id=id, name=name)
    flash("Warehouse successfuly edited!")

    return redirect("/")


def delete_warehouse(id):
    """Delete a warehouse in database and flash message."""

    warehouse_crud.delete_warehouse_by_id(id=id)
    flash("Warehouse succesfully deleted!")

    return redirect("/")
