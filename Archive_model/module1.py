import sys
import os
import subprocess
import glob

def archive_model(dir_model, archive_name, mode):

    os.chdir(dir_model)
    if mode == "all":
        inc = "*"
    elif mode == "noDat":
        inc = "*.dat"
    
    for root, dirnames, filenames in os.walk(dir_model):
        #print (root)
        print(filenames)
        #print(filenames)



    #for file in glob.glob(inc):
    #    exe7z = r"C:\Program Files\7-Zip\7za.exe"
    #    args = 'a ',archive_name,'.zip ',file
    #    #subprocess.call([exe7z, args], shell=True)


dir_model = r"C:\isis\data\examples\ISIS 2D\Coastal"
archive_name = r"C:\temp\model1_v1"
mode = "noDat"
archive_model(dir_model, archive_name, mode)
