#Functions for parsing data files - Intended for CPQCC/CMQCC use

import pandas as pd
import os

def process_excel_variable_file(file_path,
                                 var_col='variable',
                                 desc_col='description', 
                                 type_col='type', 
                                 values_col=None, 
                                 sheet_number=0, 
                                 verbose=False):
    """
    Processes an EXCEL file (.xls or .xlsx) of variable info
    Generates a DataFrame of variable descriptions and a dictionary of variable values.
    NOTE - Uses excel, CSV is overwhelmed by including the key within a column.
    
    Parameters:
    file_path (str): Path to the Excel file.
    var_col (str): Column name for variables.
    desc_col (str): Column name for descriptions.
    type_col (str): Column name for type.
    values_col (str or None): Column name for values, or None if not used.
    sheet_number (int or str): Sheet number or name to use from the Excel file.
    verbose (bool): If True, prints additional information.

    Returns:
    tuple: A DataFrame with variables, descriptions, and types, and a dictionary of variable values.
    
    GPT-4 [20231116]
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")

    # Check if the file is an Excel file
    if not (file_path.endswith('.xls') or file_path.endswith('.xlsx')):
        raise ValueError("The file must be an Excel (.xls or .xlsx) file")

    # Load the specified sheet of the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_number)

    # Check for the existence of required columns
    required_cols = [var_col, desc_col, type_col]
    if values_col:
        required_cols.append(values_col)
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the file")

    rows = []
    variable_key_dict = {}
    delimiters = ['=', '-', ':']

    for _, row in df.iterrows():
        var = row[var_col]
        desc = row[desc_col]
        type_ = row[type_col]

        # Append to the list for later concatenation
        rows.append({var_col: var, desc_col: desc, type_col: type_})

        # Process values if values_col is specified and not empty
        if values_col and pd.notna(row[values_col]) and row[values_col].strip() != "":
            values_str = str(row[values_col])
            values_dict = {}
            
            for kv in values_str.split("\n"):
                split_kv = None
                for delimiter in delimiters:
                    if delimiter in kv:
                        split_kv = kv.split(delimiter, 1)
                        break

                if split_kv and len(split_kv) == 2:
                    key, value = split_kv
                    values_dict[key.strip()] = value.strip()

            # Add to dictionary only if values_dict is not empty
            if values_dict:
                variable_key_dict[var] = values_dict

    variable_description_df = pd.concat([pd.DataFrame([row]) for row in rows], ignore_index=True)

    if verbose:
        print(f"Processed {len(df)} entries")

    return variable_description_df, variable_key_dict
