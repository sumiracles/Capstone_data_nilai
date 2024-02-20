import sys
from tabulate import tabulate

data = [
    {"NIM": 100100201, "Nama": "Intan", "nilai_UTS": 100, "nilai_UAS": 99, "Praktek": 90},
    {"NIM": 100100202, "Nama": "Rima", "nilai_UTS": 99, "nilai_UAS": 98, "Praktek": 90},
    {"NIM": 100100203, "Nama": "Lisa", "nilai_UTS": 93, "nilai_UAS": 95, "Praktek": 89},
    {"NIM": 100100204, "Nama": "Marina", "nilai_UTS": 97, "nilai_UAS": 99, "Praktek": 90}
]

#main menu
def main():
    while True:
        print('=====================================')
        print('|      Hallo Selamat Datang!        |')
        print('=====================================')
        print('''
        Anda Login Sebagai : 
        1. Dosen
        2. Mahasiswa
        3. Exit
        ''')

        opsilogin = input("Pilih menu:")
        opsilogin = (opsilogin)
        if opsilogin == '1':
            dosen()
        elif opsilogin == '2':
            mahasiswa()
        elif opsilogin == '3':
            print("Terima kasih telah menggunakan program.")
            # break  # Exit the loop and end the program
            sys.exit()
        else:
            print("Input anda invalid!")

#login as dosen
def dosen():
    print('=====================================')
    print('|               Login               |')
    print('=====================================')
    print('\n')
    print('Masukkan kode Login')
    print('\n')
    username = input('Username: ')
    password = input('Password: ')
    if username.lower() == 'admin' and password == '12345':
        menu_dosen()
    else:
        print('Username atau password salah.')
        dosen()
#menu dosen
def menu_dosen():
    while True:
        print('=====================================')
        print('Input Data Nilai Mahasiswa'.center(40))
        print('=====================================')
        print('| 1. Tambah Data                    |')
        print('| 2. Lihat Data Mahasiswa           |')
        print('| 3. Ubah Data Mahasiswa            |')
        print('| 4. Hapus Data Mahasiswa           |')
        print('| 5. Logout                         |')
        print('=====================================')
        pilihmenudosen = input('Pilih Menu : ')
        if pilihmenudosen == '1':
            tambah()
        elif pilihmenudosen == '2':
            read_data()
        elif pilihmenudosen == '3':
            ubah()
        elif pilihmenudosen == '4':
            hapus()
        elif pilihmenudosen == '5':
            selesai()
            break
        else:
            tidak = input('Menu Tidak Ada ')
            menu_dosen()


#menu tambah data 
def tambah():
    print('''
    SILAHKAN TAMBAHKAN DATA!
    ''')
    while True:
        kode = input("Masukkan Nomor Induk Mahasiswa: ")
        existing_nims =str([item['NIM'] for item in data])
       
        if kode in existing_nims:
            print("Nomor Induk Mahasiswa sudah ada dalam data. Silakan masukkan Nomor Induk Mahasiswa yang berbeda.")
        elif kode.isalpha() == True:
            print("masukkan angka saja")
        else:
            break
    kode = int(kode)

    while True:
        nama = input("Masukkan Nama Mahasiswa: ")
        if nama.isnumeric()==True:
            print("masukkan hanya huruf")
        else:
            break

    while True:
        UTS = input("Masukkan Nilai UTS: ")
        if UTS.isalpha()==True:
            print("masukkan hanya Angka")  
        else:
            break


    while True:
        UAS = input("Masukkan Nilai UAS: ")
        if UAS.isalpha()==True:
            print("masukkan hanya Angka")
        else:
            break 

    while True:
        Praktik = input("Masukkan Nilai Praktek: ")
        if Praktik.isalpha()==True:
            print("masukkan hanya Angka")
        else:
            break   


    new_data = {"NIM": kode, "Nama": nama, "nilai_UTS": UTS, "nilai_UAS": UAS, "Praktek": Praktik}
    data.append(new_data)
    print("Data berhasil ditambahkan.")
    kembali = input('tekan [enter] untuk kembali')



