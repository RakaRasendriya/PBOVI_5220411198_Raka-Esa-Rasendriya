class Pakaian:
    def __init__(self, nama, umur, jenis_kelamin):
        self.nama = nama
        self._umur = umur
        self.__jenis_kelamin = jenis_kelamin

    def display_info(self):
        print(f"\nInformasi Pengguna:")
        print(f"Nama            : {self.nama}")
        print(f"Umur            : {self._umur} tahun")
        print(f"Jenis Kelamin   : {self.__jenis_kelamin}")

class Laki(Pakaian):
    casual = {
        'atasan': ['T-shirt ', 'Sweater', 'Hoodie'],
        'bawahan': ['Jeans', 'Chino shorts', 'Joggers'],
        'alas_kaki': ['Shoes', 'Sneakers', 'Sandals']
    }

    formal = {
        'atasan': ['Suit Jacket', 'Tuxedo shirt', 'Polo shirt'],
        'bawahan': ['Suit trousers', 'Chinos', 'Tuxedo pants'],
        'alas_kaki': ['Oxford shoes', 'Loafers', 'Brogues']
    }

    def __init__(self, nama, umur):
        super().__init__(nama, umur, "Laki-laki")
        self.top = None
        self.bottom = None
        self.alas_kaki = None
        self.tipe_pakaian = None

    def show_menu(self, kategori, clothes):
        print(f"Pilihan {kategori}:")
        for idx, item in enumerate(clothes[kategori], start=1):
            print(f"{idx}. {item}")
        choice = int(input(f"Pilih nomor {kategori}: "))
        return clothes[kategori][choice - 1]

    def pilih_pakaian(self, kategori, clothes):
        print(f"\nMemilih Pakaian untuk {self.nama} ({kategori}):")
        selected_item = self.show_menu(kategori, clothes)
        return selected_item

    def set_tipe_pakaian(self, tipe):
        print(f"\nMemilih Tipe Pakaian {tipe} untuk {self.nama}:")
        if tipe == 'casual':
            self.top = self.pilih_pakaian('atasan', self.casual)
            self.bottom = self.pilih_pakaian('bawahan', self.casual)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.casual)
        elif tipe == 'formal':
            self.top = self.pilih_pakaian('atasan', self.formal)
            self.bottom = self.pilih_pakaian('bawahan', self.formal)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.formal)
        self.tipe_pakaian = tipe

    def display_pakaianL(self):
        super().display_info()
        print(f"\nDetail Pakaian untuk {self.nama}:")
        print(f"Tipe Pakaian    : {self.tipe_pakaian if self.tipe_pakaian else 'Belum dipilih'}")
        print(f"Atasan          : {self.top if self.top else 'Belum dipilih'}")
        print(f"Bawahan         : {self.bottom if self.bottom else 'Belum dipilih'}")
        print(f"Alas Kaki       : {self.alas_kaki if self.alas_kaki else 'Belum dipilih'}")


class Perempuan(Pakaian):
    casual = {
        'dalam': ['Blouse', 'Sweater', 'T-Shirt'],
        'luar': ['Vest', 'Cardigan', 'Denim Jacket'],
        'bawahan': ['Skirt', 'Pants', 'Shorts'],
        'alas_kaki': ['Shoes', 'Sneakers', 'Sandals']
    }

    formal = {
        'dalam': ['Dress shirt', 'Blouse', 'Kemeja Putih'],
        'luar': ['Long Cardigan', 'Blazer', 'Vest'],
        'bawahan': ['Dress pants', 'Pencil skirt', 'Trousers'],
        'alas_kaki': ['Heels', 'Pumps', 'Slingbacks']
    }

    def __init__(self, nama, umur):
        super().__init__(nama, umur, "Perempuan")
        self.inner = None
        self.outer = None
        self.bottom = None
        self.alas_kaki = None
        self.tipe_pakaian = None

    def show_menu(self, kategori, clothes):
        print(f"Pilihan {kategori}:")
        for idx, item in enumerate(clothes[kategori], start=1):
            print(f"{idx}. {item}")
        choice = int(input(f"Pilih nomor {kategori}: "))
        return clothes[kategori][choice - 1]

    def pilih_pakaian(self, kategori, clothes):
        print(f"\nMemilih Pakaian untuk {self.nama} ({kategori}):")
        selected_item = self.show_menu(kategori, clothes)
        return selected_item

    def set_tipe_pakaian(self, tipe):
        print(f"\nMemilih Tipe Pakaian {tipe} untuk {self.nama}:")
        if tipe == 'casual':
            self.inner = self.pilih_pakaian('dalam', self.casual)
            self.outer = self.pilih_pakaian('luar', self.casual)
            self.bottom = self.pilih_pakaian('bawahan', self.casual)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.casual)
        elif tipe == 'formal':
            self.inner = self.pilih_pakaian('dalam', self.formal)
            self.outer = self.pilih_pakaian('luar', self.formal)
            self.bottom = self.pilih_pakaian('bawahan', self.formal)
            self.alas_kaki = self.pilih_pakaian('alas_kaki', self.formal)
        self.tipe_pakaian = tipe

    def display_pakaianP(self):
        super().display_info()
        print(f"\nDetail Pakaian untuk {self.nama}:")
        print(f"Tipe Pakaian    : {self.tipe_pakaian if self.tipe_pakaian else 'Belum dipilih'}")
        print(f"Inner           : {self.inner if self.inner else 'Belum dipilih'}")
        print(f"Outer           : {self.outer if self.outer else 'Belum dipilih'}")
        print(f"Bawahan         : {self.bottom if self.bottom else 'Belum dipilih'}")
        print(f"Alas Kaki       : {self.alas_kaki if self.alas_kaki else 'Belum dipilih'}")


