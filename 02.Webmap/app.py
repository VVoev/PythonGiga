import folium
import pandas


def color_provider(elev):
    color = ''
    if elev <= 1000:
        color = 'green'
    elif 1000 < elev and elev < 3000:
        color = 'orange'
    else:
        color = 'red'
    return color


data = pandas.read_csv('./cordinates.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location=[38.59, -99.09],
                 zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(
        location=[lt, ln], popup=str(el)+' m', radius=6, fill_color=color_provider(el), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig')))

map.add_child(fg)
map.save('Map.html')
