#-------------------------------------------------------------------------------
# Name:        da.InsertCursor
#
# Purpose:  Create a new feature class containing a "NAME", "X&Y" to populate
#           the SHAPE field.
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

import arcpy

arcpy.env.workspace = r'C:\Student\PYTH\Cursors\Corvallis.gdb'

arcpy.env.overwriteOutput = True

rowValues = [["Benton", (-123.40, 44.49)], ["Linn", (-122.49, 44.48)], ["Polk", (-123.38, 44.89)], ["Tillamook", (-123.65, 45.45)]]

arcpy.CreateFeatureclass_management(arcpy.env.workspace, "CountyPNT", "POINT")

arcpy.AddField_management("CountyPNT", "NAME", "TEXT")

iCur = arcpy.da.InsertCursor("CountyPNT", ["NAME","SHAPE@XY"])

for row in rowValues:
    iCur.insertRow(row)

del iCur

print "HURAAH, CONGRATS YOU DID IT MEEEEEN"