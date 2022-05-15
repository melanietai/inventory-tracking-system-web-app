from flask import (render_template)
from myapp.crud import warehouse_crud, inventory_crud


def index():
    """Return all inventory items and warehouses to homepage."""

    all_inventory = inventory_crud.get_all_inventory()
    warehouses = warehouse_crud.get_all_warehouses()

    return render_template("index.html", all_inventory=all_inventory, warehouses=warehouses)