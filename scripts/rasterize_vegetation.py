#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

TINDEX = "/vagrant/lidar2018.shp"
INPATH = "/lidar2018/01_Punktwolke_LAS/"
OUTPATH = "/Samsung_T5/99_Derivate/vegetation/"
TMPPATH = "/Samsung_T5/99_Derivate/vegetation_tmp/"

shp = ogr.Open(TINDEX)
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
    
    bounds = "(["+str(minX)+","+str(maxX-0.25)+"],["+str(minY)+","+str(maxY-0.25)+"])"

    cmd = 'docker run -v /vagrant/scripts:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation_tmp:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/'+basename+'.las" --writers.gdal.filename="/output/'+basename+'_vegetation.tif" --writers.gdal.bounds="'+bounds+'" --filters.range.limits="Classification[4:5]" /data/rasterize_vegetation.json'
    print cmd
    x = os.system(cmd)
    
    infile = TMPPATH + basename + "_vegetation.tif"
    outfile = OUTPATH + basename + "_vegetation.tif"
    cmd = "gdal_translate -a_srs epsg:2056 "
    cmd += " -co 'TILED=YES' -co 'PROFILE=GeoTIFF'"
    cmd += " -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' "
    cmd += infile + " " + outfile
    print cmd
    os.system(cmd)

    cmd = "gdaladdo -r average "
    cmd += OUTPATH + basename + "_vegetation.tif" + " 2 4 8 16 32 "
    print cmd
    os.system(cmd)

    #break

