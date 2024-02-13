import json
def main():
    #returns all data
    def data_overview():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json_file.read()
            print(data)

    def people_count():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json.load(json_file)
            id_count = len(data)
            print(id_count)

    def gender_count():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json.load(json_file)
            
            #count by gender
            gender_count = {}

            for item in data:
                gender = item["gender"]
                gender_count[gender] = gender_count.get(gender, 0) + 1
            
            #print the results
            for gender, count in gender_count.items():
                print(f"{gender}: {count}")

            #question: how can I use list comprehension at this point?
    
    def concat_names():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json.load(json_file)
            #concat the names into a list
            full_names = [item['firstname'] + ' ' + item['lastname'] for item in data]
            # Print the list
            print(full_names)
    
    def max_min_height():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json.load(json_file)  
            heights = [person["height"] for person in data]  # Extract heights from each dictionary
            max_height = str(max(heights)) # Calculate the maximum height
            min_height= str(min(heights)) #calculate the minimum height
            print("max: " + max_height + ", min: " + min_height)
            #why is there an error with load?
            #how can I use list comprehension here?

    def avg_height():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json.load(json_file)  
            heights = [person["height"] for person in data]  # Extract heights from each dictionary
            average_height = sum(heights) / len(heights)  # Calculate the average height
            print(average_height)
            #why is there an error with load?
            #how can I use list comprehension here?

    data_overview()
    people_count()
    gender_count()
    concat_names()
    max_min_height()
    avg_height()
main()