from myapp import app
import unittest
from myapp.models import connect_to_db, db
import os

class BaseTestCase(unittest.TestCase):
    """Base Test Case."""

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