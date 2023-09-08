import sys
import person
def main():
    print("usage: python person.py lastname firstname height-range (min-max), weight")
    try:
        args = sys.argv
        lastname_criterion = args[1]
        firstname_criterion = args[2]
        height_range = args[3].split("-")
        min_height = int(height_range[0])
        max_height = int(height_range[1])
        weight = int(args[4])
        people_manager = person.PeopleManager()
        person.write_result("filtered_by_lastname_" + lastname_criterion + ".txt", people_manager.find_by_lastname(lastname_criterion))
        person.write_result("filtered_by_firstname_" + firstname_criterion + ".txt", people_manager.find_by_firstname(firstname_criterion))
        person.write_result("filtered_by_height-range_" + args[3] + ".txt", people_manager.find_by_height_range(min_height, max_height))
        person.write_result("filtered_by_weight_" + args[4] + ".txt", people_manager.find_heavier_than(weight))
    except Exception as e:
        print (str(e))    

main()