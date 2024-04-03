import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="OpenStreetMap")
fg = folium.FeatureGroup(name="Moja mapa")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " meters", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map3C.html")
