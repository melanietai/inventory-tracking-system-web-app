"""CRUD operations for Warehouse."""

from myapp.models import db, connect_to_db, Warehouse
from sqlalchemy import update


def create_warehouse(name):
    """Create and return a warehouse."""

    warehouse = Warehouse(name=name)

    db.session.add(warehouse)
    db.session.commit()

    return warehouse


def get_all_warehouses():
    """Return all warehouses."""

    return Warehouse.query.all()


def get_warehouse_by_id(id):
    """Return a warehouse by primary key."""

    return Warehouse.query.get(id)


def update_warehouse(id, name):
    """Update a warehouse."""

    stmt = update(Warehouse).where(Warehouse.id==id).values(name= name)
    
    db.session.execute(stmt)
    db.session.commit()


def delete_warehouse_by_id(id):
    """Delete an warehouse."""

    warehouse = get_warehouse_by_id(id)

    db.session.delete(warehouse)
    db.session.commit()


if __name__ == "__main__":
    from myapp import app

    connect_to_db(app)