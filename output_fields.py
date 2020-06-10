import arcpy
fields = arcpy.ListFields("C:/Projects/AIRO/LARES/GeoDatabases/2. Renewable Energy Planning/wave and tidal REDO/environmental.gdb/Wrecks")
for field in fields:
    print("{0} is a type of {1} with a length of {2}"
    .format(field.name, field.type, field.length))
    

