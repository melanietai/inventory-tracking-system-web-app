"""CRUD operations for Inventory."""

from myapp.models import db, connect_to_db, Inventory
from sqlalchemy import update


def create_inventory(name, qty, warehouse_id=None):
    """Create and return an inventory."""

    inventory = Inventory(name=name, qty=qty, warehouse_id=warehouse_id)

    db.session.add(inventory)
    db.session.commit()

    return inventory


def get_all_inventory():
    """Return all inventory items."""

    return Inventory.query.all()


def get_inventory_by_id(id):
    """Return an inventory item by primary key."""

    return Inventory.query.get(id)


def update_inventory(id, name, qty, warehouse_id=None):
    """Update an inventory."""

    stmt = update(Inventory).where(Inventory.id==id).values(name= name, qty= qty, warehouse_id=warehouse_id)
    
    db.session.execute(stmt)
    db.session.commit()


def delete_inventory_by_id(id):
    """Delete an inventory."""

    inventory = get_inventory_by_id(id)

    db.session.delete(inventory)
    db.session.commit()


if __name__ == "__main__":
    from myapp import app

    connect_to_db(app)