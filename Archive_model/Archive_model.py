import sys
import os
import subprocess
import glob

def archive_model(dir_model, archive_folder, mode):

    folderName = os.path.basename(dir_model)
    fileNum = 1
    while(os.path.exists(archive_folder+"\\"+folderName+"_v"+str(fileNum)+".zip")):
        fileNum += 1
    newFolderName
    print(archive_folder+"\\"+folderName+"_v"+str(fileNum)+".zip")

    os.chdir(dir_model)

    for file in glob.glob("*"):
        if mode == "all":
            args = 'a ',archive_folder,'.zip ',file
        elif mode == "noDat":
            args = 'a ',archive_folder,'.zip ',file,' -xr!*.dat'
        exe7z = r"C:\Program Files\7-Zip\7za.exe"
        #subprocess.call([exe7z, args], shell=True)




dir_model = r"C:\isis\data\examples\ISIS 2D\Coastal"
archive_folder = r"C:\temp"
mode = "noDat"
archive_model(dir_model, archive_folder, mode)

