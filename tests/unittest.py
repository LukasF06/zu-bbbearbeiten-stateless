import unittest
from helper import add, update, Todo, items

class TestToDoMethods(unittest.TestCase):

    def setUp(self):
        self.items_count = len(items)
    
    def test_add(self):
        add("Einkaufen")
        self.assertEqual(len(items), self.items_count + 1)
        self.assertEqual(items[self.items_count].text, "Einkaufen")
        self.assertFalse(items[self.items_count].isCompleted)

    def test_update(self):
        add("Lernen")
        items_status = items[self.items_count].isCompleted
        update(self.items_count)
        self.assertNotEqual(items_status, items[self.items_count].isCompleted)
        update(self.items_count)
        self.assertEqual(items_status, items[self.items_count].isCompleted)

    def test_bbb(self):
        add("Badenfahrt")
        self.assertEqual(items[self.items_count].text, "Bbbadenfahrt")
        
if __name__ == "__main__":
    unittest.main()
    