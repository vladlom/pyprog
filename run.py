def checkFloat():
    checkCicle = 0
    while checkCicle == 0:
        try:
            floAt = float(input('Enter    >>>>>   '))
            checkCicle = 1
        except:
            print('Вы ввели не число, повторите ввод!')
            checkCicle =0
    return floAt


wiDth = 0
wiDth1 = checkFloat()
wiDth2 = checkFloat()

print('* 2 =   ', wiDth1 + wiDth2)
