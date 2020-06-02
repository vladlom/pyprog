checkCicle = 0
while checkCicle == 0:
    try:
        floAt = float(input('Enter    >>>>>   '))
        checkCicle = 1
    except:
        print('Вы ввели не число, повторите ввод!')
        checkCicle =0
print(floAt)
