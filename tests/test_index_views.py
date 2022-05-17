from tests.base_test_case import BaseTestCase

class IndexViewsTestCase(BaseTestCase):
    """Tests for Index view functions."""

    def test_index(self):
        """Test return index.html"""

        result = self.client.get("/")
        
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"<h1>Welcome to your inventory tracking system</h1>", result.data)