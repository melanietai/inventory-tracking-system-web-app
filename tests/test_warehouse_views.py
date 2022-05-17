from myapp.models import db, Warehouse
from tests.base_test_case import BaseTestCase


class WarehouseViewsTestCase(BaseTestCase):
    """Tests for Inventory view functions."""

    def test_show_new_warehouse_page(self):
        """Test return new_warehouse.html"""

        result = self.client.get("/warehouse/new")

        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h2>Create a new warehouse in your warehouse list</h2>", result.data)

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
        self.assertIn(b"<h2>Update the warehouse name</h2>", result.data)

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
        central = Warehouse(name="central")
        db.session.add(central)
        db.session.commit()

        result = self.client.post(f"/warehouse/{central.id}/delete", data={"id": central.id}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)