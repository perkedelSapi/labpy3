# Modal awal
modal_awal = 100_000_000  # 100 juta
total_laba = 0  # Inisialisasi total laba

print("Laba per bulan:")

# Menghitung laba per bulan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0  # Bulan pertama dan kedua belum ada laba
    elif bulan == 3 or bulan == 4:
        laba = modal_awal * 0.01  # Bulan ketiga dan keempat laba 1%
    elif bulan == 5 or bulan == 6:
        laba = modal_awal * 0.05  # Bulan kelima dan keenam laba 5%
    elif bulan == 7:
        laba = modal_awal * 0.05  # Bulan ketujuh laba tetap 5%
    elif bulan == 8:
        laba = modal_awal * 0.03  # Bulan kedelapan laba turun menjadi 3%
    
    print(f"Laba bulan ke-{bulan} sebesar: Rp{laba:,.2f}")
    total_laba += laba  # Menambahkan laba bulanan ke total laba

# Menampilkan total laba setelah 8 bulan
print(f"\nTotal laba selama 8 bulan adalah: Rp{total_laba:,.2f}")
