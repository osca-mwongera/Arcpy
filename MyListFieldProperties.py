#-------------------------------------------------------------------------------
# Name:        List field properties
# Purpose:     Listing field properties and writing them to a text file.
#
# Author:      Osca Mwongera
#
# Created:     28/08/2017
# Copyright:   (c) omwongera 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os

import arcpy

wksp = "C:\Student\PYTH\Automating_scripts"

arcpy.env.workspace = os.path.join(wksp, "SanDiego.gdb")

field_list = arcpy.ListFields("MajorAttractions")

txtFile = open(os.path.join(wksp, "MajorAttractions.txt"), "w")

txtFile.write("MajorAttractions field information" + "\n")

txtFile.write("----------------------------------" + "\n")

for field in field_list:
    line = "Name: {}, Type: {}, Length: {}\n".format(
        field.name, field.type, field.length)
    txtFile.write(line)

txtFile.close()

print "Wira ni urarika!!"