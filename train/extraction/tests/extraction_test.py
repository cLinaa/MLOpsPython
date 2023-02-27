import unittest

from train.extraction.extraction import extract_images_from_pdfs
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        value = 'foo'.upper()
        expected = 'FOO'
        self.assertEqual(value, expected)


    def test_something(self):
        images=extract_images_from_pdfs(str(input_directory, str(output_directory)))
        expected_result = ['0a0e5d35-ef01-4239-af60-81f2357a6ab9.pdf']
        self.assertEqual(expected_result, images)

if __name__ == '__main__':
    unittest.main()
