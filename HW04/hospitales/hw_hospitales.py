import pandas as pd

df = pd.read_csv('./hospitales2.csv')

latitude = list()
longitude = list()

for index, row in df.iterrows():

    _latitude, _longitude = row['WKT'].replace("POINT ", "").replace("(", "").replace(")", "").split(" ")
    latitude.append(float(_latitude))
    longitude.append(float(_longitude))

# Creando nuevas columnas
df['latitude'] = latitude
df['longitude'] = longitude
# Renombrando columnas
df.rename(columns={"DOM_NORMA": "name", "NOMBRE": "label"}, inplace=True)
# Reordenar las columnas
df = df[['latitude', 'longitude', 'name', 'label']]

print(df.head())