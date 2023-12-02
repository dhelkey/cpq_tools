# #Test the table one function

import unittest
import pandas as pd
from cpq_tools.report_functions import tableOne

print(15)

class TestTableOneFunction(unittest.TestCase):

    def test_tableOne(self):
        # Sample DataFrame setup
        data = {
            'category_var': ['A', 'B', 'C', 'A', 'B', 'C'],
            'simple_cat': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
            'renamed_cat': ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],
            'no_rename_cat': ['cat1', 'cat2', 'cat1', 'cat2', 'cat1', 'cat2'],
            'continuous_var': [1.2, 3.4, 5.6, 2.3, 4.5, 6.7],
            'indicator_var': [1, 0, 1, 0, 1, 0],
            'mortality_var': [1, 1, 0, 0, 1, 0]
        }

        df = pd.DataFrame(data)

        # Variable type dictionary
        var_type_dict = {
            'simple_cat': 'categorical',
            'renamed_cat': 'categorical',
            'no_rename_cat': 'categorical',
            'continuous_var': 'continuous',
            'indicator_var': 'indicator',
            'mortality_var': 'mortality'
        }

        # Variable key dictionary for renaming
        variable_key_dict = {
            'alpha': 'Group Alpha',
            'beta': 'Group Beta',
            'gamma': 'Group Gamma'
        }

        # List of variables to analyze
        var_vec = ['simple_cat', 'renamed_cat', 'no_rename_cat', 
                   'continuous_var', 'indicator_var', 'mortality_var']

        # Function call
        result_df = tableOne(
            df, var_vec, 'category_var', all_dict=None, show_na=True, 
            only_indicator_1=True, verbose=False, cat_vars_ordered=None,
            var_type_dict=var_type_dict, variable_key_dict=variable_key_dict
        )

        # Here you would add assertions to validate the result of tableOne function
        # For example, if you expect the result to have the same number of rows as `df`:
        self.assertEqual(len(result_df), len(df),
                         "The result DataFrame should have the same number of rows as the input DataFrame.")

        self.assertEqual(1,2, '2+2=5')
        # You can add more assertions here based on the expected outcome of the `tableOne` function.

if __name__ == '__main__':
    unittest.main()