class Tampilan(Perempuan):
    pilihan = {
        'aksesoris': ['Anting', 'Kalung', 'Gelang', 'Cincin'],
        'makeup': ['Base', 'Eye', 'Lip', 'Cheek', 'Brow', 'Setting Spray', 'Body', 'Mineral', 'Skincare-Infused']
    }

    def __init__(self, nama, umur):
        super().__init__(nama, umur)
        self.aksesoris = []
        self.makeup = []

    def tambah_aksesoris(self):
        print("\nMemilih Aksesoris:")
        selected_tampilan = self.show_menu('aksesoris', self.pilihan)

        if selected_tampilan not in self.aksesoris:
            self.aksesoris.append(selected_tampilan)
            print(f"Aksesoris {selected_tampilan} berhasil ditambahkan.")
        else:
            print(f"Aksesoris {selected_tampilan} sudah ada dalam daftar.")

    def tambah_makeup(self):
        print("\nMemilih Make Up:")
        selected_tampilan = self.show_menu('makeup', self.pilihan)

        if selected_tampilan not in self.makeup:
            self.makeup.append(selected_tampilan)
            print(f"Make Up {selected_tampilan} berhasil ditambahkan.")
        else:
            print(f"Make Up {selected_tampilan} sudah ada dalam daftar.")

    def display_tampilan(self):
        super().display_pakaianP()
        print(f"Make Up         : {', '.join(self.makeup) if self.makeup else 'Belum dipilih'}")
        print(f"Aksesoris       : {', '.join(self.aksesoris) if self.aksesoris else 'Belum dipilih'}")


# Program Utama
list_pengguna = []

import os

def tampil():
    while True:
        os.system("cls")
        print("\n==============================")
        print("Menu Utama :")
        print("1. Tambah Pengguna")
        print("2. List Pengguna")
        print("3. Keluar")
        choice_menu = input("\nPilih Menu : ")

        if choice_menu == "1":
            while True:
                nama = input("\nMasukkan Nama Pengguna: ")
                umur = int(input("Masukkan Umur Pengguna: "))
                jenis_kelamin = input("Masukkan Jenis Kelamin Pengguna (L/P): ")

                if jenis_kelamin.upper() in ['L', 'P']:
                    break
                else:
                    print("Jenis kelamin tidak valid. Silahkan isi ulang data diri Anda.")
                os.system("pause")

            if jenis_kelamin.upper() == 'L':
                pengguna = Laki(nama, umur)
                list_pengguna.append(pengguna)
            elif jenis_kelamin.upper() == 'P':
                pengguna = Tampilan(nama, umur)
                list_pengguna.append(pengguna)

        elif choice_menu == "2":
            print("\n==============================")
            print("\nList Pengguna:")
            for idx, pengguna in enumerate(list_pengguna, start=1):
                print(f"{idx}. {pengguna.nama} ({pengguna._Pakaian__jenis_kelamin})")

            while True:
                choice_detail = input("\nPilih nomor pengguna untuk melihat detail (0 untuk kembali): ")
                if choice_detail.isdigit():
                    choice_detail = int(choice_detail)
                    if 0 < choice_detail <= len(list_pengguna):
                        pengguna_terpilih = list_pengguna[choice_detail - 1]

                        if isinstance(pengguna_terpilih, Laki):
                            while True:
                                os.system("cls")
                                print("\n==============================")
                                print("\nPilihan Tipe Pakaian:")
                                print("1. Casual")
                                print("2. Formal")
                                print("3. Tampilkan Data Diri dan Pakaian")
                                print("0. Kembali")
                                choice_tipe_pakaian = input("\nPilih Tipe Pakaian (0-3): ")

                                if choice_tipe_pakaian == "1":
                                    pengguna_terpilih.set_tipe_pakaian('casual')
                                elif choice_tipe_pakaian == "2":
                                    pengguna_terpilih.set_tipe_pakaian('formal')
                                elif choice_tipe_pakaian == "3":
                                    pengguna_terpilih.display_pakaianL()
                                elif choice_tipe_pakaian == "0":
                                    tampil()
                                else:
                                    print("Pilihan tidak valid. Silakan pilih antara 0-3.")
                                os.system("pause")

                        elif isinstance(pengguna_terpilih, Tampilan):
                            while True:
                                os.system("cls")
                                print("\n==============================")
                                print("\nPilihan Tipe Pakaian:")
                                print("1. Casual")
                                print("2. Formal")
                                print("3. Tambah Make Up")
                                print("4. Tambah Aksesoris")
                                print("5. Tampilkan Data Diri dan Pakaian")
                                print("0. Kembali")
                                choice_tipe_pakaian = input("\nPilih Tipe Pakaian (0-5): ")

                                if choice_tipe_pakaian == "1":
                                    pengguna_terpilih.set_tipe_pakaian('casual')
                                elif choice_tipe_pakaian == "2":
                                    pengguna_terpilih.set_tipe_pakaian('formal')
                                elif choice_tipe_pakaian == "3":
                                    pengguna_terpilih.tambah_makeup()
                                elif choice_tipe_pakaian == "4":
                                    pengguna_terpilih.tambah_aksesoris()
                                elif choice_tipe_pakaian == "5":
                                    pengguna_terpilih.display_tampilan()
                                elif choice_tipe_pakaian == "0":
                                    tampil()
                                else:
                                    print("Pilihan tidak valid. Silakan pilih antara 0-5.")
                                os.system("pause")
                    elif choice_detail == 0:
                        break
                    else:
                        print("Nomor pengguna tidak valid.")
                    os.system("pause")
                else:
                    print("Masukkan angka yang valid.")
                os.system("pause")

        elif choice_menu == "3":
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 10-3.")
        os.system("pause")

tampil()
print("berhasil ditambahkan")