#menu read data
def read_data():
    data.sort(key = lambda element:element['NIM'])
    print(tabulate(data, headers='keys', tablefmt='pretty'))
    kembali = input('tekan [enter] untuk kembali')



#menu ubah data
def ubah():
    while True:
        print('=====================================')
        print('Ubah Data Nilai Mahasiswa'.center(40))
        print('=====================================')
        print('| 1. Nilai UTS                      |')
        print('| 2. Nilai UAS                      |')
        print('| 3. Nilai Praktek                  |')
        print('| 4. Kembali                        |')
        print('=====================================')
        pilihmenudosen = input('Pilih Menu : ')
        if pilihmenudosen == '1':
            ubahUTS()
        elif pilihmenudosen == '2':
            ubahUAS()
        elif pilihmenudosen == '3':
            ubahPraktek()
        elif pilihmenudosen == '4':
            menu_dosen()
        else:
            tidak = print("menu tidak ada ")
            ubah()
# Menu Ubah Nilai Mahasiswa UTS
def ubahUTS():
    while True:
        nim = input("Masukkan NIM Mahasiswa: ")
        if nim.isalpha()==True:
            print("masukkan hanya Angka")
        else:
            break  
    found = False

    for student in data:
        if student['NIM'] == int(nim):
            while True:
                new_uts = input(f"Masukkan nilai UTS baru untuk NIM {nim}: ")  
                if new_uts.isalpha() == True:
                    print("masukkan angka saja")
                else:
                    break
            student['nilai_UTS'] = new_uts
            found = True
            print(f"Nilai UTS {nim} berhasil diubah.")
            break
    if not found:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
    
# Menu Ubah Nilai Mahasiswa UAS
def ubahUAS():
    while True:
        nim = input("Masukkan NIM Mahasiswa: ")
        if nim.isalpha()==True:
            print("masukkan hanya Angka")
        else:
            break  
    found = False
    for student in data:
        if student['NIM'] == int(nim):
            while True:
                new_uas = input(f"Masukkan nilai UAS baru untuk NIM {nim}: ")
                if new_uas.isalpha() == True:
                    print("masukkan angka saja")
                else:
                    break
            student['nilai_UAS'] = new_uas
            found = True
            print(f"Nilai UAS {nim} berhasil diubah.")
            break
    if not found:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

# Menu Ubah Nilai Mahasiswa Praktek
def ubahPraktek():
    while True:
        nim = input("Masukkan NIM Mahasiswa: ")
        if nim.isalpha()==True:
            print("masukkan hanya Angka")
        else:
            break  
    found = False
    for student in data:
        if student['NIM'] == int(nim):
            while True:
                new_praktek = input(f"Masukkan nilai Praktek baru untuk data {nim}: ")
                if new_praktek.isalpha() == True:
                    print("masukkan angka saja")
                else:
                    break
            student['Praktek'] = new_praktek
            found = True
            print(f"Nilai Praktek {nim} berhasil diubah.")
            break
    if not found:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")



#menu hapus data
def hapus():

    
    while True:
        nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
        if nim.isalpha()==True:
            print("Masukkan hanya angka saja")
        else:
            break
    nim = int(nim)
    index_to_remove = None
    for i, student in enumerate(data):
        if student['NIM'] == nim:
            index_to_remove = i
            break
    if index_to_remove is not None:
        del data[index_to_remove]
        print(f"Data mahasiswa dengan NIM {nim} telah dihapus.")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")


#menu mahasiswa
def mahasiswa():
    print('=====================================')
    print('Data Mahasiswa'.center(40))
    print('=====================================')
    
    
    # Input NIM to display data
    while True:
        nim = input("Masukkan NIM Mahasiswa: ")
        if nim.isalpha()==True:
            print("masukkan hanya Angka")
        else:
            break   

    found = False
    
    # Find and display data for the inputted NIM
    for student in data:
        if student['NIM'] == int(nim):
            print(tabulate([student], headers='keys', tablefmt='pretty'))
            found = True        
            break
    
    # If NIM is not found, display a message
    if not found:
        print("Data mahasiswa tidak ditemukan")
    
    kembali = input('Tekan [enter] untuk kembali')

def selesai():
    main()

main()
