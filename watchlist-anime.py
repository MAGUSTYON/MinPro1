watchlist = ["naruto", "black clover", "kny", "jjk", "horimiya"]
ditonton = []

while True:
    print("MENU")
    print("1. Tambah anime ke watchlist")
    print("2. Lihat watchlist")
    print("3. Tandai anime sudah ditonton + beri rating")
    print("4. Lihat daftar anime yang sudah ditonton")
    print("5. Ubah rating anime yang sudah ditonton")
    print("6. Hapus anime dari watchlist")
    print("7. Keluar")
    menu = input("Pilih menu (1-7): ")

    if menu == "1":
        while True:
            print("Ketik 'selesai' kalau sudah tidak ingin memasukkan watchlist lagi.")
            judul = input("masukkan judul anime: ")
            if judul == "selesai":
                break
            elif judul in ditonton:
                print("anime sudah di tonton")
            elif judul in watchlist:
                print("anime sudah ada di watchlist")
            else:
                watchlist.append(judul)
                print("anime di tambahkan ke watchlist")

    elif menu == "2":
        print("daftar watchlist")
        print(watchlist)

    elif menu == "3":
        while True:
            print("daftar Watchlist:")
            print(watchlist)
            print("Ketik 'selesai' kalau sudah selesai.")
            anime = input("Masukkan judul anime yang sudah ditonton: ")
            if anime == "selesai":
                break
            elif anime in watchlist:
                while True:
                    rating_input = input("Masukkan rating (0-10): ")
                    if not rating_input.isdigit():
                        print("Rating harus berupa angka.")
                        continue
                    else:
                        rating = int(rating_input)
                        if rating < 0 or rating > 10:
                            print("Rating harus antara 0 - 10.")
                        else:
                            watchlist.remove(anime)
                            ditonton.append([anime, rating])
                            print(anime, "dipindahkan ke daftar sudah ditonton dengan rating", rating)
                            break
            else:
                print(anime, "tidak ada di watchlist.")

    elif menu == "4":
        print("Daftar anime yang sudah ditonton:")
        print(ditonton)

    elif menu == "5":
        if not ditonton:
            print("Belum ada anime yang selesai ditonton.")
        else:
            while True:
                print("Daftar anime yang sudah ditonton:", ditonton)
                print("Ketik 'selesai' kalau sudah selesai.")
                ubah = input("Masukkan judul anime yang ingin diubah ratingnya: ")
                if ubah == "selesai":
                    break
                for anime in ditonton:
                    if anime[0] == ubah:
                        while True:
                            rating_baru = input("Masukkan rating baru untuk " + ubah + " (0-10): ")
                            if not rating_baru.isdigit():
                                print("Rating harus berupa angka.")
                                continue
                            rating = int(rating_baru)
                            if rating < 0 or rating > 10:
                                print("Rating harus antara 0 - 10.")
                            else:
                                anime[1] = rating
                                print("Rating", ubah, "berhasil diubah menjadi", rating)
                                break
                        break
                else:
                    print(ubah, "tidak ada di daftar yang sudah ditonton.")

    elif menu == "6":
            while True:
                print("daftar Watchlist:")
                print(watchlist)
                print("Ketik 'selesai' kalau sudah tidak ingin memasukkan watchlist lagi.")
                hapus = input("Masukkan judul anime yang ingin dihapus dari watchlist: ")
                if hapus == "selesai":
                    break
                elif hapus in watchlist:
                    watchlist.remove(hapus)
                    print(hapus, "berhasil dihapus dari watchlist.")
                else:
                    print(hapus, "tidak ditemukan di watchlist.")    

    elif menu == "7":
        print("exit")
        break
    else:
        print("Pilihan tidak ada, input lagi.")
