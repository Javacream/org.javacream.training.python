class StoreService(object):
    def __init__(self):
        self.store = {}
    
    def get_stock(self, category, item):
        category_dict = self.store.get(category, None)
        if not category_dict:
            return 0
        else:
            stock = category_dict.get(item, None)
            if stock:
                return stock
            else:
                return 0 
    def set_stock(self, category, item, stock):
        category_dict = self.store.get(category, None)
        if not category_dict:
            category_dict = {item:stock}
            self.store[category] = category_dict
        else:
            item_dict = category_dict[item]
            if not item_dict:
                item_dict ={item:stock}    
            else:
                item_dict[item] = stock
    def get_categories(self):
        return self.store.keys()
    def get_items_for(self, category):
        return self.store.get(category, {}).keys()