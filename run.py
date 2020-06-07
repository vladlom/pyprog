from datetime import datetime
areaBody = open('area_body.db', 'r')
areaBodyR = areaBody.read()
areaBodyR = areaBodyR.rstrip()
areaBody.close()
dateName = str(datetime.now().date())
dateName = dateName.replace('-','')
projectName = dateName + areaBodyR
fileOpen = open(projectName + '.db', 'w')
fileOpen.write(projectName)
fileOpen.close()




areaBodyR = int(areaBodyR)
areaBodyR += 1
areaBodyR = str(areaBodyR)
areaBody = open('area_body.db', 'w')
areaBody.write(areaBodyR)
areaBody.close()

