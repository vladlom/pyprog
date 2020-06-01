cikl = 1
count = 1
chekYes = ['Yes', 'yes', 'Да', 'да']
chekNo = ['No', 'no', 'Нет', 'нет']
chek = chekYes + chekNo



while cikl == 1:
    newPloshad = str(input("Будем считать площадь? Да или Нет >>>"))
    ciklChek = 0
    while ciklChek <= 3:
        if newPloshad == chekYes[ciklChek]:
            storona1 = int(input('Введите первую сторону >>>'))
            storona2 = int(input('Введите вторую сторону >>>'))
            Ploshad = storona1 * storona2
            print('Площадь равна', Ploshad)
        elif newPloshad == chekNo[ciklChek]:
            print('-= END =-')
            cikl = 0
            break
#        elif newPloshad != chek[ciklChek]:
#            print('Неверный ввод, повторите')
        ciklChek = ciklChek + 1

