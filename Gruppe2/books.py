import csv

class Buch:
    """
        Ein Buch mit den Attributen:
        ISBN: String
        Titel: String
        Betrag: String
    """
    def __init__(self, StrISBN, StrTitel, StrBetrag): #Constructor / address ist ein optionaler Parameter
        self.ISBN = StrISBN
        self.Titel = StrTitel
        self.Betrag = StrBetrag

class BuchManager:
    """
        Ein BuchManager mit den Attributen:
        Buecher: dict()
        BuchID: int
    """
    def __init__(self):
        self.Buecher = dict()
        self.BuchID = 0
        self.__Initialisierung__()

    def __Initialisierung__(self):
        """
            Mit dem Inhalt der Datei books.csv werden Buch-Instanzen erzeugt und die Referenzen im BuchManager.Buecher dict abgelegt.
        """
        try:
            with open('books.csv') as csvdatei:
                csv_reader_object = csv.reader(csvdatei, delimiter=',')              
                for row in csv_reader_object:
                    self.Buecher[self.BuchID] = Buch(*row)
                    
                    self.BuchID += 1  
        except:
            print("Es ist ein unerwarteter Fehler aufgetreten!") 
        #Überschriftenzeile löschen
        self.Buecher.pop(0)         

    def SearchForDuplicates(self):
        """
            Doppelte Einträge werden gesucht und die ISBN Nummern als set zurückgegeben.
        """
        doppeltebuecher = set()
        return [buch.ISBN for buch in self.Buecher.values() if buch.ISBN in doppeltebuecher or (doppeltebuecher.add(buch.ISBN) or False)]

    def SearchForTitel(self, Title):
        """
            Die ISBN Nummern der Bücher die im Titel >>Title<< enthalten werden als Liste zurückgegeben.
        """        
        return [buch.ISBN for buch in self.Buecher.values() if Title in buch.Titel]

    def SearchExpensiveBooks(self, Costs):
        """
            Die ISBN Nummern der teueren Bücher werden als Liste zurückgegeben.
        """
        return [buch.ISBN for buch in self.Buecher.values() if Costs > int(buch.Betrag)]

    def DeleteDoubleEntries(self, ListDoppelteBuecher):
        """
            Doppelte Bücher werden aus dem dict des BuchManagers gelöscht
        """        
        SetZuLoeschendeBuecher = set()
        for buffer in self.Buecher:
            AktuellesBuch = self.Buecher.get(buffer) 
            for DoppelteISBN in ListDoppelteBuecher:
                #print(DoppelteISBN, AktuelleISBN.ISBN)
                if AktuellesBuch.ISBN == DoppelteISBN:
                    SetZuLoeschendeBuecher.add(buffer)
        
        for ZuLoeschendeBuecher in SetZuLoeschendeBuecher:
            try:
                self.Buecher.pop(ZuLoeschendeBuecher)
            except:
                pass        
    
    def AktuelleListeDerBuecher(self):
        """
            Die ISBN Nummern sämtlicher Bücher werden als Liste zurückgegeben.
        """        
        ListeISBN = list()
        for buffer in self.Buecher:
            AktuelleISBN = self.Buecher.get(buffer)
            ListeISBN.append(AktuelleISBN.ISBN) 
        return ListeISBN        

    def GetAverageBookPrice(self):
        """
            Der durchschnittliche Buchpreis wird errechnet und zurückgegeben
        """        
        SummeDerKosten = 0
        AnzahlDerBuecher = 0
        for buffer in self.Buecher:
            AktuellesBuch = self.Buecher.get(buffer)
            SummeDerKosten = SummeDerKosten + int(AktuellesBuch.Betrag)
            AnzahlDerBuecher += 1
        return SummeDerKosten / AnzahlDerBuecher

    def GetMinMaxTitle(self):
         """
            Die ISBN Nummern der Bücher mit dem kürzesten und längsten Titeln werden als Liste zurückgegeben.
         """         
         BuchTitelLaengen = [len(buch.Titel) for buch in self.Buecher.values()]
         BuchMax = max(BuchTitelLaengen)
         BuchMin = min(BuchTitelLaengen)
         BuchTitelISBNMax = [buch.ISBN for buch in self.Buecher.values() if BuchMax == len(buch.Titel)]
         BuchTitelISBNMin = [buch.ISBN for buch in self.Buecher.values() if BuchMin == len(buch.Titel)]
         return "Kürzeste Bücher: " + str(BuchTitelISBNMin) + "\nLängeste Bücher: " + str(BuchTitelISBNMax)

def WriteTXT(Daten, DateiName):
    """
        Eine Textdatei wird erzeugt / überschrieben.
        Datei Name: >>DateiName<<
        Datei Inhalt: >>Daten<<
    """
    with open(DateiName, 'w', encoding="UTF8") as Datei:
        Datei.write(str(Daten))