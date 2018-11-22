def konversi_suhu(C = 0, F = 0):
    "fungsi megkonversi Celcius ke Farenheit atau sebalinya"
    if C != 0:
        x = ((9*C/5) + 32)
        print('Suhu', C,'celcius setara dengan', x, 'Farenheit')
    elif F != 0:
        y = ((F - 32)*5/9)
        print('Suhu', F , 'Farenheit setara dengan', y, 'Celcius')
    else :
        print('suhu 0 celcius setara dengan 32 farenheit')
    return 
        
