import people
def main():

    people_manager = people.people_manager
    people_manager.create("Goo", "Georg")
    people_manager.create("Foo", "Henry")

    search_result = people_manager.find_by_id(0)
    print(search_result.info())
    print(people_manager.delete_by_id(0))
    print(people_manager.delete_by_id(0))
if __name__ == "__main__":
    main()