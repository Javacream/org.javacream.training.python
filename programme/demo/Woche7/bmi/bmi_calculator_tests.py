'''
Ablauf eines Testes
1. Definiere Eingangsdaten (Größe: 183, Gewicht 75.3)
2. Definiere das erwartete Ergebnis (-> Andere Quelle, z.B. aus der Fachvorgabe, BMI 22.485)
3. Rufe den zu testenden Algorithmus auf und merke dir das berechnete Ergebnis
4. Formuliere Annahmen / Assertions: 'Das erwartete Ergebnis ist gleich dem berechneten Ergebnis'
'''
from bmi_calculator import calculate_bmi
height = 183
weight = 75.3
expected_bmi = 22.485
calculated_bmi = calculate_bmi(height, weight)
# Problem: Wie formuliere ich die Assertion und wo schreibe ich die Testergebnisse hin?
