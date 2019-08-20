#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

TINDEX = "/vagrant/lidar2018.shp"
INPATH = "/lidar2018/05_DTM_ASCII_25cm/"
OUTPATH = "/Samsung_T5/99_Derivate/dtm/"
TMPPATH = "/Samsung_T5/99_Derivate/tmp/dtm/"

shp = ogr.Open(TINDEX)
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    print "**********************: " + infileName

    basename = os.path.splitext(infileName)[0]
    infile = os.path.join(INPATH, infileName)
    outfile = os.path.join(TMPPATH, basename + ".tif")
    cmd = "gdal_translate -a_srs epsg:2056  -of GTiff -co 'TILED=YES' "
    cmd += infile + " " + outfile
    print cmd
    os.system(cmd)
    print "**********************: "

    infile = outfile
    outfile = os.path.join(OUTPATH, basename + ".tif")
    cmd = "gdal_translate -a_srs epsg:2056  -of GTiff -co 'TILED=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' "
    cmd += "-ot Float32 " + infile + " " + outfile
    print cmd
    os.system(cmd)
    print "**********************: "

    infile = outfile
    cmd = "gdaladdo -r average " + infile + " 2 4 8 16 32"
    print cmd
    os.system(cmd)

    cmd = "rm " + os.path.join(TMPPATH, "*.tif")
    print cmd
    os.system(cmd)
    print "**********************: "

