#function1
def tanah(panjang,lebar):
    luas = panjang * lebar
    return luas

#function2
def harga(luas,hpm):
    jual = luas * hpm
    print('Harga jual tanah :',jual)
    print('------------------------')
    print('------------------------')

#call function
luas = tanah(5,3)
harga(luas,1000)