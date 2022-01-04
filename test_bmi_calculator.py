import json

import unittest2
from bmi_calculator import BMICalculator


class TestBMICalculator(unittest2.TestCase):

    def test_bmi_calculation(self):
        human_body_data = [{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'bmi': 32.83},
                           {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'bmi': 32.79},
                           {'Gender': 'Female', 'HeightCm': 180, 'WeightKg': 77, 'bmi': 23.77}]
        calc = BMICalculator('BMI_table.json')
        for data in human_body_data:
            calculated_bmi = calc.calculate_bmi(height_cm=data['HeightCm'], weight_kg=data['WeightKg'],
                                                gender=data['Gender'])
            calculated_bmi = round(calculated_bmi, 2)
            self.assertEqual(calculated_bmi, data['bmi'], "Wrong BMI Calculations")

    def test_overweight_people_count(self):
        over_weight_count = 0
        human_body_data = [{'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 96},
                           {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 72},
                           {'Gender': 'Female', 'HeightCm': 180, 'WeightKg': 70}]
        expected_overweight_count = 2
        with open("BMI_table.json", "r") as fp:
            bmi_table = fp.read()
            bmi_table = json.loads(bmi_table)
        calc = BMICalculator(bmi_table)
        for data in human_body_data:
            calculated_bmi = calc.calculate_bmi(height_cm=data['HeightCm'], weight_kg=data['WeightKg'],
                                                gender=data['Gender'])
            risk = calc.get_category_and_risk(calculated_bmi)
            # print(risk)
            if risk['BMI Category'] == 'Overweight':
                over_weight_count += 1
        self.assertEqual(over_weight_count, expected_overweight_count, msg='OverWeight calculation issue')

    def test_underweight_people_count(self):
        under_weight_count = 0
        human_body_data = [{'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 25},
                           {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 72},
                           {'Gender': 'Female', 'HeightCm': 180, 'WeightKg': 70}]
        expected_underweight_count = 1
        with open("BMI_table.json", "r") as fp:
            bmi_table = fp.read()
            bmi_table = json.loads(bmi_table)
        calc = BMICalculator(bmi_table)
        for data in human_body_data:
            calculated_bmi = calc.calculate_bmi(height_cm=data['HeightCm'], weight_kg=data['WeightKg'],
                                                gender=data['Gender'])
            risk = calc.get_category_and_risk(calculated_bmi)
            # print(risk)
            if risk['BMI Category'] == 'Underweight':
                under_weight_count += 1
        self.assertEqual(under_weight_count, expected_underweight_count, msg='Underweight calculation issue')


if __name__ == '__main__':
    unittest2.main()
