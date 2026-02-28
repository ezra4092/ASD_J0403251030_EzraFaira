# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Materi Rekursif: Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# masuk 1 - 2 -3
# keluar
# ===========================================

def hitung(n):
    if n == 0:
        print("selesai")
        return
    print("Masuk:", n)
    hitung(n-1) # recursuve case
    print("keluar", n)

print("==========Program Tracing==========")
hitung(3)
