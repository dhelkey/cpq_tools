var_key_docstring = """
setup variables:

Parameters defined in PRIVATE file:
    phi_data_path - Location of PHI data - All intermediate data is saved here.
    state_infant_long_files  - Dictionary of STATE_DATA files
                        Two files per state:
                            INFANT - Infant birth records - One row per infant
                            LONG - Infant discharge records - One row per infant/stay
    file_var_documentation - Path to documentation file (excel)
    file_included_vars - Path to included variable table (excel)

Constructed by STATE_DATA_setup.py:

     - Panas dataframe of variable information (Parsed STATE_DATA_DOCUMENTATION_FILE)

    missing_unknown_var_dict - Variable values corrosponding to missing/unknown

#IMPORT CODE
"""


#Variables with missing values encoded (We use all lowercase variable names)
missing_unknown_var_dict = {'bcmod_route':[9],
                           'educatm':[0],
                           'educatv_m2':[0],
                           'kotelchuck':[9],
                           'racem':[0],
                           'racem_exp':[9],
                           'bc_attendant':[9],
                           'insurance_mom':[0]}
    #Identifying Missing Values
    #Constructs [variable]_m for variables with missing value codes
    #Replaces variable specific missing value codes (0,9,...)
    # with np.nan "."
    # This can simplify analysis in certain situations
    # E.g. Missing value reports, consistant regression handling
    # NOTE -  Caution needed when using for regression.
    #  1. Statistical functions may drop NA values
    # 2. Default comparison category may change for categorical variables


#TODO Here is the main todo
#Add recoded missing values to each of the type, description, and values dictionaries


#Add variables names with 'np.nan' missing value coding to
#   VARIABLE_KEY_DICT, VARIABLE_DESC_DICT

#Parse list of variables included for analysis
#Read in list of included variables #(Name, description, constructed, type (just for constructed))
#Add in unincluded variables to the dictinaries (type, descrition, (no categorical variables constructed?))

#Create a processe 



#TODO - Verify we have descriptions and types for all variables, and keys for all categorical variables


    
#Extract and parse full list of variables from STATE_DATA_documentation.xlsx
#All variables, including extranious variables, currently unused in analysis
#WE are interested in 3 dictionaries (key = variable name)
#         - type (categorical, continious,...)
#         - description
#         - values (dictionary key)

##TODO rename these
# #
# VARIABLE_INFO_DF, VARIABLE_KEY_DICT, \
#       VARIABLE_DESC_DICT = 

parsed_documentation = process_excel_variable_file(
    file_var_documentation,
    var_col="Variable", 
    desc_col="Description/Label", 
    type_col="Type",
    values_col='Values'
) 

#Extracting parsed documentation (All documentation stored in these 
#parsed dictionaries)
var_key_dict =  parsed_documentation['var_key_dict']
var_desc_dict = parsed_documentation['desc_dict']
var_type_dict = parsed_documentation['type_dict']

state_data_vars_dat = pd.read_excel(file_vars_use)

#Read STATE_DATA_vars_use.xlsx 
#Overwrite any variable descriptions 
#Frome this, ADD the variable names (constructed=1) to var_disc_dict
#Right now, we are focusing on var_desc_dict
#ADD any variables with

