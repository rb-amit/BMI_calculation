class BMICalculator:

    def __init__(self, bmi_table, average_height):
        self.bmi_table = bmi_table
        self.average_height = average_height

    def get_category_and_risk(self, bmi):

        # using binary search to find range optimally
        def get_bmi_table_index(bmi_table, l, r, bmi):
            if r < l:
                return -1
            mid = l+(r-l)//2
            if self.bmi_table[mid]["BMI Range"][0] <= bmi <= self.bmi_table[mid]["BMI Range"][1]:
                return mid
            elif bmi < self.bmi_table[mid]["BMI Range"][0]:
                return get_bmi_table_index(bmi_table, 0, mid-1, bmi)
            else:
                return get_bmi_table_index(bmi_table, mid+1, r, bmi)

        # For now we are using same table for male and female candidates
        idx = get_bmi_table_index(self.bmi_table, 0, len(self.bmi_table)-1, bmi)
        return self.bmi_table[idx]

    def refactor_bmi_with_height(function):
        def inner(self, height, weight, gender='Male'):
            bmi = function(self, height, weight, gender)
            if height < self.average_height:
                bmi = bmi - bmi*0.1
            elif height > self.average_height:
                bmi = bmi + bmi*0.1
            return bmi
        return inner

    @refactor_bmi_with_height
    def calculate_bmi(self, height_cm, weight_kg, gender='Male'):
        # for now we are treating same formula to calculate bmi for Male and Female
        bmi = weight_kg/((height_cm/100)**2)
        return bmi

    @staticmethod
    def count_specific_category(bmi_category, specific_category):
        num_specific_category_people = 0
        for bmi_result in bmi_category:
            if bmi_result['BMI Category'] == specific_category:
                num_specific_category_people += 1
        return num_specific_category_people


