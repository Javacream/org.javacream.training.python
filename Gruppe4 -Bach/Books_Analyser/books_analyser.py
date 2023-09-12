
duplikate=".\\duplikate.txt"
dup = open(duplikate, "w")

books = open("books.csv", "r")
lines = books.readlines()

intern={}

count=0
i=0
for line in lines:
    if count >0:
        l = line.strip()
        l = l.split (",")

        isdup=False #ist ein Dupliakt
        for item in intern:
            if l[0]==intern[item]["ISBN"]:
                isdup=True

        if isdup == False:       
            intern[i]={}
            intern[i]["ISBN"]=l[0]
            intern[i]["TITLE"]=l[1]
            intern[i]["PRICE"]=int(l[2])
            i=i+1
        else:
            dup.write(l[0]+"\n")

    count = count+1         
        
dup.close()        
# das bereinigte internal dictonary als bereinigte books_cleared.CSV erstellen
books_cleared=".\\books_cleared.csv"
b_cleared = open(books_cleared, "w")

for index in intern:
    b_cleared.write(intern[index]["ISBN"]+",") 
    b_cleared.write(intern[index]["TITLE"]+",")       
    b_cleared.write(str(intern[index]["PRICE"])+"\n")    

b_cleared.close()



# das bereinigte internal dictonary als CSV mit allen Büchern deren Titel Python enthält erstellen
books_python=".\\books_python.csv"
b_python = open(books_python, "w")

for index in intern:
    
    if "Python" in intern[index]["TITLE"]:
        b_python.write(intern[index]["ISBN"]+",") 
        b_python.write(intern[index]["TITLE"]+",")       
        b_python.write(str(intern[index]["PRICE"])+"\n")  

b_python.close()

# das bereinigte internal dictonary als CSV mit allen Büchern die teuerer als 50EUR sind erstellen
books_expensive=".\\books_expensive.csv"
b_expensive = open(books_expensive, "w")

for index in intern:
    
    if intern[index]["PRICE"] > 50:
        b_expensive.write(intern[index]["ISBN"]+",") 
        b_expensive.write(intern[index]["TITLE"]+",")       
        b_expensive.write(str(intern[index]["PRICE"])+"\n")  

b_expensive.close()


# das bereinigte internal dictonary als CSV mit dem Buch mit dem längsten und kürzesten Titel erstellen

books_min_max=".\\books_min_max.csv"
b_min_max = open(books_min_max, "w")


min = 30
max = 0
min_index =[]
max_index =[]

for index in intern:
   
    if len(intern[index]["TITLE"]) >max:
        max = len(intern[index]["TITLE"])
        max_index =index
    if len(intern[index]["TITLE"]) <min:
        min = len(intern[index]["TITLE"])
        min_index = index
    

b_min_max.write(intern[min_index]["ISBN"]+",") 
b_min_max.write(intern[min_index]["TITLE"]+",")       
b_min_max.write(str(intern[min_index]["PRICE"])+"\n")  

b_min_max.write(intern[max_index]["ISBN"]+",") 
b_min_max.write(intern[max_index]["TITLE"]+",")       
b_min_max.write(str(intern[max_index]["PRICE"])+"\n")  


b_min_max.close()


w=1