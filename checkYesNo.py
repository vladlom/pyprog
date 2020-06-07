checkYesNo = ['Yes','yes','No','no','Да','да','Нет','нет']
cicleCount = 0
while cicleCount == 0:
    YesNo = input('\nЖелаете продолжить? Введите <Да или Нет>  >>>   ')
    if YesNo in checkYesNo:
        cicleCount = 1
    else:
        print('\n', 'Вы ввели некоректный ответ. Повторите пожалуйста ввод!')
        cicleCount = 0
print('\n', YesNo)
