import unittest
import pandas as pd
from cpq_tools import crosstab_three_way  # Ensure this is the correct import for your crosstab function
from cpq_tools.data  import SAMPLE_INFANT_DATA
from cpq_tools.data import SAMPLE_VARIABLE_KEY_DICT

# Constants for DataFrame column names
INDEX1_VAR = 'RacialCategory'
INDEX2_VAR = 'HispanicLatino'
COLUMNS_VAR = 'Sex'
# LABEL_DICT = {
#     INDEX1_VAR: {1: 'American Indian/Alaska Native', 2: 'Asian', 3: 'Black or African American'},
#     INDEX2_VAR: {0: 'Not Hispanic or Latino', 1: 'Hispanic or Latino'},
#     COLUMNS_VAR: {0: 'Female', 1: 'Male'}
LABEL_DICT = SAMPLE_VARIABLE_KEY_DICT
# }

class TestCrosstabThreeWay(unittest.TestCase):
    # Assuming SAMPLE_INFANT_DATA is already defined in the test environment

    def test_crosstab_creation_with_censoring(self):
        # Test the crosstab creation with censoring
        crosstab = crosstab_three_way(SAMPLE_INFANT_DATA, 
                                      index1_var=INDEX1_VAR, 
                                      index2_var=INDEX2_VAR, 
                                      columns_var=COLUMNS_VAR, 
                                      label_dict=LABEL_DICT, 
                                      sub_totals=True, 
                                      n_censor=15)
        # Check if all values that should be censored are correctly censored
        for col in crosstab.columns:
            for idx in crosstab.index:
                value = crosstab.at[idx, col]
                if isinstance(value, int) and value < 15:
                    self.assertEqual(crosstab.at[idx, col], '<15')

    def test_crosstab_creation_without_censoring(self):
        # Test the crosstab creation without censoring
        crosstab = crosstab_three_way(SAMPLE_INFANT_DATA, 
                                      index1_var=INDEX1_VAR, 
                                      index2_var=INDEX2_VAR, 
                                      columns_var=COLUMNS_VAR, 
                                      label_dict=LABEL_DICT, 
                                      sub_totals=True)
        # Check if values are numeric or 'Total'
        for col in crosstab.columns:
            for idx in crosstab.index:
                self.assertTrue(isinstance(crosstab.at[idx, col], int) or crosstab.at[idx, col] == 'Total')

    def test_crosstab_no_subtotals_with_censoring(self):
        # Test the crosstab creation without subtotals but with censoring
        crosstab = crosstab_three_way(SAMPLE_INFANT_DATA, 
                                      index1_var=INDEX1_VAR, 
                                      index2_var=INDEX2_VAR, 
                                      columns_var=COLUMNS_VAR, 
                                      label_dict=LABEL_DICT, 
                                      sub_totals=False, 
                                      n_censor=15)
        # Ensure that numeric values are strings and check if they are censored
        censored_values = crosstab.applymap(lambda x: x.startswith('<') if isinstance(x, str) else True)
        self.assertTrue(censored_values.all().all())

    def test_n_censor_not_integer(self):
        # Test for n_censor not being an integer
        with self.assertRaises(ValueError):
            crosstab_three_way(SAMPLE_INFANT_DATA, 
                               index1_var=INDEX1_VAR, 
                               index2_var=INDEX2_VAR, 
                               columns_var=COLUMNS_VAR, 
                               label_dict=LABEL_DICT, 
                               n_censor='12')

# This allows the test suite to be run from the command line
if __name__ == '__main__':
    unittest.main()
import unittest
import pandas as pd
from cpq_tools import crosstab_three_way  # Ensure this is the correct import for your crosstab function

# Constants for DataFrame column names
INDEX1_VAR = 'RacialCategory'
INDEX2_VAR = 'HispanicLatino'
COLUMNS_VAR = 'Sex'
LABEL_DICT = {
    INDEX1_VAR: {1: 'American Indian/Alaska Native', 2: 'Asian', 3: 'Black or African American'},
    INDEX2_VAR: {0: 'Not Hispanic or Latino', 1: 'Hispanic or Latino'},
    COLUMNS_VAR: {0: 'Female', 1: 'Male'}
}

class TestCrosstabThreeWay(unittest.TestCase):
    # Assuming SAMPLE_INFANT_DATA is already defined in the test environment

    def test_crosstab_creation_with_censoring(self):
        # Test the crosstab creation with censoring
        crosstab = crosstab_three_way(SAMPLE_INFANT_DATA, 
                                      index1_var=INDEX1_VAR, 
                                      index2_var=INDEX2_VAR, 
                                      columns_var=COLUMNS_VAR, 
                                      label_dict=LABEL_DICT, 
                                      sub_totals=True, 
                                      n_censor=15)
        # Check if all values that should be censored are correctly censored
        for col in crosstab.columns:
            for idx in crosstab.index:
                value = crosstab.at[idx, col]
                if isinstance(value, int) and value < 15:
                    self.assertEqual(crosstab.at[idx, col], '<15')

    def test_crosstab_creation_without_censoring(self):
        # Test the crosstab creation without censoring
        crosstab = crosstab_three_way(SAMPLE_INFANT_DATA, 
                                      index1_var=INDEX1_VAR, 
                                      index2_var=INDEX2_VAR, 
                                      columns_var=COLUMNS_VAR, 
                                      label_dict=LABEL_DICT, 
                                      sub_totals=True)
        # Check if values are numeric or 'Total'
        for col in crosstab.columns:
            for idx in crosstab.index:
                self.assertTrue(isinstance(crosstab.at[idx, col], int) or crosstab.at[idx, col] == 'Total')

    def test_crosstab_no_subtotals_with_censoring(self):
        # Test the crosstab creation without subtotals but with censoring
        crosstab = crosstab_three_way(SAMPLE_INFANT_DATA, 
                                      index1_var=INDEX1_VAR, 
                                      index2_var=INDEX2_VAR, 
                                      columns_var=COLUMNS_VAR, 
                                      label_dict=LABEL_DICT, 
                                      sub_totals=False, 
                                      n_censor=15)
        # Ensure that numeric values are strings and check if they are censored
        censored_values = crosstab.applymap(lambda x: x.startswith('<') if isinstance(x, str) else True)
        self.assertTrue(censored_values.all().all())

    def test_n_censor_not_integer(self):
        # Test for n_censor not being an integer
        with self.assertRaises(ValueError):
            crosstab_three_way(SAMPLE_INFANT_DATA, 
                               index1_var=INDEX1_VAR, 
                               index2_var=INDEX2_VAR, 
                               columns_var=COLUMNS_VAR, 
                               label_dict=LABEL_DICT, 
                               n_censor='12')

# This allows the test suite to be run from the command line
if __name__ == '__main__':
    unittest.main()
