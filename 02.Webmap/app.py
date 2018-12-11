import folium
import pandas
import json

df = pandas.read_csv('./cordinates.txt')


def colors(elev):
    minimum = int(min(df['ELEV']))
    step = int(max((df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum, minimum+step):
        col = "green"
    elif elev in range(minimum+step, minimum+step*2):
        col = "orange"
    else:
        col = "red"
    return col


map_1 = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()],
                   zoom_start=6, tiles='mapbox bright')

for name, lon, lat, elev in zip(df['NAME'], df['LON'], df['LAT'],
                                df['ELEV']):
    folium.Marker([lat, lon], popup=name,
                  icon=folium.Icon(color=colors(elev))).add_to(map_1)

folium.GeoJson(open('./world.json'),
               name='geojson',
               style_function=lambda x: {'fillColor': 'green' if
                                         x['properties']['POP2005'] < 10000000
                                         else 'orange' if 10000000 < x['properties']['POP2005'] > 20000000 else 'red'}
               ).add_to(map_1)
folium.LayerControl().add_to(map_1)
