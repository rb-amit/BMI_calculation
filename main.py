# Press the green button in the gutter to run the script.

import json
import bmi_calculator as bmi_cal


def main():
    with open("humanBody_data.json", "r") as fp:
        human_body_data = fp.read()
        human_body_data = json.loads(human_body_data)

    with open("BMI_table.json", "r") as fp:
        bmi_table = fp.read()
        bmi_table = json.loads(bmi_table)

    calculator = bmi_cal.BMICalculator(bmi_table)
    bmi_human_bodies = []
    for i in range(len(human_body_data)):
        height_cm = human_body_data[i]['HeightCm']
        weight_kg = human_body_data[i]['WeightKg']
        gender = human_body_data[i]['Gender']
        bmi = calculator.calculate_bmi(height_cm, weight_kg, gender)
        risk = calculator.get_category_and_risk(bmi)
        bmi_human_bodies.append({})
        bmi_human_bodies[i].update(human_body_data[i])
        bmi_human_bodies[i].update({'bmi': bmi, 'BMI Category': risk['BMI Category'], 'Health risk': risk['Health risk']})
        # we can directly calculate overweight people here, but
        # I am storing it first in case we want to do some more calculations later
    print("Calculated BMIs")
    print(bmi_human_bodies)
    # calculate overweight people number
    num_overweight_people = calculator.count_specific_category(bmi_human_bodies, 'Overweight')
    print("Number of overweight people is: {0}".format(num_overweight_people))


if __name__ == '__main__':
    main()







