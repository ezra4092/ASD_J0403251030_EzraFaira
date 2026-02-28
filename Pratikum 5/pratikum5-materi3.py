# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Materi rekursif: menjumlahkan elemen list
# ===========================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    
    #recursive case
    return data[index] + jumlah_list(data, index+1)

print("=========Program Jumlah Data List==========")
print(jumlah_list([2,4,5]))