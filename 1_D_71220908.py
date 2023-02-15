print("="*10, "MAKANAN", "="*10)
print("1. Telur Bakar       : Rp 7.000")
print("2. Lele Terbang      : Rp 10.000")
print("3. Es Coklat         : Rp 5.000")
print("4. Es Doger          : Rp 13.000")
print("="*10, "PESANAN", "="*10)

telur = int(input("Telur Bakar      :"))
lele = int(input("Lele Terbang      :"))
cklt = int(input("Es Coklat         :"))
doger = int(input("Es Doger         :"))

print("="*10, "TOTAL", "="*10)

def tlr_bakar():
    bakar = telur * 7000
    return bakar
def lele_trbng():
    terbang = lele * 10000
    return terbang
def s_coklat():
    ess = cklt * 5000
    return ess
def es_dgr():
    es = doger * 13000
    return es
def total():
    jmlh = bkr + ll + ckl + dog
    return jmlh

bkr = tlr_bakar()
ll = lele_trbng()
ckl = s_coklat()
dog = es_dgr()
tot = total()

print("TOTAL TELUR BAKAR x ", telur,":",bkr)
print("TOTAL LELE TERBANG x", lele, ":", ll)
print("TOTAL ES COKLAT x ", cklt, ":", ckl)
print("TOTAL ES DOGER x ", doger, ":", dog)
print("Jumlah total biaya yang harus dibayar adalah Rp ", tot)