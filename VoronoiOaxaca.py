#Enlace para visualizar en colab
#https://colab.research.google.com/drive/1JnlblRIGIj9kjE4etyvP7sqMVmShnb0v?usp=sharing

""" 
!pip install geopandas==0.12
!pip3 install contextily
!pip install -U geovoronoi[plotting]
"""
import numpy as np
import geopandas as gpd
import pandas as pd
from pandas import DataFrame
import contextily as ctx
import matplotlib.pyplot as plt
from shapely.ops import cascaded_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords

df = pd.read_excel('/content/drive/My Drive/clinicasSanLorenzo.xlsx', index_col=0)
estaciones = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.long,df.lat)) ### Geodataframe
estaciones.head()

#Sistema de coordenadas de referencia(CRS)
#WGS94 Latitude/Longitude: "EPSG:4326"
estaciones.crs = "EPSG:4326"

#municipiosOax contiene los polígonos que corresponden a cada municipio
municipios = gpd.read_file('/content/drive/My Drive/municipiosOax.zip')
# municipios

#Seleccionar el municipio según su número 'CVE_MUN'
#La columna es de strings
oax_jua=municipios[municipios['CVE_MUN'] == '227']
#oax_jua.head()
#municipios.head()

municipio = municipio.to_crs(epsg=3359)
gdf_proj = estaciones.to_crs(municipio.crs)
municipio_shape = cascaded_union(municipio.geometry)
coords = points_to_coords(gdf_proj.geometry)

#Se genera el diagrama de Voronoi sobre el polígono
poly_shapes, pts = voronoi_regions_from_coords(coords, municipio_shape)

#Graficar el diagrama de Voronoi
fig, ax = subplot_for_map(figsize=(14.5,10))
plot_voronoi_polys_with_points_in_area(ax,municipio_shape,poly_shapes,coords,pts)
ax.set_title('Clínicas en San Lorenzo Cacaotepec')
plt.tight_layout()
plt.show()