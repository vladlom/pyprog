cikl = 1
count = 1
checkNo = ['No','no','Нет','нет']
checkYes = ['Yes','yes','Да','да']
checkYesNo = checkNo + checkYes


while cikl == 1:
    cicleCount = 0
    while cicleCount == 0:
        YesNo = input('\nЖелаете продолжить? Введите <Да или Нет>  >>>   ')
        if YesNo in checkYesNo:
            cicleCount = 1
        else:
            print('\n', 'Вы ввели некорректный ответ. Повторите пожалуйста ввод!')
            cicleCount = 0
    if YesNo in checkYes:
        storona1 = int(input('Введите первую сторону >>>'))
        storona2 = int(input('Введите вторую сторону >>>'))
        Ploshad = storona1 * storona2
        print('Площадь равна', Ploshad)
    elif YesNo in checkNo:
        print('-= END =-')
        cikl = 0
        break
#        ciklChek = ciklChek + 1

