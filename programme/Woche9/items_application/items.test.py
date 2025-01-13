import unittest
import random
from items import ItemService

class ItemServiceTests(unittest.TestCase):
    def test_sequence(self):
        item_service = ItemService()
        NAME = f'CD {random.randint(0, 10000000)}'
        PRICE = 19
        generated_item_id = item_service.create(NAME, PRICE)
        self.assertIsNotNone(generated_item_id)
        item = item_service.find_by_id(generated_item_id)
        self.assertEqual(NAME, item.name)
        items = item_service.find_by_name(NAME)
        self.assertEqual(1, len(items))

if __name__ == '__main__':
    unittest.main()        
