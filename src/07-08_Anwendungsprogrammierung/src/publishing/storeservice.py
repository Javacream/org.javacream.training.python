from publishing.utilities import checkNoneOrEmptyParameter


class StoreService(object):
    def __init__(self):
        self.store = {}
    
    def get_stock(self, category, item):
        checkNoneOrEmptyParameter(category, "category")
        checkNoneOrEmptyParameter(item, "item")
        categoryDict = self.store.get(category, None)
        if not categoryDict:
            return 0
        else:
            stock = categoryDict.get(item, None)
            if stock:
                return stock
            else:
                return 0 