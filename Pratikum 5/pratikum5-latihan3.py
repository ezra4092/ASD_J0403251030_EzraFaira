# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Latihan 3: Mencari Nilai Maksimum
# ===========================================

def cari_maks(data, index=0):
    # base case, jika index sudah berada di elemen terakhir list maka tidak ada lagi yang perlu dibandingkan
    # sehingga langsung kembalikan nilai elemen tersebut
    if index == len(data) - 1:
        return data[index]
    
    #recursive case, mencari nilai maksimum dengan memanggil fungsi yang sama
    maks_sisa = cari_maks(data, index + 1)

    # setelah mendapatkan maksimum dari sisa elemen,
    # bandingkan dengan elemen pada index sekarang
    if data[index] > maks_sisa:
        #jika elemen sekarang lebih besar, maka elemen sekarang adalah maksimum sementara
        return data[index]
    else:  # jika maksimum dari sisa elemen lebih besar, maka kembalikan nilai tersebut
        return maks_sisa

# contoh data
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))