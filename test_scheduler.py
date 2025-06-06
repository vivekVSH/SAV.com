import unittest
from utils import parse_timestamps

class TestUtils(unittest.TestCase):
    def test_parse_timestamps(self):
        input_str = "09:15:25,11:58:23,13:45:09,13:45:09,13:45:09,17:22:00,17:22:00"
        expected_output = {
            "09:15:25": ["09:15:25"],
            "11:58:23": ["11:58:23"],
            "13:45:09": ["13:45:09", "13:45:09", "13:45:09"],
            "17:22:00": ["17:22:00", "17:22:00"],
        }
        self.assertEqual(parse_timestamps(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()
