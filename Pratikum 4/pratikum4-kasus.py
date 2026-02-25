# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1

# ===========================================
# Studi Kasus: Sistem antrian layanan akademik
# Implementasi queue
# Enqueue: memindahkan pointer rear (tambah data baru dari belakang)
# Dequeue: memidahkan pointer front (menghapus data dari depan)
# Front-> A -> B -> C -> Rear
# ===========================================

# 1) Mendefinisikan Node (unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim # menyimpan nim mahasiswa
        self.nama = nama # menyimpan nama mahasiswa
        self.next = None # menyimpan ke node berikutnya

# 2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        # ketika queue kosong makan front = rear = none
        return self.front is None 
    
    # menambahkan data baru ke bagian belakang (rear) => menambahkan mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self, nim, nama):
        # jika data baru masuk dari queue yang kosong makan data baru = front = rear
        nodeBaru = Node(nim, nama)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # jika queue tidak kosong, maka data baru diletakkan setelah rear, kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada Mahasiswa yang dilayani")
            return None
        # lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front 

        #geser pointer front ke next front
        self.front = self.front.next

        # jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        
        return node_dilayani
    
    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

# program utama

def main():
    #instiantiasi queue
    q = queueAkademik()

    while True:
        print("====== Sistem Antrian Akademik ======")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4):").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa Dilayani: {dilayani.nim} - {dilayani.nama}")
        
        elif pilihan == "3":
            q.tampilkan()
        
        elif pilihan == "4":
            print("Program Selesai. Terimakasih")
            break
        
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()

