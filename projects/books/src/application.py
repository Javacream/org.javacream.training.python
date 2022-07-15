
from javacream.storeservice import StoreService


if __name__ == '__main__':
    store_service = StoreService()
    print (store_service.get_stock("this", "that"))