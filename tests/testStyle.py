import unittest
from pathlib import Path


class TestStyle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        css_path = Path(__file__).parent.parent / "static" / "style.css"
        cls.css = css_path.read_text(encoding="utf-8")

    def test_body_layout(self):
        self.assertIn("display: flex;", self.css)
        self.assertIn("justify-content: center;", self.css)
        self.assertIn("align-items: center;", self.css)
        self.assertIn("height: 100vh;", self.css)

    def test_body_style(self):
        self.assertIn("font-family: Arial, sans-serif;", self.css)
        self.assertIn("background-color: #f0f0f0;", self.css)
        self.assertIn("margin: 0;", self.css)

    def test_calculator_container(self):
        self.assertIn(".calculator", self.css)
        self.assertIn("max-width: 600px;", self.css)
        self.assertIn("background-color: #333;", self.css)
        self.assertIn("padding: 30px;", self.css)
        self.assertIn("border-radius: 15px;", self.css)
        self.assertIn("text-align: center;", self.css)

    def test_calculator_shadow(self):
        self.assertIn("box-shadow: 0px 0px 15px 0px #000;", self.css)

    def test_title_style(self):
        self.assertIn("h1", self.css)
        self.assertIn("color: #fff;", self.css)
        self.assertIn("font-size: 36px;", self.css)
        self.assertIn("margin-bottom: 20px;", self.css)

    def test_display_style(self):
        self.assertIn("#display", self.css)
        self.assertIn("text-align: right;", self.css)
        self.assertIn("width: 100%;", self.css)
        self.assertIn("height: 80px;", self.css)
        self.assertIn("background-color: #222;", self.css)
        self.assertIn("border: none;", self.css)

    def test_buttons_grid_layout(self):
        self.assertIn(".buttons", self.css)
        self.assertIn("display: grid;", self.css)
        self.assertIn("grid-template-columns: repeat(4, 1fr);", self.css)
        self.assertIn("gap: 15px;", self.css)

    def test_button_style(self):
        self.assertIn(".btn", self.css)
        self.assertIn("padding: 30px;", self.css)
        self.assertIn("font-size: 24px;", self.css)
        self.assertIn("border-radius: 10px;", self.css)
        self.assertIn("cursor: pointer;", self.css)

    def test_button_hover(self):
        self.assertIn(".btn:hover", self.css)
        self.assertIn("background-color: #555;", self.css)

    def test_operator_style(self):
        self.assertIn(".operator", self.css)
        self.assertIn("background-color: #ff9500;", self.css)

    def test_operator_hover(self):
        self.assertIn(".operator:hover", self.css)
        self.assertIn("background-color: #e68a00;", self.css)

    def test_button_active(self):
        self.assertIn(".btn:active", self.css)
        self.assertIn("background-color: #444;", self.css)

    def test_operator_active(self):
        self.assertIn(".operator:active", self.css)
        self.assertIn("background-color: #cc7a00;", self.css)

    def test_button_transition(self):
        self.assertIn("transition: background-color 0.2s;", self.css)


if __name__ == "__main__":
    unittest.main()

