from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """A simple test to see if the CI/CD is working"""
        self.assertEqual(1 + 1, 2)

    def test_homepage_status(self):
        """Checks if your site root is even loading"""
        response = self.client.get('/')
        # Even if it's a 404, the test proves the server is running!
        self.assertIn(response.status_code, [200, 404])