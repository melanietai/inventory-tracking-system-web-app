from myapp import app
import unittest
from myapp.models import connect_to_db, db, Warehouse
from myapp.crud.warehouse_crud import create_warehouse, get_all_warehouses, get_warehouse_by_id, update_warehouse, delete_warehouse_by_id
import os


class WarehouseCrudTestCase(unittest.TestCase):
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
        connect_to_db(app, "sqlite:///test.db")

    def setUp(self):
        # Create tables
        db.create_all()

    def tearDown(self):
        db.session.commit()
        db.drop_all()

    def test_create_warehouse(self):
        """Test create warehouse view function."""

        warehouse = create_warehouse(name="central")
        self.assertEqual("central", warehouse.name)

    def test_get_all_warehouses(self):

        # Add sample data
        central = Warehouse(name="central")
        remote = Warehouse(name="remote")
        db.session.add_all([central, remote])
        db.session.commit()

        self.assertEqual(list(get_all_warehouses()), [central, remote])

    def test_get_warehouse_by_id(self):

        # Add sample data
        central = Warehouse(name="central")
        db.session.add(central)
        db.session.commit()

        self.assertEqual(get_warehouse_by_id(id=central.id), central)

    def test_update_inventory(self):

        # Add sample data 
        remote = Warehouse(name="remote")
        db.session.add(remote)
        db.session.commit()

        # Sample data for update
        new_name = "remote-1"

        update_warehouse(id=remote.id, name=new_name)

        self.assertEqual(remote.name, "remote-1")

    def test_delete_inventory_by_id(self):

        # Add sample data
        central = Warehouse(name="central")
        db.session.add(central)
        db.session.commit()

        delete_warehouse_by_id(id=central.id)

        self.assertEqual(get_warehouse_by_id(id=central.id), None)


if __name__ == "__main__":
    unittest.main()