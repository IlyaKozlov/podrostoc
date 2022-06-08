import os
import unittest

from client import DedocClient
from exceptions.dedoc_exception import DedocException


class TestApi(unittest.TestCase):
    host = os.environ.get('DEDOC_HOST', 'localhost')
    client = DedocClient(dedoc_host=host, dedoc_port=1231)

    def test_bad_file(self) -> None:
        file = os.path.join(os.path.dirname(__file__), "..", "data", "file.bin")
        file = os.path.abspath(file)
        with self.assertRaises(DedocException):
            _ = self.client.parse_file(file_path=file, parameters={})

    def test_csv_file(self) -> None:
        file_name = "books.csv"
        file = os.path.join(os.path.dirname(__file__), "..", "data", file_name)
        file = os.path.abspath(file)
        result = self.client.parse_file(file_path=file, parameters={})
        self.assertEqual(1, len(result.content.tables))
        [table] = result.content.tables
        self.assertEqual(11, len(table.cells))
        self.assertEqual(file_name, result.metadata.file_name)
        self.assertListEqual("id,cat,name,price,inStock,author,series_t,sequence_i,genre_s".split(","), table.cells[0])

    def test_csv_semicolons_file(self) -> None:
        file = os.path.join(os.path.dirname(__file__), "..", "data", "books_semicolons.csv")
        file = os.path.abspath(file)
        result = self.client.parse_file(file_path=file, parameters=dict(delimiter=';'))
        self.assertEqual(1, len(result.content.tables))
        [table] = result.content.tables
        self.assertEqual(11, len(table.cells))
        self.assertListEqual("id,cat,name,price,inStock,author,series_t,sequence_i,genre_s".split(","), table.cells[0])

    def test_version(self) -> None:
        version = self.client.version
        self.assertEqual(3, len(version.split('.')))
        self.assertEqual(10, len(version))
