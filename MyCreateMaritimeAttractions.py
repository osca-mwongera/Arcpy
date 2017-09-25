#-------------------------------------------------------------------------------
# Name:        Working woth selections
#
# Purpose:     Find all major historic attractions in San Diego that are located
#              within the maritime climate zones and expoet them to a new feature
#              class
#
# Author:      Osca Mwongera
#
# Created:     30/08/2017
# Copyright:   (c) omwongera 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r'C:\Student\PYTH\Selections\SanDiego.gdb'

newField1 = arcpy.AddFieldDelimiters(arcpy.env.workspace, "TYPE")

newField2 = arcpy.AddFieldDelimiters(arcpy.env.workspace, "ESTAB")

maritimeSQLExp = newField1 + " = " + " 'Maritime' "

historicSQLExp = newField2 + " > 0 and " + \
    newField2 + "< 1956"

arcpy.MakeFeatureLayer_management("Climate", "MaritimeLyr", maritimeSQLExp)

arcpy.MakeFeatureLayer_management("MajorAttractions", "HistoricLyr", historicSQLExp)

arcpy.SelectLayerByLocation_management("HistoricLyr", "COMPLETELY_WITHIN", "MaritimeLyr", "", "NEW_SELECTION")

featCount = arcpy.GetCount_management("HistoricLyr")

print featCount

arcpy.CopyFeatures_management("HistoricLyr", "MaritimeAttractions")

arcpy.Delete_management("MaritimeLyr")

arcpy.Delete_management("HistoricLyr")

print "Congrats, you did it bro"
