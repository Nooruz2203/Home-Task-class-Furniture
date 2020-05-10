class House:
    def __init__(self, household_type, total_area, furniture_names_list):
        self.household_type = household_type
        self.total_area = total_area
        self.remaining_area = total_area
        self.furniture_names_list = furniture_names_list

    def furniture(self):
        for furniture in self.furniture_names_list:
            if furniture == 'Bed':
                self.remaining_area -= 4
            elif furniture == 'Wardrobe':
                self.remaining_area -= 2
            elif furniture == 'Table':
                self.remaining_area -= 1.5
        print(f'household_type:{self.household_type}, total_area = {self.total_area}, remaining_area: {self.remaining_area}, furniture_name_list: {self.furniture_names_list}')            

house = House('Bedroom', 40, ['Bed', 'Wardrobe', 'Table'])
house.furniture()



