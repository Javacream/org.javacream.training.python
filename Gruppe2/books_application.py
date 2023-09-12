import books

def cleanup(BM, Liste):
    #Doppelte Einträge entfernen
    BM.DeleteDoubleEntries(Liste)  

def analysis(BM):
    #Ausgabe der korrigierten Liste
    books.WriteTXT(BM.AktuelleListeDerBuecher(), 'KorrigierteISBN.txt')
    
    #Ermittlung der Buchtitel die "Python" enthalten
    books.WriteTXT(BM.SearchForTitel("Python"), 'python_books.txt')
    
    #Ermittlung der teuersten Bücher
    books.WriteTXT(BM.SearchExpensiveBooks(50), 'expensive_books.txt')
    
    #Ermittlung des Durchschnittlichen Buchpreises.
    books.WriteTXT(BM.GetAverageBookPrice(), 'average_book_price.txt')

    #Ermittlung des kürzesten/längsten Buchtitels
    books.WriteTXT(BM.GetMinMaxTitle(), 'min_max.txt')


def main():
    #BuchManager erzeugen
    BM = books.BuchManager()
    
    #Liste doppelter Einträge ermitteln
    ListDoppelteBuecher = BM.SearchForDuplicates() 
    
    #Liste doppelter Einträge ausgeben
    books.WriteTXT(ListDoppelteBuecher, 'DoppeltISBN.txt') 
    
    #Doppelte Einträge entfernen
    cleanup(BM, ListDoppelteBuecher)
    #Analysen der korrigierten Liste
    analysis(BM)

main()