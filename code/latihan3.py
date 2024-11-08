def atm():
    saldo = 1_000_000  # Saldo awal pengguna

    while True:
        # Menampilkan menu pilihan
        print("\n==== Menu ATM ====")
        print("1. Cek Saldo")
        print("2. Tarik Uang")
        print("3. Keluar")
        
        # Meminta input dari pengguna
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            # Menampilkan saldo
            print(f"Saldo Anda saat ini adalah: Rp{saldo:,.2f}")
        
        elif pilihan == '2':
            # Menarik uang
            jumlah_tarik = int(input("Masukkan jumlah uang yang ingin ditarik: Rp"))
            
            # Mengecek apakah saldo cukup
            if jumlah_tarik > saldo:
                print("Saldo tidak cukup untuk menarik uang sebesar itu.")
            else:
                saldo -= jumlah_tarik
                print(f"Uang Rp{jumlah_tarik:,.2f} berhasil ditarik.")
                print(f"Sisa saldo Anda adalah: Rp{saldo:,.2f}")
        
        elif pilihan == '3':
            # Keluar dari program
            print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Menjalankan mesin ATM
atm()
