#-------------------------------------------------------------------------------
# Name:        da.SearchCursor
#
# Purpose:  Making a list of a three-line address-style from a feature class
#
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

arcpy.env.workspace = r'C:\Student\PYTH\Cursors\SanDiego.gdb'

with arcpy.da.SearchCursor("MajorAttractions", ["NAME", "ADDR", "CITYNM", "ZIP"]) as cursor:
    for row in cursor:
        print "{}\n".format(row)