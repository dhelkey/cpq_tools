import unittest
from pathlib import Path
from cpq_tools.data_functions import process_excel_variable_file


class TestDataFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_folder = Path(__file__).parent / 'data'
        excel_file_path = data_folder / 'birth_key.xlsx'
        cls.variable_description, cls.variable_keys = process_excel_variable_file(excel_file_path, values_col='values')

        cls.expected_variables = ['ID', 'Name', 'BirthDate', 'EyeColor', 'Gender']
        cls.eye_color_keys = ['Blue', 'Brown', 'Green', 'Hazel']
        cls.gender_keys = ['Male', 'Female']
        cls.expected_values = {
            'EyeColor': {'Blue': '1', 'Brown': '2', 'Green': '3', 'Hazel': '4'},
            'Gender': {'Male': 'M', 'Female': 'F'}
        }

    def test_variable_names(self):
        actual_variables = self.variable_description['variable'].tolist()
        self.assertListEqual(self.expected_variables, actual_variables)

    def _assert_key_list(self, key, expected_list):
        actual_list = list(self.variable_keys[key].keys())
        self.assertListEqual(expected_list, actual_list)

    def test_keys_correct(self):
        self._assert_key_list('EyeColor', self.eye_color_keys)
        self._assert_key_list('Gender', self.gender_keys)

    def _assert_parsed_value(self, category, key, expected_value):
        actual_value = self.variable_keys[category][key]
        self.assertEqual(actual_value, expected_value)

    def test_parsing_correctness(self):
        for category, values in self.expected_values.items():
            for key, value in values.items():
                self._assert_parsed_value(category, key, value)

if __name__ == '__main__':
    unittest.main()