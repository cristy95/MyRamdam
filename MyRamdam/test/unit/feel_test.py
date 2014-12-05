import unittest
from feel import Feel


class TestFeel(unittest.TestCase):

    def test_get_feeling(self):
        feel = Feel(001, "happy")
        feel_id = 001
        self.assertEqual(feel.get_feeling(feel_id), 'happy')

    def test_add_feeling(self):
        feel = Feel(001, "happy")
        feel_id = 001
        self.assertEqual(feel.add_feeling(feel_id), 'OK')
