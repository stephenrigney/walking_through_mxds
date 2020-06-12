import arcpy
import os

arcpy.env.workspace = "C:/Projects/AIRO/LARES/GeoDatabases/2. Renewable Energy Planning/"
output_workspace = "C:/Projects/AIRO/LARES/GeoDatabases/outputs"

#getting a syntax error here. I know why because the use of def is not right, I know this.
def fields(arcpy.ListFields("C:/Projects/AIRO/LARES/GeoDatabases/2. Renewable Energy Planning/"))
for field in fields:
         print("{0} is a type of {1} with a length of {2}"
         .format(field.name, field.type, field.length))


workspace = "C:/Projects/AIRO/LARES/GeoDatabases/2. Renewable Energy Planning/"
feature_classes = []
rasters = []

walk = arcpy.da.Walk(workspace, datatype="FeatureClass", type="Polygon")
walk_r = arcpy.da.Walk(workspace, topdown=True, datatype="RasterDataset")

for dirpath, dirnames, filenames in walk:
     for filename in filenames:
         feature_classes.append(os.path.join(dirpath, filename))
         print(filename)
         print(dirpath)

for dirpath, dirnames, filenames in walk_r:
     for filename_r in filenames:
         feature_classes.append(os.path.join(dirpath, filename_r))
         print(filename_r)
         print(dirpath)


     
