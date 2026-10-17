import unittest
from pathlib import Path
from app import app

class TestCalculatorPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        cls.client = app.test_client()
        cls.project_dir = Path(__file__).parent.parent

    def test_homepage_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_page_contains_calculator_title(self):
        response = self.client.get("/")
        self.assertIn(b"Flask Calculator", response.data)

    def test_page_contains_display(self):
        response = self.client.get("/")
        self.assertIn(b'id="display"', response.data)

    def test_page_contains_number_buttons(self):
        response = self.client.get("/")
        for number in "0123456789":
            with self.subTest(number=number):
                self.assertIn(
                    f"appendToDisplay('{number}')".encode(),
                    response.data
                )

    def test_page_contains_operators(self):
        response = self.client.get("/")
        for operator in ["+", "-", "*", "/"]:
            with self.subTest(operator=operator):
                self.assertIn(
                    f"appendToDisplay('{operator}')".encode(),
                    response.data
                )

    def test_page_contains_clear_button(self):
        response = self.client.get("/")
        self.assertIn(b"clearDisplay()", response.data)

    def test_page_contains_submit_button(self):
        response = self.client.get("/")
        self.assertIn(b'type="submit"', response.data)

    def test_css_file_exists(self):
        css_path = self.project_dir / "static" / "style.css"
        self.assertTrue(css_path.is_file())

    def test_css_is_accessible(self):
        response = self.client.get("/static/style.css")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b".calculator", response.data)

if __name__ == "__main__":
    unittest.main()