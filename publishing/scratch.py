#uraltes Python...
# scratchFile = open("./publishing/publishing.py", "r")
# print(scratchFile.readline())
# print(scratchFile.readline())
# scratchFile.close()#Schließen der Ressource
# print(scratchFile.readline())# Error:  Operation on closed file

# #with-Statement schließt eine angeforderte Ressource automatisch
# with open("./publishing/publishing.py", "r") as scratchFile:
#     print(scratchFile.readline())
#     print(scratchFile.readline())
# #print(scratchFile.readline())# Error:  Operation on closed file


#In den meisten Fällen nötig:
try:
    with open("./publishing/publishing.py", "r") as scratchFile:
        print(scratchFile.readline())
        print(scratchFile.readline())
except:
    print("error using file")