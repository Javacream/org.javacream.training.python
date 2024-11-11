# Lernpfad für Python Ausbildungsreihe

## Voraussetzungen

### Technik

* Internet-Zugang, insbesondere Zugriff auf [GitHub](https://GitHub.com/Javacream)
* Lokale Python-Installation Version 3.x
* Visual Studio Code mit installierter Python Extension von Microsoft
* Microsoft Teams, die Verwendung eines Headsets ist zu empfehlen
* Hinweis
  * Falls die technischen Voraussetzungen vom Kunden nicht erfüllt werden können können Remote Rechner verwendet werden. Hier ist im Vorfeld ein gesonderter Verbindungstest notwendig

### Teilnehmende Personen

* Sicherer Umgang mit Microsoft Teams
* Grundbegriffe der IT (Was sind Daten, was ist ein Server? Dateisystem und grundlegende Bedienung von Windows-Cmd, Powershell oder Linux Shell)
* Grundlagen der Programmierung
  * Hinweise
    * Hier sind keine vertiefende Kenntnisse aus einer anderen Sprache wie Java oder C# gemeint. Theoretisch genügen auch schon Kenntnisse der Tabellenkalkulation
    * Falls Kandidaten für die Teilnehmer noch gar keine Programmier-Affinität aufweisen ist zu überlegen, einen Tag "Grundlagen der Programmierung" anzubieten. Eine Vorabfrage der Teilnehmenden-Kenntnisse ist zu empfehlen, Fragenkatalog und Auswertung können von Cegos übernommen werden

 ### Lern-Methode

* Präsentation
* Diskussion
* Eigenständige Übungen, Übungsanteil etwa 30%
* Programmbeispiele und Musterlösungen werden pro Durchführung in einem GitHub-Repository bereitgestellt. Die Commit-Historie dokumentiert den Lernfortschritt nachvollziehbar
  * Hinweis: Die Repositories sind auch nach Ende der Schulungen verfügbar
* Lernzielkontrolle durch Abschlussübung
* Handouts zur eigenständigen Nachbearbeitung im PDF-Format
* Verwendung einer kuratierten Liste weiterer Ressourcen, insbesondere Online-Dokumentationen und -Tutorials

### Ablauf

* 5 Blöcke mit den Themen
  * Python für Einsteiger*innen
  * Python für Fortgeschrittene
  * Python Datenanalyse & Visualisierung
  * Objektorientierte Programmierung mit Python
  * Python und maschinelles Lernen
* Pro Block 8 Unterrichtseinheiten verteilt auf 2 Tage
  * Seminarzeiten 9:00 - 17:00 mit Vormittag- und Nachmittagspause je 20' sowie Mittagspause 1:15 
* Durchführung mit Microsoft Teams

## Inhalte

Jeder Hauptblock umfasst etwa 90 Minuten

### Python für Einsteiger*innen

* Einführung
    * Vorstellung der referierenden Person und der Teinehmer:innen
    * Vorstellung des Lernpfades, wo starten wir, wo geht die Reise hin? Erwartungsabfrage
    * Erster Kontakt mit Python
        * Schreiben eines ersten Programms mit Visual Studio Code
        * Starten von Programmen, integriertes Terminal
    * Übersicht: KI-Hilfsmittel zur Codegenerierung
    * Online-Ressourcen
* Variablen
  * Deklaration und Nutzen von Variablen
  * `print` und `input`
  * Umgang mit Fehlern 
  * Effizientes Programieren mit VSC
    * Python Editor (Syntax Highlighting, Code Assist) 
    * Debugger: Haltepunkte, Oberfläche, Betrachten und Ändern von Werten während des Debbuggings
* Datentypen und Operatoren
    * Literale für Zeichenketten, Ganz- und Fließkommazahlen
    * Mathematische Operatoren sowie + und * für Zahlen und Zeichenketten
    * Typ-Umwandlung mit `str`, `int` und `float`
    * Formatted Strings f'...'
* Kontrollstrukturen
    * Datentyp Boolean
    * `if-elsè`
    * Boolsche Algebra
    * Fehlerbehandlung mit `try-except`
  
* Datencontainer
    * Kategorisierung: List, Set, Dict, Tuple, Range
    * Erzeugung von Datencontainern mit Literalen und BuildIn-Funktionen
    * Iteration mit for
    * Methoden der Datencontainer
* Funktionen
    * Definition: Name, Parameter, Rückgabewert
    * Aufruf von Funktionen
    * Methoden vs BuildIn-Funktionen vs selbstdefinierte Funktionen
* Abschlussübung

### Python für Fortgeschrittene

* Module
    * import
    * Befehlsumfang einiger Standard-Module
        * os
        * datetime
        * math
    * Überblick pip und PyPi
* Dateioperationen
    * Lesen und Schreiben von Textdateien
    * Fehlerbehandlung
    * Die Module csv und json
* Objekte und Referenzen
    * Speichermodell des Python Interpreters mit Stack und Heap
    * Variablen als Referenzen auf Objekte
    * Funktionsparameter und Referenzen
* Detailwissen
    * Funktionen
        * *args und **kwargs
        * Lambda-Ausdrücke
    * Collections
        * Comprehensions
        * Sortieren
    * `with`-Statement
* Testen
    * Das Modul unittest
    * Schreiben von Tests
        * Eine kurze Einführung in die Syntax der Vererbung
        * Schreiben von TestCases
* Zugriff auf WebServices
    * Das Modul `requests`
    * Zugriff auf einen RESTful WebService
    * Lesen und Schreiben mit GET und PUT
* Zugriff auf eine relationale Datenbank
    * Das Modul `mysql-connector`
    * Kurzeinführunug in die `select`- und `insert`-Klauseln von SQL
    * Lesen und Schreiben in eine einfache Tabelle
* Abschlussübung

### Python Datenanalyse & Visualisierung

* Einführung
  * Von Rohdaten zur Story: Grundsätzlicher Ablauf einer Datenanalyse
  * Das pandas-Modul: Installation, Dokumentation, Funktionsumfang
  * Jupyter Notebooks vs Skript-Programm
* Erstes Arbeiten
  * Einlesen von CSV, JSON, Excel
  * Series und DataFrame
  * Beschreibung und Kategorisierung der Daten
Visualisierung mit Pandas und Matplotlib
  * Übersicht der unterstützten Diagramm-Typen
  * Histogramme, Linien- und Kreisdiagramme
* Aufbereitung der Rohdaten
  * Erkennen von fehlenden oder fehlerhaften Werten
  * Datenbereinigung
* Datenauswertung
  * Filtern, Formatieren und Transformieren
  * Gruppierung und Aggregation
* Fallstudien und Praxisbeispiele
* Abschlussübung
### Objektorientierte Programmierung mit Python
* Grundprinzipien der Objektorientierten Programmierung
  * Datenstrukturen, Assoziationen und Vererbung
  * Modellierung mit Klassendiagramm
  * Umsetzung einer Klasse in Python
* Objekte und Klassen
  * Konstruktoren im Detail
  * Attribute und Methoden
  * Das Klassenobjekt
* Assoziationen und Vererbung
* Dunder-Methoden
  * Kapselung
  * `__repr__`, `__eq__` und `__hash__`
* Eine Übersicht der Klassen der Python-Bibliotheken 
* Expertenwissen
  * Abstrakte Elemente
  * Protokolle
  * Mehrfachvererbung / Mixins
* Abschlussübung
### Python und maschinelles Lernen
* Einführung
  * Begriffsdefinition und Einbettung in den Komplex "Künstliche Intelligenz"
  * Abgrenzung und Gemeinsamkeiten zur Statistik
* Grundlagen des Maschinellen Lernens
  * Unterschied zwischen überwachten und unüberwachten Lernverfahren
  * Grundlagen und Anwendungsbeispiele zu Klassifikation, Regression, Clustering 
  * Trainieren und Bewerten von Modellen
* Einführung in die Statistik
  * Deskriptive Statistik (Mittelwert, Median, Abweichung und Varianz)
  * Von der Stichprobe zur Allgemeinheit: Inferenzstatistik
  * Regressionsanalyse
* Klassifizierungsmethoden
  * K-Nearest Neighbors (KNN)
  * Entscheidungsbäume
* Machine Learning mit Python-Bibliotheken
  * Deskriptive Statistik mit Pandas
  * Scikit Learn
* Neronale Netze
* Von der Korrelation zur Kausalität: Bewertung der Modelle
* Abschlussarbeit    

