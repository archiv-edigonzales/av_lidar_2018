#!/bin/bash

BASEPATH=/Samsung_T5/99_Derivate/vegetation/
OUTPATH=/Samsung_T5/99_Derivate/tmp/

gdal_translate $BASEPATH/vegetation.vrt $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif -a_srs EPSG:2056 -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'

gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config PREDICTOR_OVERVIEW 2 -ro -r average $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif 2
gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config PREDICTOR_OVERVIEW 2 -ro -r average $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif.ovr 2
gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config PREDICTOR_OVERVIEW 2 -ro -r average $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif.ovr.ovr 2
gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config PREDICTOR_OVERVIEW 2 -ro -r average $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif.ovr.ovr.ovr 2
gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config PREDICTOR_OVERVIEW 2 -ro -r average $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif.ovr.ovr.ovr.ovr 2
gdaladdo --config COMPRESS_OVERVIEW DEFLATE --config PREDICTOR_OVERVIEW 2 -ro -r average $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif.ovr.ovr.ovr.ovr.ovr 2

gdal_translate $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation_tmp.tif $OUTPATH/ch.so.agi.lidar_2018.ndsm_vegetation.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'

# 0ERROR 6: Only single band dataset supported for non Byte datatype
#gdal_translate --config OGR_SQLITE_SYNCHRONOUS OFF -co APPEND_SUBDATASET=YES -co RASTER_TABLE=ch.so.agi.lidar_2018.dtm -co TILE_FORMAT=TIFF -of GPKG $OUTPATH/ch.so.agi.lidar_2018.dtm.tif $OUTPATH/ch.so.agi.lidar_2018.dtm.gpkg
#gdaladdo --config OGR_SQLITE_SYNCHRONOUS OFF -oo TABLE=ch.so.agi.lidar_2018.dtm -r average $OUTPATH/ch.so.agi.lidar_2018.dtm.gpkg 2 4 8 16 32 64 128 256