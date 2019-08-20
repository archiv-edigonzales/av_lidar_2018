#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

VRT = "/Samsung_T5/99_Derivate/dtm/dtm.vrt"
TINDEX = "/vagrant/lidar2018.shp"
INPATH = "/Samsung_T5/99_Derivate/dtm/"
OUTPATH = "/Samsung_T5/99_Derivate/dtm_slope/"
TMPPATH = "/tmp/slope/dtm/"
BUFFER = 10

shp = ogr.Open("/vagrant/lidar2018.shp")
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    basename = os.path.splitext(infileName)[0]
    print "**********************: " + infileName

    geom = feature.GetGeometryRef()
    env = geom.GetEnvelope()

    minX = int(env[0] + 0.001)
    minY = int(env[2] + 0.001)
    maxX = int(env[1] + 0.001)
    maxY = int(env[3] + 0.001)
    
    print minX 
    print minY

    cmd = "mkdir -p " + TMPPATH
    print cmd
    os.system(cmd)

    outfile = os.path.join(TMPPATH, basename + ".tif")
    cmd = "gdalwarp -s_srs epsg:2056 -t_srs epsg:2056 -te "  + str(minX - BUFFER) + " " +  str(minY - BUFFER) + " " +  str(maxX + BUFFER) + " " +  str(maxY + BUFFER)
    cmd += " -tr 0.25 0.25 -wo NUM_THREADS=ALL_CPUS -co 'TILED=YES' -co 'PROFILE=GeoTIFF'"
    cmd += " -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' "
    cmd += " -r bilinear " + VRT + " " + outfile
    print cmd
    os.system(cmd)

    infile = outfile
    outfile = os.path.join(TMPPATH, "tmp_1_" + basename + ".tif")
    cmd = "gdaldem slope -compute_edges " + infile + " " + outfile
    print cmd
    os.system(cmd)

    #infile = outfile
    #outfile = os.path.join(TMPPATH, "tmp_2_" + basename + ".tif")
    #cmd = "gdaldem color-relief " + infile +  " ../ramps/hillshade/ramp_3.txt " + outfile
    #print cmd
    #os.system(cmd)

    infile = outfile
    outfile = os.path.join(TMPPATH, "tmp_3_" + basename + ".tif")
    cmd = "gdalwarp -overwrite -s_srs epsg:2056 -t_srs epsg:2056 -te "  + str(minX) + " " +  str(minY) + " " +  str(maxX) + " " +  str(maxY)
    cmd += " -tr 0.25 0.25 -wo NUM_THREADS=ALL_CPUS -co 'TILED=YES' -co 'PROFILE=GeoTIFF'"
    cmd += " -r bilinear " + infile + " " + outfile
    print cmd
    os.system(cmd)

    infile = outfile
    outfile = os.path.join(OUTPATH, basename + ".tif")
    cmd = "gdal_translate -a_srs epsg:2056  -of GTiff -co 'TILED=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' "
    cmd += " -co 'TILED=YES' -co 'PROFILE=GeoTIFF'"
    cmd += " " + infile + " " + outfile
    print cmd
    os.system(cmd)

    cmd = "gdaladdo -r average "
    cmd += outfile + " 2 4 8 16 32 64 "
    print cmd
    os.system(cmd)

    cmd = "rm -rf " + TMPPATH
    print cmd
    os.system(cmd)

