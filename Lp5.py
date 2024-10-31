print('welcome to the website programmed by ahmad ibnu batutah'.upper())
print('silakan isi jumlah pengunjung yang akan membeli terlebih dahulu'.upper())
jumlah_pengunjung = int(input('\nMasukan jumlah pengunjung: '))
total_harga = 0

for i in range(jumlah_pengunjung):
    umur = int(input(f'Masukan umur pengunjung ke-{i+1}: '))
    if umur <= 2:
        harga = 0
    elif 3 <= umur <= 12:
      harga = 14
    elif umur >= 65:
       harga = 18
    else:
       harga = 23
    total_harga += harga
    print(f'Harga tiket untuk umur {umur} tahun: ${harga}')
print(f'\nTotal harga tiket keseluruhan: ${total_harga}')

while True:
   if total_harga > 0:
      uang = float(input('Masukan jumlah uang yang di bayarkan: $'))
      kurang = total_harga - uang
      if uang < total_harga:
         print(f'Uang yang di bayarkan ${uang:.2f}')
         print(f'Sedangkan harga yang harus di bayar ${total_harga:.2f}')
         print(f'Dan anda kurang ${kurang:.2f}')
         print('\nSilakan mohon untuk coba lagi.')
      else:
         uang >= total_harga
         kembalian = uang - total_harga
         print(f'Silakan uang kembalian anda: ${kembalian:.2f}')
         break
print('\nSelamat berlibur di kebun binatang'.upper())
print('semoga harimu menyenangkan :)'.upper())