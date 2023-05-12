r'''A partir del csv hospitales2.csv, generar un archivo CSV de salida, 
que contenga los siguientes campos en este orden:
* latitude
* longitude
* name
* label
Con los correspondientes datos extraídos del CSV original, el campo name
tiene que corresponder con la dirección del hospital, y el campo label con
el nombre del hospital.

Ejemplo de visualización en: https://www.gpsvisualizer.com
'''
import pandas as pd

# Loading .csv file into DataFrame
df = pd.read_csv('./hospitales2.csv')
# New Columns initialization
latitude = list()
longitude = list()
# Loop for transform column where are coordinates
for index, row in df.iterrows():

    _longitude, _latitude = row['WKT'].replace("POINT (", "").replace(")", "").split(" ")
    latitude.append(float(_latitude))
    longitude.append(float(_longitude))

# Inserting Latitude and Longitud column
df['latitude'] = latitude
df['longitude'] = longitude
# Renaming Columns
df.rename(columns={"DOM_NORMA": "name", "NOMBRE": "label"}, inplace=True)
# Reordering Columns
df = df[['latitude', 'longitude', 'name', 'label']]

df.to_csv("./hospitales_cleaned.csv")