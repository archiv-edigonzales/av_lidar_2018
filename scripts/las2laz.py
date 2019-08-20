#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

#VRT = "/lidar2018/99_Derivate/dtm_25cm/dtm_25cm.vrt"
TINDEX = "/vagrant/lidar2018.shp"
INPATH = "/lidar2018/01_Punktwolke_LAS/"

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

    cmd = 'docker run -v /vagrant/scripts:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/laz:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/'+basename+'.las" --writers.las.filename="/output/'+basename+'.laz" /data/las2laz.json'
    print cmd
    x = os.system(cmd)


    #break

