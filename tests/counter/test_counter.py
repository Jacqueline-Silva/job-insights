from src.counter import count_ocurrences
from unittest.mock import patch, mock_open


def test_counter():
    text = "Lorem python et nisl qPyq PYThOn massa molestie python"
    with patch("builtins.open", mock_open(read_data=text)):
        assert count_ocurrences("src/jobs.csv", "py") == 4
