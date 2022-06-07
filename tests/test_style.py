import os
from typing import List

from style_test import StyleTest


class TestStyle(StyleTest):
    def get_files(self) -> List[str]:
        test_dir = os.path.dirname(__file__)
        source_dir = os.path.join(test_dir, "..", "src")
        result = []
        for directory in [test_dir, source_dir]:
            for file in os.listdir(directory):
                file = os.path.abspath(os.path.join(directory, file))
                if os.path.isfile(file):
                    result.append(file)
        return result

    def test_style(self) -> None:
        self.flake_test()
