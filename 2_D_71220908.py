nomor = input("Masukkan Nomor Telepon : ").split()

def jenis():
    if nomor == [0,8,1,6]:
        print("Anda menggunakan operator Indosat")
    elif nomor == [0,8,1,4]:
        print("Anda menggunakan operator Telkomsel")
    else:
        print("Operator anda tidak diketahui")
