import os
import subprocess
import glob
import re

fileCase = 1    # 1 if filename format is like xxx_i0005.shp; 2 if xxx_h24i0005.shp
# Deleting first the existing database
layername = 'temp_gi.second_gen_flood_maps'
psql = r"C:\Program Files\PostgreSQL\9.3\bin\psql.exe"
psql_args = '-h UKSD2F0W3J ', '-d taiwan ', '-U taiwan_user ', '-c "DELETE FROM ' , layername
#subprocess.call([psql, psql_args])    
ogr2ogr = r"C:\OSGeo4W\bin\ogr2ogr.exe"
# Changing directory to the specified folder
os.chdir(r"C:\Projects\FM_Global\Taiwan\Data\2nd_Gen_FloodMaps\14_GIS_Pingtung\Pingtung\no_flood_defense")

for file in glob.glob("*.shp"): # loop through files with extension *.shp
    infile = os.path.abspath(file)
    filename, fileExtension = os.path.splitext(file)
    m = re.search("\d", file)

    if fileCase == 1:
        type = file[m.start()-1]    # check whether i,r,h before the number digits
        num_meta = ""
        for index, ch in enumerate(file):
            if index>=m.start() and index<m.start()+4:
                num_meta+=ch
        if type == "i":
            RP = num_meta; rainDepth = "\'\'"; duration = "\'\'"
        elif type == "r":
            RP = "\'\'"; rainDepth = num_meta; duration = "\'\'"
        elif type == "h":
            RP = "\'\'"; rainDepth = "\'\'"; duration = num_meta

    if fileCase == 2:
        type1 = file[m.start()-1]    
        type2 = file[m.start()+2]   # check whether i,r,h before the number digits
        num_meta = ""
        dur_meta = ""
        for index, ch in enumerate(file):
            if index>=m.start() and index<m.start()+2:
                dur_meta+=ch
            if index>=m.start()+3 and index<m.start()+7:
                num_meta+=ch
        if type2 == "i":
            RP = num_meta; rainDepth = "\'\'"; duration = dur_meta
        elif type2 == "r":
            RP = "\'\'"; rainDepth = num_meta; duration = dur_meta

    depth = "\'\'"
    class_ = "CLASS"
    defense = "\'no\'"
    args = '-f PostgreSQL PG:"dbname=taiwan host=UKSD2F0W3J user=taiwan_user password=taiwan" ', infile, \
        ' -nln ', layername, ' -nlt POLYGON ', ' -lco FID=gid ', '-lco GEOMETRY_NAME=geom ', '-s_srs EPSG:3826 ', \
        '-a_srs EPSG:3826 ', '-t_srs EPSG:3826 ', '-sql "SELECT ' + '\''+ filename + '\'' + ' AS name, ' + depth + \
        ' AS depth, ' + class_+ ' AS class, ' + RP + ' AS rp, ' + rainDepth + ' AS rainfall_depth, ' + duration + \
        ' AS duration, ' + defense + ' AS defense FROM ' + filename + '"', ' -append', ' -skipfailure'

    # Upload shapefile to the database
    print(infile)
    subprocess.call([ogr2ogr,args])

psql_vacuum = '-h UKSD2F0W3J ', '-d taiwan ', '-U taiwan_user ', '-c "VACUUM ANALYZE ' , layername
# Refresh the database (vacuum analyze)
subprocess.call([psql, psql_vacuum])

