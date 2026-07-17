def operasi (operator):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        if num2 == 0:
            return 'undefined'
        else :
            return num1/num2
    else : 
        return 'maaf tanda pilih tanda operasi yg benar dong'

num1 = float(input('nilai pertama : '))
num2 = float(input('nilai kedua : '))

operator = input('masukan operator yg diinginkan (+,-,*,/): ')

hasil = operasi(operator)
print(f'hasil dari operasi {num1} dan {num2} = {hasil}')