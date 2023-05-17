import unittest

class TestDemo(unittest.TestCase):
    def testSimple(self):
        # Definition der Ausgangsdaten
        inputData = "HUGo"
        # Bestimmung eines Ergebnisses durch Aufruf der zu testenden Logik
        result = inputData.isupper()
        # Erwartung
        expected = True
        # Assertion = Prüfung: Erwartung gegen Result
        self.assertEqual(expected, result)

    def testSimple2(self):
        # Definition der Ausgangsdaten
        inputData = "HUGO"
        # Bestimmung eines Ergebnisses durch Aufruf der zu testenden Logik
        result = inputData.isupper()
        # Erwartung
        expected = True
        # Assertion = Prüfung: Erwartung gegen Result
        self.assertEqual(expected, result)

    def testSimple3(self):
        # Definition der Ausgangsdaten
        inputData = "HUGO"
        # Bestimmung eines Ergebnisses durch Aufruf der zu testenden Logik
        result = inputData.isupper()
        # Erwartung
        expected = True
        # Assertion = Prüfung: Erwartung gegen Result
        self.assertEqual(expected, result)

#TestDemo().testScratch()

# Typisches Python-Idiom zum Ausführen eines Unit-Tests
if __name__ == '__main__':
    unittest.main()
