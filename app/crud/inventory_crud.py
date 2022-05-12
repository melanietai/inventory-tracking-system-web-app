"""CRUD operations."""

from models import db, connect_to_db, Inventory


if __name__ == "__main__":
    from run import app

    connect_to_db(app)