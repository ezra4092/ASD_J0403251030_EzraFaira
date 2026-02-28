# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1
# ===========================================

# ===========================================
# Latihan 5: Generator PIN
# ===========================================

def buat_pin(panjang, hasil=""):
    # base case, mengecek panjang 'hasil' sudah sesuai sama dengan panjang pin yg diminta
    if len(hasil) == panjang:
        print("PIN", hasil) # jika sudah cukup, tampilkan pin
        return # hentikan rekursi
    
    # jika belum cukup panjang, ulangi untuk setiap pilihan angka (0,1,2)
    for angka in['0', '1', '2']:
        
        # recursive case, tambahkan satu angka ke 'hasil'
        # lalu panggil fungsi lagu untuk melanjutkan
        buat_pin(panjang, hasil + angka)

buat_pin(2)