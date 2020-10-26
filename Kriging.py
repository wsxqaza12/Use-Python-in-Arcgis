# -*- coding: cp950 -*-
# MakeXYLayer.py
# Description: Creates an XY layer and exports it to a layer file

print("import system modules")
# import system modules 
import arcpy
import os
from arcpy import env
from arcpy.sa import *

print("Set environment settings")
# Set environment settings
arcpy.env.workspace = "D:/Dengue/Month_data/Add_XY/"
arcpy.env.extent = "C:/Users/User/Desktop/登革熱/Village_shp/Village_NLSC_121_1050715.shp"

day = 1
month = 1
year = 2014

print("define do() function")
def do():

    if month < 10:
        month2 = str(0) + str(month)
    else:
        month2 = str(month)


    fileadr = "D:/Dengue/Month_data/Add_XY/Rainfall"  + "_" +  str(year) + "_" + str(month) + ".lyr"

    if os.path.isfile(fileadr):
        try:
            print("Set the local variables")
            
            inFeatures = "D:/Dengue/Month_data/Add_XY/Rainfall" + "_" + str(year) + "_" + str(month) +  ".lyr"
            field = "Rainfall"
            cellSize = 0.0009009009
            outVarRaster = "D:/Dengue/Month_data/Result_Kriging/"   + "_" +  str(year) + "_" + str(month)  
            lagSize = 0.015129
            majorRange = "#"
            partialSill = "#"
            nugget = "#"

            kModelOrdinary = KrigingModelOrdinary("Spherical", lagSize,
                                majorRange, partialSill, nugget)
            kRadius = RadiusVariable(12, "#")



            # Check out the ArcGIS Spatial Analyst extension license
            arcpy.CheckOutExtension("Spatial")

            # Execute Kriging
            outKriging = Kriging(inFeatures, field, kModelOrdinary, 0.0009009009,
                     kRadius, outVarRaster)
            
            print ("Rainfall"  + "_" +  str(year) + "_" + str(month) + ".dbf is OK")
            
        except Exception as err:
            print(err.args[0])
            pass
        
    else:
        print ("Rainfall"  + "_" +  str(year) + "_" + str(month) + ".dbf does not exist.")
        
while year <= 2015:
    while month <= 12:
        do()
        month += 1
    year += 1
    month = 1
    day = 1
    
