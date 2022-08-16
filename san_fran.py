#plotting attraction on San Francisco Map 

from math import perm
import os 
import folium
import pandas as pd
import json
from folium import plugins

#path to data file & csv with all attractions in San Francisco
path = os.chdir('/Users/noahchu/Desktop/sf')
df = pd.read_csv('sf_attractions.csv')


with open('/Users/noahchu/Desktop/sf/SanFrancisco.Neighborhoods.json') as f:
    sfArea = json.load(f)

#tiles = 'cartodbpositron' for plain map
#initialize the map around San Francisco
sfMap = folium.Map(location=[37.7749,-122.4194], tiles='OpenStreetMap', zoom_start=9)
folium.GeoJson(sfArea).add_to(sfMap)

#save the map as an html    
sfMap.save('sfPointMap.html')

#allows the user to disable the blue zones on the map  
folium.LayerControl().add_to(sfMap)
#makes the map take up the entire screen
plugins.Fullscreen(position='topright', force_separate_button=True).add_to(sfMap)
#allows user to locate themselves on the map
plugins.LocateControl(position='topright').add_to(sfMap)
#adds small map to left that can be used to move the larger map
plugins.MiniMap(position='bottomleft', zoom_level=10).add_to(sfMap)

#run everytime a new location is added to the csv file
df = pd.read_csv('sf_attractions.csv')

for i,row in df.iterrows():
    folium.CircleMarker((row.latitude,row.longitude),popup = row.location, radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(sfMap)

sfMap.save('sfPointMap.html')

#how to find the coordinates and address of a place
from geopy.geocoders import Nominatim 
geolocator = Nominatim(user_agent='myapplication')
location = geolocator.geocode("Red Umbrella Cafe")
print((location.latitude, location.longitude,location.address))























#Look at later
#spots = ['Patagonia','Grateful Dead House','Coit Tower','Golden Gate Bridge','Golden Gate Park',
# 'Chinatown','San Francisco Airport','Yank Sing','HK Clay Pot','Din Tai Fung','Alcatraz Island',
# 'Twin Peaks','Baker Beach','Ferry Building','Union Square','Mission District', 'Ocean Beach',
# 'Lombard Street','Painted Ladies','Dolores Park','Palace of Fine Arts','Sunset Squares']

#from geopy.geocoders import Nominatim 
#geolocator = Nominatim(user_agent='myapplication')
#location = geolocator.geocode("8021 Gleason Dr, Knoxville, TN 37919")
#for loop that runs through spots and geocodes them
#for spot in spots:
    #location = geolocator.geocode(spot)
    #print(location.address)
    #print(location.latitude, location.longitude)
    #folium.CircleMarker((location.latitude,location.longitude),popup=spot, radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(sfMap)
#print((location.latitude, location.longitude,location.address))

#save print((location.latitude, location.longitude, location.address)) into sf_attractions.csv


#df = pd.DataFrame.to_csv(columns=['latitude','longitude','address'])
#df.loc[0] = [location.latitude, location.longitude, location.address]
#df.to_csv('sf_attractions.csv', index=False)
#print(df)



