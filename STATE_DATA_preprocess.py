#Preprocessing code, primarily charge data code preprocessing, generating geographic data and
#constructing hospital data 


#Import Charge dataframes -> convert to dictionary 


#Reverse search - 
from uszipcode import SearchEngine
search = SearchEngine()
# from uszipcode import Zipcode
import numpy as np

#Import hospital list, reverse search to identify zipcode.
#define zipcode search function
def get_zipcode(lat, long):
    result = search.by_coordinates(lat = lat, lng = long, returns = 1)
    print(result)
    return result[0].zipcode

#Test this function
get_zipcode(39.619197, -112.814088)

#define latitude/longitude for function
# df = pd.DataFrame({‘lat’:lat, ‘lon’:lon})

#add new column with generated zip-code
# df[‘zipcode’] = df.apply(lambda x: get_zipcode(x.lat,x.lon), axis=1)