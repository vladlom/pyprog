from datetime import datetime


areaBody = open('area_body.db', 'r')
areaBodyR = areaBody.read()
areaBodyR = areaBodyR.rstrip()
areaBody.close()


dateName = str(datetime.now().date())
dateName = dateName.replace('-','')
projectName = dateName + areaBodyR


fileOpen = open(projectName + '.db', 'w')
fileOpen.write('project No ' + projectName + '\n')
name = input('Please enter nama of the customer >>> ')
surname = input('Please enter surname of the customer >>> ')
address = input('Please enter address of the customer >>> ')
phone = input ('Please enter phone of the customer >>> ')
fileOpen.write('Name - ' + name + '\n')
fileOpen.write('Surname - ' + surname + '\n')
fileOpen.write('Address - ' + address + '\n')
fileOpen.write('Phone number - ' + phone + '\n')
fileOpen.close()




areaBodyR = int(areaBodyR)
areaBodyR += 1
areaBodyR = str(areaBodyR)


areaBody = open('area_body.db', 'w')
areaBody.write(areaBodyR)
areaBody.close()

