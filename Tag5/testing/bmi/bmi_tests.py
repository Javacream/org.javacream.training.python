import unittest
import people_data 
import bmi 

class PeopleDataUnitTests(unittest.TestCase):
    def test_read_person_data(self):
        infile = 'Tag5/testing/bmi/people_test.csv'
        data = people_data.read_person_data(infile)
        expected_data_length = 4
        expected_name_of_second_person = 'Anna Schmidt'
        length = len(data)
        self.assertEqual(expected_data_length, length)
        self.assertEqual(expected_name_of_second_person, data[1]['name'])


    def test_write_person_data(self):
        outfile = 'Tag5/testing/bmi/test_result.txt'
        data = ['Line1', 'Line2', 'Line3']
        people_data.write_person_data(outfile, data)
        # Assertion hier nicht gut möglich, man muss sich halt die Datei anschauen. Suboptimal, aber gerade nicht zu ädnern
      

class BmiUnitTests(unittest.TestCase):
    def test_calculate_bmi(self):
        height = 1.88
        weight = 81.3
        expected_bmi = 23.00
        calculated_bmi = bmi.calculate_bmi(height, weight)
        self.assertAlmostEqual(expected_bmi, calculated_bmi, 2) # 2=gerundet auf Nachkommastellen
    def test_bmi_category_for(self):
        test_bmi = 17
        expected_category = "untergewichtig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

        test_bmi = 22
        expected_category = "normalgewichtig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

        test_bmi = 26
        expected_category = "übergewichtig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

        test_bmi = 30.5
        expected_category = "fettleibig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

if __name__ == '__main__':
    unittest.main()