"""CRUD operations."""

from myapp.models import db, connect_to_db, Inventory


def create_inventory(name, qty):
    """Create and return an inventory."""

    inventory = Inventory(name=name, qty=qty)

    db.session.add(inventory)
    db.session.commit()

    return inventory


def get_all_inventory():
    """Return all inventory items."""

    return Inventory.query.all()


def get_inventory_by_id(id):
    """Return an inventory item by primary key."""

    return Inventory.query.get(id)


if __name__ == "__main__":
    from myapp import app

    connect_to_db(app)