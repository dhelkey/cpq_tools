
#Functions for formatting dataframes, constructing summarys ets
#Useful for constructing reports
#Use common API, var
import pandas as pd

def table_one(df, variable_vec, category_var=None, all_dict=None,
                show_na=False,
                only_indicator_1 = False,
                verbose=False,
                cat_vars_ordered = ['ucodr130', 'dcat_i'],
                var_type_identifier = 'type'): #Specify a variable type dataframe, including the keys. Use existing function to creat.
    """Function generated primiarily by GPT"""

    return(df.head(2)) #This should break the tests for right now


    #Want it to have "All" functionality, the ability BUT NOT THE REQUIREMENT to recode values 

    # required_vars = ['categorical_vars_use', 'cont_vars_use', 'indicator_vars_use','mort_vars_use', 'var_dict_list', 'var_name_dict']
    # # if not all(var in globals() for var in required_vars):
    # #     raise ValueError("All required variables must be defined in the global scope: " + ', '.join(required_vars))

    # cont_var_suffix = "mean (SD)"
    # cat_var_suffix = "N (%)"
    # mort_var_suffix = "N (Mortality per 1000 births)"
      
    # def catVarFun(temp_df, var, index_use):
    #     if index_use == 'Unknown':
    #         n = temp_df[temp_df[var].isna()].shape[0]
    #     else:
    #         n = temp_df[temp_df[var] == index_use].shape[0]

    #     if temp_df.shape[0] == 0:
    #         col_pct = 0
    #     else:
    #         col_pct = n / temp_df.shape[0] * 100

    #     return f"{n:,} ({col_pct:.1f})"

    # def contVarFun(temp_df, var):
    #     mean_val = temp_df[var].mean()
    #     sd_val = temp_df[var].std()
    #     return f"{mean_val:.1f} ({sd_val:.1f})"

    # def mortVarFun(temp_df, var, mort_type='CDC'):
    #     if mort_type == 'CDC': #Due to the way death records are identified by the CDC
    #         num_deaths = int(temp_df[temp_df[var] == 1].recwt.sum())
    #     else: #For using with other types of mortality
    #         num_deaths = int(temp_df[temp_df[var] == 1].shape[0])

    #     mort_per_1000 = num_deaths / temp_df.shape[0] * 1000
    #     return f"{num_deaths:,} ({mort_per_1000:.1f})"

    # if category_var is None:
    #     raise ValueError("category_var must be defined.")

    # all_vars = categorical_vars_use + cont_vars_use + indicator_vars_use + mort_vars_use
    # if not set(variable_vec).issubset(set(all_vars)):
    #     offending_vars = list(set(variable_vec) - set(all_vars))
    #     raise ValueError(f"All elements of variable_vec must be in either categorical_vars_use, cont_vars_use, or indicator_vars_use. Offending vars: {offending_vars}")

    # if category_var not in var_dict_list:
    #     raise ValueError(f"{category_var}  must be in var_dict_list.")


    # category_var_vals = df.sort_values(by=category_var)[category_var].unique()
    # variable_vec_vals_dict = {var: df[var].unique().tolist() for var in variable_vec}

    # out_dict = {}

    # iterable_list = [(val, df[df[category_var] == val]) for val in category_var_vals]

    # if all_dict is not None:
    #     iterable_list += [(key, df[df[category_var].isin(all_dict[key])]) for key in all_dict]

    # for name_of_df, df_temp in iterable_list:
    #     #print(name_of_df)
    #     # print(var_dict_list[category_var])
    #     # print(category_var)
    #     # print(var_dict_list[category_var][name_of_df])
    #     # print(all_dict)
    #     if all_dict is None:
    #         col_name = var_dict_list[category_var][name_of_df]
    #     else:
    #         col_name = name_of_df if name_of_df in all_dict else var_dict_list[category_var][name_of_df]
    #     for var in variable_vec:
    #         first_row = True
    #         if var in cont_vars_use:
    #             out_str = contVarFun(df_temp, var)
    #             out_key = f"{var}_mean_sd"

    #             if out_key not in out_dict:
    #                 out_dict[out_key] = {}

    #             out_dict[out_key][col_name] = out_str
    #             out_dict[out_key]['value'] = "mean (SD)"
    #             var_str = f"{var_name_dict[var]}, {cont_var_suffix}"
    #             out_dict[out_key]['var_str'] = var_str if first_row else ''
    #             out_dict[out_key]['var'] = var
    #             first_row = False

    #         elif var in categorical_vars_use or var in indicator_vars_use:

    #             if var in cat_vars_ordered:  # If the variable is in the specified list, order by frequency
    #                 sorted_vals = df[var].value_counts().index.tolist()
    #             else:
    #                 sorted_vals = np.sort(df[var].dropna().unique())

    #             n_na = df[var].isna().sum()
    #             if var in indicator_vars_use:
    #                 sorted_vals = [1, 0]

    #                 if only_indicator_1:
    #                     sorted_vals = [1]

    #             if show_na & (n_na > 0):
    #                 try:
    #                     sorted_vals = sorted_vals.tolist()
    #                 except:
    #                     pass
    #                 sorted_vals.append('Unknown')

    #             for val_index, val in enumerate(sorted_vals):
    #                 if not (pd.isna(val) and not show_na):
    #                     if val != 'Unknown':
    #                         #print(var, val)
    #                         #print(var)
    #                         if var_dict_list[var] is not None:
    #                             key_val = var_dict_list[var][val]
    #                         else:
    #                             key_val = val
    #                     else:
    #                         key_val = 'Unknown'

    #                     out_str = catVarFun(df_temp, var, val)
    #                     out_key = f"{var}_{val_index}_{key_val}"
                        
    #                     if out_key not in out_dict:
    #                         out_dict[out_key] = {}
                            
    #                     out_dict[out_key][col_name] = out_str
    #                     out_dict[out_key]['value'] = key_val
    #                     try:
    #                         var_str = f"{var_name_dict[var]}, {cat_var_suffix}"
    #                     except:
    #                         var_str = f"{var}, {cat_var_suffix}"
    #                     out_dict[out_key]['var_str'] = var_str if first_row else ''
    #                     out_dict[out_key]['var'] = var

    #                     if first_row:
    #                         first_row = False
 
    #                     if  ((val=='Unknown') & ((not show_na) | (df[var].isna().sum()==0))):
    #                         continue

    #         elif var in mort_vars_use:
    #             out_str = mortVarFun(df_temp, var)
    #             out_key = f"{var}_mortality"

    #             if out_key not in out_dict:
    #                 out_dict[out_key] = {}

    #             out_dict[out_key][col_name] = out_str
    #             out_dict[out_key]['value'] = mort_var_suffix
    #             var_str = f"{var_name_dict[var]}, {mort_var_suffix}"
    #             #var_str = var
    #             out_dict[out_key]['var_str'] = var_str if first_row else ''
    #             out_dict[out_key]['var'] = var
                          
    # out_df = pd.DataFrame(out_dict).T.reset_index().rename(columns={'index': 'var_value'})
    # return out_df