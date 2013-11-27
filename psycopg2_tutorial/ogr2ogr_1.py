import os
import subprocess
import glob
import re

# Deleting first the existing database
layername = 'temp_gi.second_gen_flood_maps'
psql = r"C:\Program Files\PostgreSQL\9.3\bin\psql.exe"
psql_args = '-h UKSD2F0W3J ', '-d taiwan ', '-U taiwan_user ', '-c "DELETE FROM ' , layername
subprocess.call([psql, psql_args])
    
ogr2ogr = r"C:\OSGeo4W\bin\ogr2ogr.exe"
# Changing directory to the specified folder
os.chdir(r"C:\temp\Hsinchu")

for file in glob.glob("*.shp"):
    infile = os.path.abspath(file)
    print(infile)
    filename, fileExtension = os.path.splitext(file)
    args = '-f PostgreSQL PG:"dbname=taiwan host=UKSD2F0W3J user=taiwan_user password=taiwan" ', infile, \
        ' -nln ', layername, ' -nlt POLYGON ', ' -lco FID=gid ', '-lco GEOMETRY_NAME=geom ', '-s_srs EPSG:3826 ', \
        '-a_srs EPSG:3826 ', '-t_srs EPSG:3826 ', '-sql "SELECT CLASS AS class FROM '+ filename+ '"', ' -append '

    # Upload shapefile to the database
    subprocess.call([ogr2ogr,args])

