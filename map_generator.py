import pandas


class MapGenerator:
    def __init__(self):
        self.provinces_dictionary = {
            'provinces': [],
            'xcor': [],
            'ycor': []
        }

    def save_provinces_into_dictionary(self, csv):
        # Extracting provinces names and cps from .csv
        provinces_cp_data = pandas.read_csv(csv)
        # Modifying Series refactoring data into a list
        provinces_list = provinces_cp_data['LITERAL'].to_list()
        # Saving each province into our dictionary
        self.provinces_dictionary['provinces'] = provinces_list

    def save_click_into_coordinates(self, x, y):
        # Now we are going to save each province coordinates into our dictionary
        self.provinces_dictionary['xcor'].append(x)
        self.provinces_dictionary['ycor'].append(y)

    def generate_final_csv(self, country):
        # We use pandas to convert our dictionary to a .csv with all the info
        data = pandas.DataFrame(self.provinces_dictionary)
        data.to_csv(f'{country}_prov.csv', index=False)
