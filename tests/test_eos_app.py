import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
import argparse
from module import (
    save_to_csv,
    save_to_json,
    main,
    FileExtensionError,
    NotTwoDimensionalArrayError,
    OutputFileExistsError
)


class TestFileIO(unittest.TestCase):
    """Test for input\output files with path and data """

    def setUp(self) -> None:
        """SetUp with path & data to context managers"""

        self.path_csv = "test.csv"
        self.path_json = "test.json"
        self.data = [[1, 2], [3, 4]]

    def tearDown(self) -> None:
        """Check and clear after test case end"""

        if os.path.exists(self.path_csv):
            os.remove(self.path_csv)
        if os.path.exists(self.path_json):
            os.remove(self.path_json)

    def test_save_to_csv(self) -> None:
        """Should check, create and save data by path to file.csv format"""

        save_to_csv(self.path_csv, self.data)
        with open(self.path_csv) as csv_file:
            content = csv_file.read()
        expected_output = "1,2\n3,4\n"
        self.assertEqual(content, expected_output)

    def test_save_to_json(self) -> None:
        """Should check, create and save data by path to file.json format"""

        save_to_json(self.path_json, self.data)
        with open(self.path_json) as file:
            content = file.read()
        expected_output = "[[1, 2], [3, 4]]"
        self.assertEqual(content, expected_output)

    def test_main_json(self) -> None:
        """Should check and create json file by Cli interface"""

        with patch("argparse.ArgumentParser.parse_args",
                   return_value=argparse.Namespace(
                       path=self.path_json, data="[[1,2],[3,4]]")
                   ):
            with redirect_stdout(StringIO()) as out:
                main()
        expected_output = f"Create new file: {self.path_json}\n"
        self.assertEqual(out.getvalue(), expected_output)

    def test_main_file_exists(self) -> None:
        """Should check and raise exception if file exist"""

        with open(self.path_csv, "w") as file:
            file.write("")
        with patch("argparse.ArgumentParser.parse_args",
                   return_value=argparse.Namespace(
                       path=self.path_csv, data="[[1,2],[3,4]]")
                   ):
            with self.assertRaises(OutputFileExistsError):
                main()

    def test_main_file_extension_error(self) -> None:
        """Should check `.scv & .json` file format"""

        with patch("argparse.ArgumentParser.parse_args",
                   return_value=argparse.Namespace(
                       path="test.txt", data="[[1,2],[3,4]]")
                   ):
            with self.assertRaises(FileExtensionError):
                main()

    def test_main_not_two_dimensional_array_error(self) -> None:
        """Should check and rise exception if
         data not in two-dimensional list"""

        with patch("argparse.ArgumentParser.parse_args",
                   return_value=argparse.Namespace(
                       path=self.path_json, data="[1,2]")
                   ):
            with self.assertRaises(NotTwoDimensionalArrayError):
                main()
