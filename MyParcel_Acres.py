#-------------------------------------------------------------------------------
# Name:        da.UpdateCursor
#
# Purpose:  Adding a new field to a feature class and populating it with values
#
# Author:      Osca Mwongera
#
# Created:     31/08/2017
# Copyright:   (c) omwongera 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os

import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r'C:\Student\PYTH\Cursors\Corvallis.gdb'

arcpy.AddField_management("Parcel", "ACRES", "Double")

with arcpy.da.UpdateCursor("Parcel", ["SHAPE@AREA", "ACRES"]) as cursor:
    for row in cursor:
       geom = row[0]
       row[1] = geom / 43560
       cursor.updateRow(row)

print "This far we have come"
