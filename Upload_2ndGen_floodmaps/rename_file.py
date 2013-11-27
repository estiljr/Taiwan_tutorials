import os

os.chdir(r"C:\temp2")
for file in os.listdir("."):
    fileName, fileExtension = os.path.splitext(file)
    fileNum = ""
    baseName = ""
    i=0
    for ch in file:
        if i<16: baseName += ch
        if i>15 and i<len(file)-4: 
            fileNum+=ch
        i+=1
    if len(fileNum) == 1:
        fileNum = "000" + fileNum
    elif len(fileNum) == 2:
        fileNum = "00" + fileNum
    elif len(fileNum) == 3:
        fileNum = "0" + fileNum
    elif len(fileNum) == 4:
        fileNum = fileNum

    newName = baseName + fileNum + fileExtension
    print(file+"-->"+newName)

    os.rename(file,newName)
