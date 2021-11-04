import folium
from folium import plugins
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv('mapcode/zillowdata.csv')
df.head()

map = folium.Map([35.72,-119.91], tiles="OpenStreetMap", zoom_start=1, control_scale= True)
for index, row in df.iterrows():
    folium.Marker([row["latitude"], row["longitude"]],
    popup=row["address"],
    icon=folium.Icon(icon='home')
    ).add_to(map)

sw = df[['latitude', 'longitude']].min().values.tolist()
ne = df[['latitude', 'longitude']].max().values.tolist()
map.fit_bounds([sw, ne])

map
map.save(r"C:\xampp\htdocs\Project3\foliumhtml.html")