cikl = 1
count = 1
checkNo = ['No','no','Нет','нет']
checkYes = ['Yes','yes','Да','да']
checkYesNo = checkNo + checkYes


def checkFloat():
    checkCicle = 0
    while checkCicle == 0:
        try:
            floAt = float(input(' >>>>>   '))
            checkCicle = 1
        except:
            print('Вы ввели не число, повторите ввод!')
            checkCicle =0
    return floAt


while cikl == 1:
    cicleCount = 0
    while cicleCount == 0:
        YesNo = input('\n Желаете продолжить? Введите <Да или Нет>  >>>   ')
        if YesNo in checkYesNo:
            cicleCount = 1
        else:
            print('\n Вы ввели некорректный ответ. Повторите пожалуйста ввод!')
            cicleCount = 0
    if YesNo in checkYes:
        print('Введите высоту окна. ', end=' ')
        windowHeight = checkFloat()
        print('Введите ширину окна. ', end=' ')
        windowWidth = checkFloat()
        windowArea = windowHeight * windowWidth
        print('Площадь окна равна', windowArea)
        strWindowHeight = '  Высота окна  ' + str(windowHeight) + '\n'
        strWindowWidth = '  Ширина окна  ' + str(windowWidth) + '\n'
        strWindowArea = '  Площадь окна  ' + str(windowArea) + '\n'
        fileOpen = open('area.txt', 'w')
        fileOpen.write(strWindowHeight)
        fileOpen.write(strWindowWidth)
        fileOpen.write(strWindowArea)
        fileOpen.close()
    elif YesNo in checkNo:
        print('-= Конец прогрвммы, выход. =-')
        cikl = 0
        break
#        ciklChek = ciklChek + 1

