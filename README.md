# av_lidar_2018

```
gdaltindex lidar2018.shp /lidar2018/05_DTM_ASCII_25cm/*.asc
```

Und nach `/lidar2018/99_Derivate/` kopieren.

## DTM Processing
ascii to geotiff und Overviews mittels `./scripts/asc2tif_dtm.py`.

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm/
gdalbuildvrt -addalpha dtm.vrt *.tif
```

Einzelnes BigTIFF erstellen:
```
./scripts/bigtiff_dtm.sh
```

## DOM Processing
ascii to geotiff und Overviews mittels `./scripts/asc2tif_dom.py`.

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dom/
gdalbuildvrt -addalpha dom.vrt *.tif
```

Einzelnes BigTIFF erstellen:
```
./scripts/bigtiff_dom.sh
```

## DTM Hillshading
Hillshading der einzelnen Kacheln rechnen:
```
./scripts/hillshade_dtm.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm_hillshade/
gdalbuildvrt -addalpha dtm_hillshade.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_dtm_hillshade.sh
```

## DTM Slope
Einzelne Kacheln rechnen:
```
./scripts/slope_dtm.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm_slope/
gdalbuildvrt -addalpha dtm_slope.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_dtm_slope.sh
```

## DOM Hillshading
Hillshading der einzelnen Kacheln rechnen:
```
./scripts/hillshade_dom.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dom_hillshade/
gdalbuildvrt -addalpha dom_hillshade.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_dom_hillshade.sh
```


## Rasterizing Vegetation
```
./scripts/rasterize_vegetation.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/vegetation/
gdalbuildvrt -addalpha vegetation.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_vegetation.sh
```

## Rasterizing Buildings
```
./scripts/rasterize_buildings.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/buildings/
gdalbuildvrt -addalpha buildings.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_buildings.sh
```