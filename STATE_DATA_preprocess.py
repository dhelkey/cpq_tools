#Preprocessing code, primarily generating geographic data and
#data for hospitals


#Import 


#Reverse search - 
from uszipcode import SearchEngine
search = SearchEngine()
# from uszipcode import Zipcode
import numpy as np

#define zipcode search function
def get_zipcode(lat, long):
    result = search.by_coordinates(lat = lat, lng = long, returns = 1)
    print(result)
    return result[0].zipcode


#Test this function
# get_zipcode(39.519042, -119.814866)
# get_zipcode(39.519586, -119.813490)
get_zipcode(39.619197, -112.814088)

# # #load columns from dataframe
# lat = df['Latitude']
# lon = df['Longitude']

#define latitude/longitude for function
# df = pd.DataFrame({‘lat’:lat, ‘lon’:lon})

#add new column with generated zip-code
# df[‘zipcode’] = df.apply(lambda x: get_zipcode(x.lat,x.lon), axis=1)