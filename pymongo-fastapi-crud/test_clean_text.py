import unittest
from cleanText import clean_text

class TestStringMethods(unittest.TestCase):

    def test_clean_text_1(self):
        mock_text = "      Text1    "
        out = clean_text(mock_text)
        self.assertEqual(out, "-Text1")
        
    def test_clean_text_2(self):
        mock_text = "    +++++++++  Text2    "
        out = clean_text(mock_text)
        self.assertEqual(out, "-Text2")

    def test_clean_text_2(self):
        mock_text = "    Text3   \n\n\n\n"
        out = clean_text(mock_text)
        self.assertEqual(out, "-Text3")

if __name__ == '__main__':
    unittest.main()