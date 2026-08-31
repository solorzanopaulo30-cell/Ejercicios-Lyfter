import unittest
from unittest.mock import patch, mock_open
from read_lines import read_lines


class TestReadLines(unittest.TestCase):

    def test_read_lines_returns_expected_content(self):
        # Arrange
        fake_content = "linea1\nlinea2\nlinea3\n"
        # Act & Assert
        with patch("builtins.open", mock_open(read_data=fake_content)):
            result = read_lines("archivo_falso.txt")
            self.assertEqual(result, ["linea1\n", "linea2\n", "linea3\n"])

    def test_read_lines_raises_file_not_found(self):
        # Arrange
        # Act & Assert
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_lines("no_existe.txt")


if __name__ == '__main__':
    unittest.main()

