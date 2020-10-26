# MakeXYLayer.py
# Description: Creates an XY layer and exports it to a layer file

print("import system modules")
# import system modules 
import arcpy
import os
import os.path

print("Set environment settings")
# Set environment settings
arcpy.env.workspace = "D:/Dengue/Month_data/Temp and Rain (2014 - 2015)/"


day = 1
month = 1
year = 2014

print("define do() function")
def do():

    if month < 10:
        month2 = str(0) + str(month)
    else:
        month2 = str(month)

        
    fileadr = "D:/Dengue/Month_data/Temp and Rain (2014 - 2015)/Temp"  + "_" +  str(year) + "_" + str(month) + ".dbf"

    if os.path.isfile(fileadr):
        try:
            print("Set the local variables")
            
            # Set the local variables
            in_Table = "D:/Dengue/Month_data/Temp and Rain (2014 - 2015)/Temp"  + "_" +  str(year) + "_" + str(month) + ".dbf"
            x_coords = "Lon"
            y_coords = "Lat"
            #z_coords = ""


            print("Set the saved Layer Name and Outlayer name")
            saved_Layer = "D:/Dengue/Month_data/Add_XY/Temp"  + "_" +  str(year) + "_" + str(month) + ".lyr"
            out_Layer = "Temp" + "_" + str(year) + "_" + str(month2) + ".lyr"
            
            print("Set the spRef")
            spRef = "C:/Users/User/Desktop/µn­²¼ö/Village_shp/Village_NLSC_121_1050715.shp"
            
            print("Make the XY event layer")
            # Make the XY event layer...
            arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef)
            
            print("Print the total rows")
            # Print the total rows
            print arcpy.GetCount_management(out_Layer)
            
            print("Save to a layer file")
            # Save to a layer file
            arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
            
            print ("Temp " + str(year) + "/" + str(month2) + "/"  + " DONE")
            
        except Exception as err:
            print(err.args[0])
            pass
        
    else:
        print ("a" + str(year) + "_" + str(month) + "_" + str(day) + ".dbf does not exist.")
        
while year <= 2015:
    while month <= 12:
        do()
        month += 1
        
    year += 1
    month = 1
    day = 1
    
