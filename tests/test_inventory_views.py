from myapp.models import db, Inventory
from tests.base_test_case import BaseTestCase


class InventoryViewsTestCase(BaseTestCase):
    """Tests for Inventory view functions."""

    def test_show_new_inventory_page(self):
        """Test return new_inventory.html"""

        result = self.client.get("/inventory/new")

        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h2>Create a new item in your inventory list</h2>", result.data)

    def test_new_inventory(self):
        """Test redirect to / after creating a new inventory item."""

        result = self.client.post("/inventory/new", data={"name": "Shampoo", "qty": 500}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)

    def test_show_edit_inventory_page(self):
        """Test return edit_inventory.html"""    

        # Add sample data
        shampoo = Inventory(name="shampoo", qty=500)
        db.session.add(shampoo)
        db.session.commit()

        result = self.client.get(f"/inventory/{shampoo.id}")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h2>Update the product name, quantity, or warehouse</h2>", result.data)

    def test_edit_inventory(self):
        """Test redirect to / after editing an inventory item."""

        # Add sample data
        shampoo = Inventory(name="shampoo", qty=500)
        db.session.add(shampoo)
        db.session.commit()

        result = self.client.post(f"/inventory/{shampoo.id}", data={"id": shampoo.id, "name": "Dove Shampoo", "qty": 400}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)

    def test_delete_inventory(self):
        """Test redircet to / after deleting an inventory item."""

        # Add sample data
        shampoo = Inventory(name="shampoo", qty=500)
        db.session.add(shampoo)
        db.session.commit()

        result = self.client.post(f"/inventory/{shampoo.id}/delete", data={"id": shampoo.id}, follow_redirects=True)
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)
