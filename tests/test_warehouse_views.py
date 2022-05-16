from myapp import app
import unittest
from myapp.models import connect_to_db, db, Warehouse
import os


class WarehouseViewsTestCase(unittest.TestCase):
    """Tests for Inventory view functions."""

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

    def test_show_new_warehouse_page(self):
        """Test return new_warehouse.html"""

        result = self.client.get("/warehouse/new")

        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<p>Create a new warehouse in your warehouse list.</p>", result.data)

    def test_new_warehouse(self):
        """Test redirect to / after creating a new warehouse item."""

        result = self.client.post("/warehouse/new", data={"name": "central"}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)

    def test_show_edit_warehouse_page(self):
        """Test return edit_warehouse.html"""    

        # Add sample data
        central = Warehouse(name="central")
        db.session.add(central)
        db.session.commit()

        result = self.client.get(f"/warehouse/{central.id}")

        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<p>Update the warehouse name.</p>", result.data)

    def test_edit_warehouse(self):
        """Test redirect to / after editing a warehouse."""

        # Add sample data
        central = Warehouse(name="central")
        db.session.add(central)
        db.session.commit()

        result = self.client.post(f"/warehouse/{central.id}", data={"id": central.id, "name": "central"}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)

    def test_delete_warehouse(self):
        """Test redircet to / after deleting an inventory item."""

        # Add sample data
        central = Warehouse(name="central", qty=500)
        db.session.add(central)
        db.session.commit()

        result = self.client.post(f"/warehouse/{central.id}/delete", data={"id": central.id}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)


if __name__ == "__main__":
    unittest.main()
