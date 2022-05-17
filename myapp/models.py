"""Models.

A many-to-one relationship.
An inventory item will be associated with one warehouse.
A warehouse can have many inventory items.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Inventory(db.Model):
    """An inventory."""
    
    __tablename__="inventories"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.id"))

    warehouse = db.relationship("Warehouse", backref=backref("inventories", cascade="all, delete"))

    def __repr__(self):
        return f"<Inventory id={self.id} name={self.name} qty={self.qty}>"


class Warehouse(db.Model):
    "A warehouse."

    __tablename__="warehouses"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # inventories = a list of Inventory objects

    def __repr__(self):
        return f"<Warehouse id={self.id} name={self.name}>"


def connect_to_db(flask_app, db_uri="sqlite:///inventory.db", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__=="__main__":
    from myapp import app

    connect_to_db(app)