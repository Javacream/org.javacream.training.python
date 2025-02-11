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
        self.assertEqual(expected_name_of_second_person, data[1].name)

    def test_read_person_data_with_non_existing_file_reads_empty_list(self):
        infile = 'Tag5/testing/bmi/non-existing.csv'
        data = people_data.read_person_data(infile)
        expected_data_length = 0
        length = len(data)
        self.assertEqual(expected_data_length, length)


    def test_write_person_data(self):
        outfile = 'Tag5/testing/bmi/test_result.txt'
        data = ['Line1', 'Line2', 'Line3']
        people_data.write_person_data(outfile, data)
        # Assertion hier nicht gut möglich, man muss sich halt die Datei anschauen. Suboptimal, aber gerade nicht zu ädnern

    def test_write_to_non_existing_file_throws_exception(self):
        outfile = '/TagX/non-existing'
        data = ['Line1', 'Line2', 'Line3']
        try:
            people_data.write_person_data(outfile, data)
            self.fail("FileNotFoundError must be thrown")
        except FileNotFoundError:
            pass
    def test_categorize_fat_person(self):
        person = people_data.Person('Hugo', 99, 1.55, 'm')
        people_data.categorize(person)
        self.assertEqual(1, len(people_data.people_in_categories['fettleibig']))
        self.assertEqual(1, len(people_data.people_by_gender['m']))
    def test_categorize_underweight_person(self):
        person = people_data.Person('Hugo', 19, 1.55, 'w')
        people_data.categorize(person)
        self.assertEqual(1, len(people_data.people_in_categories['untergewichtig']))
        self.assertEqual(1, len(people_data.people_by_gender['w']))
    def test_categorize_normalweight_person(self):
        person = people_data.Person('Hugo', 78, 1.83, 'd')
        people_data.categorize(person)
        self.assertEqual(1, len(people_data.people_in_categories['normalgewichtig']))
        self.assertEqual(1, len(people_data.people_by_gender['d']))

    def test_categorize_overweight_person(self):
        person = people_data.Person('Hugo', 90, 1.83, 'm')
        people_data.categorize(person)
        self.assertEqual(1, len(people_data.people_in_categories['übergewichtig']))

class BmiUnitTests(unittest.TestCase):
    def test_calculate_bmi(self):
        height = 1.88
        weight = 81.3
        expected_bmi = 23.00
        calculated_bmi = bmi.calculate_bmi(height, weight)
        self.assertAlmostEqual(expected_bmi, calculated_bmi, 2) # 2=gerundet auf Nachkommastellen
    def test_bmi_17_has_category_underweight(self):
        test_bmi = 17
        expected_category = "untergewichtig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

    def test_bmi_22_has_category_normalweight(self):
        test_bmi = 22
        expected_category = "normalgewichtig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

    def test_bmi_26_has_category_overweight(self):
        test_bmi = 26
        expected_category = "übergewichtig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

    def test_bmi_31_has_category_obese(self):
        test_bmi = 31
        expected_category = "fettleibig"
        calculated_category = bmi.bmi_category_for(test_bmi)
        self.assertEqual(expected_category, calculated_category)

if __name__ == '__main__':
    unittest.main()