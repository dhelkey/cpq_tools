import pandas as pd

def missingness_grid(df, var_list=None, col_var_list=None, annotation_dict=None,
                      var_key_dict=None, col_var_max_categories=5, decimals=1):
    """
    Possibly deprecate this function
    Create a grid displaying the percentage of missing values for variable combinations.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
        var_list (list, optional): List of row variables. If None, includes all columns.
        col_var_list (list, optional): List of column variables. These should be categorical.
        annotation_dict (dict, optional): Dictionary to annotate row variable names.
        var_key_dict (dict, optional): Dictionary to annotate column variable names.
        col_var_max_categories (int): Maximum number of categories to include for column variables.
        decimals (int): Number of decimal places to round the missingness percentages.

    Returns:
        pd.DataFrame: A DataFrame showing the percentage of missing values for each variable combination.

    GPT-4 "Code Wizard" - 20240111
    """
    if var_list is None:
        var_list = df.columns

    # Initialize grid_data with a 'Total' column for overall missingness
    grid_data = pd.DataFrame(df[var_list].isnull().mean().multiply(100).round(decimals), columns=['Total'])

    if col_var_list:
        for col_var in col_var_list:
            top_categories = df[col_var].value_counts().index[:col_var_max_categories]
            for category in top_categories:
                category_str = str(int(category)) if \
                    isinstance(category, float) and category.is_integer() else str(category)
                col_name = f"{col_var}={category_str}"
                if var_key_dict and col_var in var_key_dict:
                    col_name = var_key_dict[col_var].get(category, col_name)
                grid_data[col_name] = df[df[col_var] == category][var_list].isnull().mean().multiply(100).round(decimals)

    if annotation_dict:
        grid_data.index = [annotation_dict.get(idx, idx) for idx in grid_data.index]

    return grid_data

# Example usage:
# Assuming SAMPLE_INFANT_DATA is your DataFrame.
#missingness_grid(SAMPLE_INFANT_DATA_NA, 
#                          var_list=None, 
#                          col_var_list=['Sex', 'RacialCategory'], decimals=1)
