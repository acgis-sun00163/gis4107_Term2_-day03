# -*- coding: utf-8 -*-
# ================================================================================================
# Ex 02- Part A
# name: use search cursor.py
# Created on: 2020-01-22
# Create by Chengjiaqi Sun
# Puropose:
# Description: python 3.x
# ================================================================================================

# 1. import system modules
# -------------------------------
import os
import sys
import arcpy

# 2. allow overwrite the environment

arcpy.env.overwriteOutput = True


# 3. setting local variables
out_folder_path = "D:\\GIS4207_programming\\EX02\\02_working"

out_gdb = "EX2_searchcursor.gdb"

inputFC = "D:\\GIS4207_programming\\EX02\01_source\\GIS4207_EX_01_A_B_Sample_Data\\031f14\\031F14_haz_air_p.shp"

# 4. create the gdb
arcpy.CreateFileGDB_management(out_folder_path, out_gdb)

 # 4.1 decide the output filename
outputFC = inputFC.split('_',1).rstrip('.shp')

# 5. load feature class to gdb
arcpy.FeatureClassToGeodatabase_conversion([inputFC, outputFC],out_gdb)


# 6. set the spatial reference
out_coordinate_system = arcpy.SpatialReference('NAD 1983 UTM Zone 18N')

# 7. list interested fileds from haz_air_p.shp attribute table
fileds_name = [ID, SHAPE@XY, HEIGHT, TYPE]

# 8. sql clause to redorder all rows of haz_air_p.shp, dont understand  ---- HELP !!!!
sql_where_clase (select filed_name  from feature calss  where name like ""  Height asending )

# 9. using search cursor fine the target shapfile and list the wanted attributes ?????? Help !
target_fc_cursor = arcpy.SearchCursor (out_gdb, sql_where_clase, out_coordinate_system, fc_name,)


# 10. use the loop to print all rows

for rows in target_fc_cursor:
    print ("" % ())

    print(str.format( )



