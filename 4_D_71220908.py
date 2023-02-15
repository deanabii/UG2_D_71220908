list_nama = []
list_member = []

x = 1
while x == 1:
    print("!! Selamat datang di H+ GYM !!")
    print("Silahkan pilih mennu dibawah ini:")
    print("1. Menambahkan data")
    print("2. Menampilkan data")
    print("3. Keluar")
    pilih = int(input("Silahkan masukkan pilihan yang Anda inginkan: "))

    if pilih == 1:
        nama = str(input("Masukkan nama pelanggan: "))
        member = str(input("Masukkan jenis member: "))
        list_nama += [nama]
        list_member += [member]
        print("Data sudah berhasil ditambahkan")
    elif pilih == 2:
        print("Pelanggan        Member:")
        for i in list_nama:
            print(i," ", end=" ")
        for i in list_member:
            print(i," ", end=" ")
    else:
        print("Sistem Berhenti...")
        break
