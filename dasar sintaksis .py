"""
semua sintaksis dasar bahasa pemrograman terdiri dari:
1. sekuensial : langkah berurutan
2. percabangan : langkah melompat jika kondisi terpenuhi
3. perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# sekuensial
print('ibu berkata, "beli 1 botol susu, dan 6 butir telur"')
print('anak menjawab, "baik"')
print('maka anak berangkat ke toko')
print('dan mulai berbelanja')

# percabangan
jumlah_botol_susu = 55
jumlah_butir_telur = 32
print(f"jumlah susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_butir_telur} butir")
print('anak mengecek harganya, ternyata uangnya cukup')

if jumlah_botol_susu > 0:
    print('anak membeli 1 botol susu')
if jumlah_butir_telur > 0:
    print('anak membeli 6 butir telur')

print('anak kembali ke rumah')
print('anak memberi hasilnya kepada ibu')
