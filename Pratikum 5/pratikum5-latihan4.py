# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Latihan 4: Kombinasi Huruf
# ===========================================

def kombinasi (n, hasil=""):
    # base case, jika panjang dari hasil sudah sama dengan n
    # maka akan mengembalikan nilai hasil dan menghentikan program
    if len(hasil) == n:
        print(hasil)
        return
    
    #recursive case, tambahkan "A" lalu lanjut rekursi
    kombinasi(n, hasil + "A")
    #recursive case, tambahkan "B" lalu lanjut rekursi
    kombinasi(n, hasil + "B")

kombinasi(3)