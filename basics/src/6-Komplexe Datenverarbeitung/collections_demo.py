beatles = {"John": "Rhythm Guitar", "Paul": "Bass", 
           "George": "Lead Guitar", "Ringo": "Drums"}
instruments = list(map(lambda name: beatles.get(name), beatles))
instruments.sort(reverse=False)
print(instruments)