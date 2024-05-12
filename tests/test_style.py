import os
from typing import List

from utils import StyleTest


class TestStyle(StyleTest):
    def get_files(self) -> List[str]:
        test_dir = os.path.dirname(__file__)
        source_dir = os.path.join(test_dir, "..", "podrostoc")
        result = []
        for directory in [test_dir, source_dir]:
            for root, _, files in os.walk(directory):
                for file in files:
                    file = os.path.abspath(os.path.join(root, file))
                    if os.path.isfile(file) and file.endswith(".py"):
                        result.append(file)
        return result

    def test_style(self) -> None:
        self.flake_test()
