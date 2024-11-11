import unittest

from pipelines.ingestion import get_path_for_csv_file


class TestDataIngestionFunctions(unittest.TestCase):
    def test_get_path_for_csv_file_returns_path_accordingly(self):
        path = get_path_for_csv_file('data.csv', './work/')

        self.assertEqual(path, "./work/extracted/data.csv")

    def test_get_path_for_csv_file_returns_string(self):
        path = get_path_for_csv_file('data.csv', './work/')

        self.assertIsInstance(path, str)
