import unittest
import pandas as pd

from cpq_tools.missingness_grid import missingness_grid
from cpq_tools.data import SAMPLE_INFANT_DATA, SAMPLE_INFANT_DATA_NA, SAMPLE_VARIABLE_KEY_DICT

class TestMissingnessGrid(unittest.TestCase):

    def setUp(self):
        """Set up for calculating expected missingness percentages."""
        # Initialize dictionaries to hold the expected missingness for each dataset
        self.expected_missingness = {}
        self.datasets = {
            'data': SAMPLE_INFANT_DATA,
            'data_na': SAMPLE_INFANT_DATA_NA
        }
        

    def calculate_missingness(self, dataset, dataset_name):
        """Calculate the expected total missingness and by 'Sex' for a given dataset."""
        self.expected_missingness[dataset_name] = {
            'total': dataset.isnull().mean() * 100,
            'by_sex': {
                'Male': dataset[dataset['Sex'] == 1.0].isnull().mean() * 100,
                'Female': dataset[dataset['Sex'] == 0.0].isnull().mean() * 100
            }
        }

    def test_missingness_by_dataset(self):
        """Test missingness calculations for each dataset."""
        for dataset_name, dataset in self.datasets.items(): 
            #[('data', SAMPLE_INFANT_DATA), ('data_na', SAMPLE_INFANT_DATA_NA)]:
            self.calculate_missingness(dataset, dataset_name)
            with self.subTest(dataset=dataset_name):
                result_total = missingness_grid(dataset)
                result_by_sex = missingness_grid(dataset, col_var_list=['Sex'], var_key_dict=SAMPLE_VARIABLE_KEY_DICT)
                # Check 'Total' column
                for col in dataset.columns:
                    expected_total = round(self.expected_missingness[dataset_name]['total'][col], 1)
                    self.assertEqual(result_total.at[col, 'Total'], expected_total)
                # Check 'by_sex' columns if applicable
                if dataset_name == 'data_na':
                    for col in dataset.columns:
                        expected_male = round(self.expected_missingness[dataset_name]['by_sex']['Male'][col], 1)
                        expected_female = round(self.expected_missingness[dataset_name]['by_sex']['Female'][col], 1)
                        self.assertEqual(result_by_sex.at[col, 'Male'], expected_male)
                        self.assertEqual(result_by_sex.at[col, 'Female'], expected_female)
    
    def test_total_column(self):
            """Test if 'Total' column exists and has correct missingness percentages."""
            for dataset_name, dataset in self.datasets.items():
                with self.subTest(dataset=dataset_name):
                    self.calculate_missingness(dataset, dataset_name)
                    result = missingness_grid(dataset)
                    self.assertIn('Total', result.columns)
                    for col in dataset.columns:
                        expected_total = round(self.expected_missingness[dataset_name]['total'][col], 1)
                        self.assertAlmostEqual(result.at[col, 'Total'], expected_total)

    def test_category_columns(self):
        """Test if categorical columns are created and have correct missingness percentages."""
        for dataset_name, dataset in self.datasets.items():
            with self.subTest(dataset=dataset_name):
                result = missingness_grid(dataset, col_var_list=['Sex'])
                self.assertIn('Sex=1', result.columns)
                self.assertIn('Sex=0', result.columns)
                self.calculate_missingness(dataset, dataset_name)
                for col in dataset.columns:
                    expected_male = round(self.expected_missingness[dataset_name]['by_sex']['Male'][col], 1)
                    expected_female = round(self.expected_missingness[dataset_name]['by_sex']['Female'][col], 1)
                    self.assertAlmostEqual(result.at[col, 'Sex=1'], expected_male)
                    self.assertAlmostEqual(result.at[col, 'Sex=0'], expected_female)

    def test_annotation(self):
        """Test if columns are correctly annotated using var_key_dict."""
        for dataset_name, dataset in self.datasets.items():
            with self.subTest(dataset=dataset_name):
                result = missingness_grid(dataset, col_var_list=['Sex'], var_key_dict=SAMPLE_VARIABLE_KEY_DICT)
                self.assertIn('Male', result.columns)
                self.assertIn('Female', result.columns)
                self.calculate_missingness(dataset, dataset_name)
                for col in dataset.columns:
                    expected_male = round(self.expected_missingness[dataset_name]['by_sex']['Male'][col], 1)
                    expected_female = round(self.expected_missingness[dataset_name]['by_sex']['Female'][col], 1)
                    self.assertAlmostEqual(result.at[col, 'Male'], expected_male)
                    self.assertAlmostEqual(result.at[col, 'Female'], expected_female)

    def test_decimals(self):
        """Test if the number of decimals is correctly applied."""
        for dataset_name, dataset in self.datasets.items():
            for decimals in [0, 1, 2, 3]:
                with self.subTest(dataset=dataset_name, decimals=decimals):
                    result = missingness_grid(dataset, decimals=decimals)
                    self.calculate_missingness(dataset, dataset_name)
                    for col in dataset.columns:
                        expected_value = round(self.expected_missingness[dataset_name]['total'][col], decimals)
                        self.assertAlmostEqual(result.at[col, 'Total'], expected_value, places=decimals)

# This is the standard boilerplate to run the test suite
if __name__ == '__main__':
    unittest.main()
