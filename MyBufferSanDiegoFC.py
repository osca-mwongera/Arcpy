#-------------------------------------------------------------------------------
# Name:        Buffering features
# Purpose:
#
# Author:      Osca Mwongera
#
# Created:     29/08/2017
# Copyright:   (c) omwongera 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os

import arcpy

arcpy.env.workspace = r'C:\Student\PYTH\Automating_scripts\SanDiego.gdb'

fc_list = arcpy.ListFeatureClasses()

for featClass in fc_list:
    desc = arcpy.Describe(featClass)
    if desc.shapeType =='Point':
     buffDist = '1000 feet'
    elif desc.shapeType == 'Polyline':
     buffDist = '500 feet'
    elif desc.shapeType == 'Polygon':
     buffDist = '-750 feet'
    arcpy.Buffer_analysis (in_features = featClass, out_feature_class = featClass + "_Buff", buffer_distance_or_field = buffDist)

print "I excelled in this lesson, you are a champ"