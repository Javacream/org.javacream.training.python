from publishing_service import PublishingService
def main():
    publishing_service = PublishingService()
    publishing_service.load()
    print(publishing_service.books_more_expensive_than(20))
    print(publishing_service.authors_for_publisher(publishing_service.publishers[1]))
    print(publishing_service.authors_for_publisher_with_lastname(publishing_service.publishers[2], 'Schneider'))
    print('done')
    publishing_service.save()
if __name__ == '__main__': 
    main() 
