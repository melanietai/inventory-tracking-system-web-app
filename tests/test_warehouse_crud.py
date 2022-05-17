from myapp.models import db, Warehouse
from myapp.crud.warehouse_crud import create_warehouse, get_all_warehouses, get_warehouse_by_id, update_warehouse, delete_warehouse_by_id
from tests.base_test_case import BaseTestCase


class WarehouseCrudTestCase(BaseTestCase):
    """Tests for Inventory crud functions."""

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