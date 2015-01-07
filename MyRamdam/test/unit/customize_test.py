import unittest
from myramdam.newfeel import Feel

class TestCustFeel(unittest.TestCase):
    
    def test_if_new_feeling_is_added(self):
        feel = NewFeel("incomplete", "sad")
        self.assertEqual(feel.addFeel(feel), "OK")

    def test_feeling_leaning_towards(self):
        feel = NewFeel("incomplete", "sad")
        self.assertEqual(feel.add_feeling(feel), "OK")
        self.assertEqual(feel.getLeanFeel(cfeel_id), "sad")