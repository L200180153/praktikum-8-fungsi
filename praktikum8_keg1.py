## kegiatan 1.
D = {'NIM' : 'L200180153', 'Nama' : 'Anita Lusi Romadhon', 'Alamat' : 'Sragen', 'Asal' : 'Tangen', 'Email' : 'anitalusi90@gmail.com', 'Hobi' : 'Makan', 'Prodi' : 'Informatika'}
def nim() :
    "fungsi ini untuk menampilkan nim"
    print ('NIM:', D['NIM'])
    return
def nama() :
    "fungsi ini untuk menampilkan nama"
    print ('Nama :', D['Nama'])
    return
def alamat() :
    "fungsi ini untuk menampilkan alamat"
    print ('Alamat :', D['Alamat'])
    return
def email() :
    "fungsi ini untuk menampilkan email"
    print ('Email :', D['Email'])
    return
def asal() :
    "fungsi ini untuk menampilkan asal"
    print ('Asal :', D['Asal'])
    return
def hobi() :
    "fungsi ini untuk menampilkan hobi"
    print ('Hobi :', D['Hobi'])
    return
def prodi() :
    "fungsi ini untuk menampilkan prodi"
    print ('prodi :', D['prodi'])
    return
print('\n NIM l200180153' +
      '\n Nama Anita Lusi Romadhon' +
      '\n Alamat Sragen Jawa Tengah' +
      '\n Asal Tangen' +
      '\n Email anitalusi90@gmail.com' +
      '\n Hobi Makan' +
      '\n Prodi Informatika')

print ('Pilihan yang tersedia :'+
       '\nb menampilkan bantuan ini'+
       '\nN menampilkan NIM'+
       '\na menampilkan Nama'+
       '\nA menampilkan Alamat'+
       '\nL menampilkan Email'+
       '\nK menampilkan Asal'+
       '\nH menampilkan Hobi'+
       '\nP menampilkan Prodi'+
       '\nk Keluar')
for x in range(9):
    p = str(input('Masukkan Pilihan Anda :'))
    if p == 'N':
        NIM()
    elif p == 'a':
        nama()
    elif p == 'A':
        alamat()
    elif p == 'L' :
        email()
    elif p == 'K' :
        asal()
    elif p == 'H' :
        hobi()
    elif p == 'P':
        prodi()
    elif p == 'k' :
        print('Terimakasih.')
    elif p == 'b':
        ('Pilihan yang tersedia :'+
       '\nb menampilkan bantuan ini'+
       '\nN menampilkan NIM'+
       '\na menampilkan Nama'+
       '\nA menampilkan Alamat'+
       '\nL menampilkan Email'+
       '\nK menampilkan Asal'+
       '\nH menampilkan Hobi'+
       '\nP menampilkan Prodi'+
       '\nk Keluar')
    else :
        ('perintah tidak dikenal')
    
