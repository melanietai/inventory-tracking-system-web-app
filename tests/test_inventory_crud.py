from myapp import app
import unittest
from myapp.models import connect_to_db, db, Inventory
from myapp.crud.inventory_crud import create_inventory, get_all_inventory, get_inventory_by_id, update_inventory, delete_inventory_by_id
import os


class InventoryCrudTestCase(unittest.TestCase):
    """Tests for Inventory crud functions."""

    @classmethod
    def setUpClass(cls):
        # Get the Flask test client
        cls.client = app.test_client()
        app.config["TESTING"] = True

        # Create test database tables
        os.system("dropdb testdb")
        os.system('createdb testdb')

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

    def setUp(self):
        # Create tables
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()

    def test_create_inventory(self):
        """Test create inventory view function."""

        inventory = create_inventory(name="shampoo", qty=500)
        self.assertEqual("shampoo", inventory.name)
        self.assertEqual(500, inventory.qty)

    def test_get_all_inventory(self):

        # Add sample data
        shampoo = Inventory(name="Shampoo", qty=500)
        napkins = Inventory(name="Napkins", qty=100)
        db.session.add_all([shampoo, napkins])
        db.session.commit()

        self.assertEqual(list(get_all_inventory()), [shampoo, napkins])

    def test_get_inventory_by_id(self):

        # Add sample data
        shampoo = Inventory(name="Shampoo", qty=500)
        db.session.add(shampoo)
        db.session.commit()

        self.assertEqual(get_inventory_by_id(id=shampoo.id), shampoo)

    def test_update_inventory(self):

        # Add sample data 
        shampoo = Inventory(name="Shampoo", qty=500)
        db.session.add(shampoo)
        db.session.commit()

        # Sample data for update
        new_name = "Dove Shampoo"
        new_qty = 400

        update_inventory(id=shampoo.id, name=new_name, qty=new_qty)

        self.assertEqual(shampoo.name, "Dove Shampoo")
        self.assertEqual(shampoo.qty, 400)

    def test_delete_inventory_by_id(self):

        # Add sample data
        shampoo = Inventory(name="Shampoo", qty=500)
        db.session.add(shampoo)
        db.session.commit()

        delete_inventory_by_id(id=shampoo.id)

        self.assertEqual(get_inventory_by_id(id=shampoo.id), None)


if __name__ == "__main__":
    unittest.main()