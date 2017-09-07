import folium
import pandas as pd

df = pd.read_csv("/Users/star/Desktop/GitHub_Code_To_Show_off/volcanoes/Volcanoes-USA.txt")
test1 = folium.Map(location=[40.446,-101.689],zoom_start=4,tiles ='Stamen Terrain') 

def mrk_color(elev):
	if elev in range (0,1000):
		color= "green"
	elif elev in range (1000,3000):
		color= "orange"
	else:
		color = "red"
	return color


for lat ,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'],df['ELEV']):  #when iterating through two or more list, use zip
	test1.simple_marker(location=[lat,lon],popup=name +"." + "elevation: %s" %(str(elev)),marker_color= mrk_color(elev)) #function to

test1.create_map(path='Volcanoes_USA.html') #create local HTML file.
