#-------------------------------------------------------------------------------
# Name:     Points Feaure shapefile to Excel
# Purpose:  Converts features in a shapefile and writes it on an excel table
#           (.csv) including the longitude and latitude and other columns
#           containing attributes.
#
# Author:      Osca Mwongera
#
# Created:     16/12/2017
# Copyright:   (c) Osca 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


# Import your modules

import arcpy

import os

import csv

# Set your working environment

arcpy.env.workspace = r'G:\WorkSpace\DataOut'

# This variable holds our data

dataset = r'G:\Data\DESKTOP-V3SFD1T\Osca\Fwd__location_data_(set_in_UTMs)\Peprojected.shp'

# This will be our final output find. It will be placed in the same directory as
# the script

outfile = r'file.csv'

# I use overwriteOutput as True so that I don't get errors when I run the srcipt
# over and over during development.

arcpy.env.overwriteOutput = True

# These are the fields I want to get from the shapefile 'object id, x-coord,
# y-coord, Date, Surveyor, ActualPnt'. They are unique to my shapefile feel free
# to adjust depending on the fields you want to get and also the columns in your
# shapefile

fields = ["OID@", "SHAPE@X", "SHAPE@Y", "Date", "Surveyor", "ActualPnt"]

# field names these will be our column names in the csv that we genetate

field_names = ["Object ID", "X", "Y", "Date", "Surveyor", "ActualPnt"]

with open(outfile,'wb') as f:
            w = csv.writer(f)
    #--write all field names to the output file
            w.writerow(fields_names)

            # using the searchcursor and a for loop loop through the rows in the
            # shapefile writing the field values to our csv file.

            with arcpy.da.SearchCursor(dataset, fields) as cursor:
                for row in cursor:
                    field_vals = [row[0], row[1], row[2], row[3], row[4], row[5]]
                    w.writerow(field_vals)
                    print (row)
                del row

