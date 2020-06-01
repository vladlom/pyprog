checkListYes = ['Yes', 'yes', 'Да', 'да']
checkListNo = ['No', 'no', 'Нет', 'нет']
check = 0
progBody = 0


def checkEnterYesNo(InPuT):
    if InPuT in checkListYes:
        return 2
    elif InPuT in checkListNo:
        return 1
    else:
        return 3


while progBody == 0:
    InPuT = str(input('Do you whant to calculate the area?'))
    check = checkEnterYesNo(InPuT)
    if check == 2:
        length = int(input('Enter length >>>  '))
        width = int(input('Enter width >>>  '))
        print('The area is  ', length * width)
        progBody = 0
    elif check == 1:
        print(' -= END =- ')
        progBody = 1
    else:
        print('<<< Please retype!!! >>>')



