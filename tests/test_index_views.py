from myapp import app
import unittest
from myapp.models import connect_to_db, db
import os

class IndexViewsTestCase(unittest.TestCase):
    """Tests for Index view functions."""

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

    def test_index(self):
        """Test return index.html"""

        result = self.client.get("/")
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)