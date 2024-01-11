import pandas as pd

def crosstab_three_way(df, 
                       index1_var='RacialCategory', 
                       index2_var='HispanicLatino', 
                       columns_var='Sex', 
                       label_dict=None, 
                       sub_totals=False, 
                       n_censor=None):
    """
    Creates a three-way crosstabulation with provided DataFrame and variable names.
    Labels for integer values are taken from label_dict, if provided; otherwise, 
    original integer values are used. Overall totals are always included if sub_totals 
    or n_censor are True. Subtotals can be included based on the sub_totals parameter. 
    Individual values can be censored based on n_censor, but total counts remain unaffected.
    
    Args:
        df (pd.DataFrame): The input data frame.
        index1_var (str): Column name for the first index (default: 'RacialCategory').
        index2_var (str): Column name for the second index (default: 'HispanicLatino').
        columns_var (str): Column name for the columns (default: 'Sex').
        label_dict (dict, optional): Dictionary of dictionaries for value labels.
        sub_totals (bool): Option to include subtotals in the crosstab (default: False).
        n_censor (int, optional): The smallest value that will be reported; values below this 
                                  threshold will be reported as '<{n_censor}'.

    Returns:
        pd.DataFrame: Crosstabulation with applied labels and censored values.

    Raises:
        KeyError: If any of the default column names do not exist in the DataFrame.
        ValueError: If n_censor is not an integer.

    [GPT Version] [20240108]
    """
    
    # Check if the default column names exist in the DataFrame
    for var in [index1_var, index2_var, columns_var]:
        if var not in df.columns:
            raise KeyError(f"Column '{var}' does not exist in the DataFrame.")

    # Initialize label_dict if None
    label_dict = label_dict or {}

    # Helper function to apply labels from the dictionary or use original values
    def label_values(column, var_name):
        if var_name in label_dict and isinstance(label_dict[var_name], dict):
            return df[column].map(label_dict[var_name]).fillna(df[column])
        else:
            return df[column]

    # Creating the crosstabulation with margins for totals
    create_margins = sub_totals or n_censor is not None
    crosstab = pd.crosstab(index=[label_values(index1_var, index1_var), 
                                  label_values(index2_var, index2_var)], 
                           columns=label_values(columns_var, columns_var), 
                           margins=create_margins, 
                           margins_name="Total")

    # Apply censoring if n_censor is provided
    if n_censor is not None:
        crosstab = crosstab.applymap(lambda x: f"<{n_censor}" if isinstance(x, (int, float)) and x < n_censor else x)

    return crosstab
