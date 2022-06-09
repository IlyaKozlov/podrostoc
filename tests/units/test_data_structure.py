import json
import os
import unittest

from podrostoc.data_structures.parsed_document import ParsedDocument


class TestDataStructure(unittest.TestCase):

    def test_response(self) -> None:
        path = os.path.join(os.path.dirname(__file__), "..", "data", "response.json")
        path = os.path.abspath(path)
        with open(path) as file:
            response = json.load(file)
        result = ParsedDocument(**response)
        self.assertEqual(["test warning"], result.warnings)
        self.assertEqual("doc_uid_auto_d95c17e0-e65c-11ec-874b-0242ac170002", result.metadata.uid)
        self.assertListEqual(["N", "Фамилия", "Имя", "Организация", "Телефон", "Примечания"],
                             result.content.tables[0].cells[0])
