import glob
import os

folder_main = r"C:\Projects\FM_Global\Taiwan\Data\2nd_Gen_FloodMaps"
os.chdir(folder_main)

for folder in os.listdir(folder_main):
    os.chdir(os.path.abspath(folder))
    print(os.path.abspath(folder))
#    for file in glob.glob("*.shp"):
#        print(file)
    os.chdir(r"C:\Projects\FM_Global\Taiwan\Data\2nd_Gen_FloodMaps")