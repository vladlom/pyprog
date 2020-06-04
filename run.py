cikl = 1
count = 0
checkNo = ['No','no','Нет','нет']
checkYes = ['Yes','yes','Да','да']
checkYesNo = checkNo + checkYes


def checkFloat(count):
    checkCicle = 0
    while checkCicle == 0:
        try:
            floAt = float(input(' >>>>>   '))
            checkCicle = 1
        except:
            print('Вы ввели не число, повторите ввод!')
            checkCicle =0
            count = count - 1
    return floAt, count


while cikl == 1:
    cicleCount = 0
    while cicleCount == 0:
        count = count + 1
        if count == 1:
            print('Добро пожаловать в программу вычисления площади окна. =)')
            YesNo = 'Yes'
            cicleCount = 1
        else:
            YesNo = input('Желаете продолжить? Введите <Да или Нет>  >>>   ')
            if YesNo in checkYesNo:
                cicleCount = 1
            else:
                print('Вы ввели некорректный ответ. Повторите пожалуйста ввод!')
                cicleCount = 0
                count = count - 1
    if YesNo in checkYes:
        strCount = str(count)
        print('Введите высоту ' + strCount + '-го окна. ', end=' ')
        windowHeight = checkFloat(count)
        print('Введите ширину ' + strCount + '-го окна. ', end=' ')
        windowWidth = checkFloat(count)
        windowArea = windowHeight[0] * windowWidth[0]
        print('Площадь ' + strCount + '-го окна равна', windowArea)
        strWindowHeight = 'Высота ' + strCount + '-го окна = ' + \
                str(windowHeight[0]) + '\n'
        strWindowWidth = 'Ширина ' + strCount + '-го окна = ' + \
                str(windowWidth[0]) + '\n'
        strWindowArea = 'Площадь ' + strCount + '-го окна = ' + \
                str(windowArea) + '\n\n'
        if count == 1:
            fileOpen = open('area.txt', 'w')
        else:
            fileOpen = open('area.txt', 'a')
        fileOpen.write(strWindowHeight)
        fileOpen.write(strWindowWidth)
        fileOpen.write(strWindowArea)
        fileOpen.close()
    elif YesNo in checkNo:
        print('-= Конец прогрвммы, выход. =-')
        cikl = 0
        break
