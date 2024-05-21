import csv
import json

provinsi = {
    'Aceh (NAD)': [
        'Aceh Barat',
        'Aceh Barat Daya',
        'Aceh Besar',
        'Aceh Jaya',
        'Aceh Selatan',
        'Aceh Singkil',
        'Aceh Tamiang',
        'Aceh Tengah',
        'Aceh Tenggara',
        'Aceh Timur',
        'Aceh Utara',
        'Bener Meriah',
        'Bireuen',
        'Gayo Lues',
        'Kota Banda Aceh',
        'Kota Langsa',
        'Kota Lhokseumawe',
        'Kota Sabang',
        'Kota Subulussalam',
        'Nagan Raya',
        'Pidie',
        'Pidie Jaya',
        'Simeulue'
    ]
}

# Membaca file JSON
with open('data_advan_workplus_with_stock.json', 'r') as file:
    data = json.load(file)

# Inisialisasi dictionary untuk menyimpan stok berdasarkan provinsi
stok_provinsi = {}

# Iterasi setiap elemen dalam data JSON
for item in data:
    # Mengambil stok dan lokasi (kota/kabupaten)
    stok = item.get('Stok', 0)
    lokasi = item.get('Lokasi', '')

    # Mencari provinsi berdasarkan lokasi
    for provinsi_nama, kota_kabupaten in provinsi.items():
        if lokasi in kota_kabupaten:
            # Menjumlahkan stok untuk provinsi ini
            if provinsi_nama in stok_provinsi:
                stok_provinsi[provinsi_nama] += stok
            else:
                stok_provinsi[provinsi_nama] = stok
            break
    else:
        # Jika lokasi tidak ditemukan dalam daftar provinsi
        stok_provinsi['Tidak Diketahui'] = stok_provinsi.get('Tidak Diketahui', 0) + stok

# Membuat list dari stok_provinsi
data_provinsi = [{'Provinsi': provinsi, 'Stok': stok} for provinsi, stok in stok_provinsi.items()]

# Menyimpan data ke file JSON baru
with open('stok_provinsi.json', 'w') as file:
    json.dump(data_provinsi, file, indent=4)

print('Data stok per provinsi berhasil disimpan ke file stok_provinsi.json')