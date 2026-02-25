#========IDENTITAS MAHASISWA================================
#NAMA : Ezra Faira Azzahra Faisal
#NIM : J0403251030
#Kelas : B / P1
#===========================================================

# ========================================================== 
# Tugas Hands-On: Sistem Antrian Bengkel Motor 
# ========================================================== 

# 1) mendefinisikan node
class Node: 
    def __init__(self, no, nama, servis): 
        self.no = no # menyimpan nomor
        self.nama = nama  # menimpan nama
        self.servis = servis # menyimpan jenis servis
        self.next = None 

# 2) mendefinisikan queue
class QueueBengkel: 
    def __init__(self): 
        self.front = None 
        self.rear = None

    def is_empty(self):
        # ketika queue kosong, maka front dan rear adalah none
        return self.front is None

    # fungsi menambahkan data baru ke belakang rear
    def enqueue(self, no, nama, servis):
        # data disimpan dalam node
        nodeBaru = Node(no, nama, servis)

        # jika queue kosong, data baru menjadi front dan rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, data baru diletakkan setelah rear kemudian dijadikan rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru
    
    # fungsi menghapus front dan memindahkan ke next front
    def dequeue(self):
        # jika queue kosong, menampilkan informasi bahwa antrian kosong
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan yang harus dilayani \n")
            return None
        
        # data pada front akan dihapus (dilayani)
        diservis = self.front

        # geser pointer front ke next front
        self.front = self.front.next

        # jika front menjadi none, maka front = rear = none
        if self.front is None:
            self.rear = None
        
        return diservis
    
    # fungsi menampilkan queue
    def tampilkan(self):
        # jika queue kosong, menampilkan informasi bahwa antrian kosong
        if self.is_empty():
            print("Antrian kosong\n")
            return None
        
        # menampilkan queue dari front sampe rear
        print("Daftar Antrian Bengkel:")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.no} - {current.nama} ({current.servis})")
            current = current.next
            no += 1
        

# program utama
def main():
    #instiantiasi queue
    q = QueueBengkel()
    while True:
        print("=== Sistem Antrian Bengkel ===")            
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu (1-4): ").strip()

        if pilih == "1":
            no = input("Masukkan nomor antrian: ").strip()
            nama = input("Masukkan nama pelanggan: ").strip()
            servis = input("Masukkan jenis servis: ").strip()
            q.enqueue(no, nama, servis)
            print("Data pelanggan berhasil ditambahkan ke antrian \n")

        elif pilih == "2":
            diservis = q.dequeue()
            if diservis is not None:
                print(f"Pelanggan yang dilayani: {diservis.nama} - {diservis.servis}") 

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Program selesai. Terimakasih")
            break

        else:
            print("Pilihan tidak valid.")

# menjalankan fungsi main()
if __name__ == "__main__":
    main()


    

