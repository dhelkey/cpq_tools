import unittest
import pandas as pd
import os
from cpq_tools import process_excel_variable_file

class TestDataFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the path to the Excel file
        data_dir = os.path.join(os.getcwd(), 'cpq_tools', 'data')
        excel_path = os.path.join(data_dir, 'birth_key.xlsx')
        
        # Read the Excel file
        cls.excel_data = pd.read_excel(excel_path)
        
        # Process the Excel file to simulate how your actual processing function works
        cls.variable_description, _ = process_excel_variable_file(excel_path)
        
        # Extract expected columns data directly from the read DataFrame
        cls.expected_variables = cls.excel_data['variable'].tolist()
        cls.expected_descriptions = cls.excel_data['description'].tolist()
        cls.expected_types = cls.excel_data['type'].tolist()

    def test_variable_column(self):
        # Verify the 'variable' column
        actual_variables = self.variable_description['variable'].tolist()
        self.assertListEqual(self.expected_variables, actual_variables)

    def test_description_column(self):
        # Verify the 'description' column
        actual_descriptions = self.variable_description['description'].tolist()
        self.assertListEqual(self.expected_descriptions, actual_descriptions)

    def test_type_column(self):
        # Verify the 'type' column
        actual_types = self.variable_description['type'].tolist()
        self.assertListEqual(self.expected_types, actual_types)

if __name__ == '__main__':
    unittest.main()
