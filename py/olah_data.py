import csv
import json
from statistics import mean

daftar_provinsi = {
    'Aceh (NAD)': [
        'Aceh Barat', 'Aceh Barat Daya', 'Aceh Besar', 'Aceh Jaya', 'Aceh Selatan',
        'Aceh Singkil', 'Aceh Tamiang', 'Aceh Tengah', 'Aceh Tenggara', 'Aceh Timur',
        'Aceh Utara', 'Bener Meriah', 'Bireuen', 'Gayo Lues', 'Banda Aceh',
        'Langsa', 'Lhokseumawe', 'Sabang', 'Subulussalam', 'Nagan Raya',
        'Pidie', 'Pidie Jaya', 'Simeulue'
    ],
    'Sumatera Utara': [
        'Asahan', 'Batu Bara', 'Dairi', 'Deli Serdang', 'Karo', 'Labuhan Batu',
        'Labuhan Batu Selatan', 'Labuhan Batu Utara', 'Langkat', 'Mandailing Natal',
        'Nias', 'Nias Barat', 'Nias Selatan', 'Nias Utara', 'Padang Lawas',
        'Padang Lawas Utara', 'Pakpak Bharat', 'Samosir', 'Serdang Bedagai',
        'Simalungun', 'Tapanuli Selatan', 'Tapanuli Tengah', 'Tapanuli Utara',
        'Toba Samosir', 'Binjai', 'Gunungsitoli', 'Medan', 'Padangsidempuan',
        'Pematang Siantar', 'Sibolga', 'Tanjung Balai', 'Tebing Tinggi'
    ],
    'Sumatera Barat': [
        'Agam', 'Dharmasraya', 'Kepulauan Mentawai', 'Lima Puluh Kota', 'Padang Pariaman',
        'Pasaman', 'Pasaman Barat', 'Pesisir Selatan', 'Solok', 'Solok Selatan',
        'Tanah Datar', 'Bukittinggi', 'Padang', 'Padang Panjang', 'Pariaman',
        'Payakumbuh', 'Sawahlunto', 'Solok'
    ],
    'Riau': [
        'Bengkalis', 'Indragiri Hilir', 'Indragiri Hulu', 'Kampar', 'Kepulauan Meranti',
        'Kuantan Singingi', 'Pelalawan', 'Rokan Hilir', 'Rokan Hulu', 'Siak',
        'Dumai', 'Pekanbaru'
    ],
    'Jambi': [
        'Batang Hari', 'Bungo', 'Kerinci', 'Merangin', 'Muaro Jambi',
        'Sarolangun', 'Tanjung Jabung Barat', 'Tanjung Jabung Timur', 'Tebo',
        'Jambi', 'Sungai Penuh'
    ],
    'Sumatera Selatan': [
        'Banyuasin', 'Empat Lawang', 'Lahat', 'Muara Enim', 'Musi Banyuasin',
        'Musi Rawas', 'Ogan Ilir', 'Ogan Komering Ilir', 'Ogan Komering Ulu',
        'Ogan Komering Ulu Selatan', 'Ogan Komering Ulu Timur', 'Penukal Abab Lematang Ilir',
        'Lubuk Linggau', 'Pagar Alam', 'Palembang', 'Prabumulih'
    ],
    'Bengkulu': [
        'Bengkulu Selatan', 'Bengkulu Tengah', 'Bengkulu Utara', 'Kaur', 'Kepahiang',
        'Lebong', 'Mukomuko', 'Rejang Lebong', 'Seluma', 'Bengkulu'
    ],
    'Lampung': [
        'Lampung Barat', 'Lampung Selatan', 'Lampung Tengah', 'Lampung Timur',
        'Lampung Utara', 'Mesuji', 'Pesawaran', 'Pesisir Barat', 'Pringsewu',
        'Tanggamus', 'Tulang Bawang', 'Tulang Bawang Barat', 'Way Kanan', 'Bandar Lampung',
        'Metro'
    ],
    'Kepulauan Bangka Belitung': [
        'Bangka', 'Bangka Barat', 'Bangka Selatan', 'Bangka Tengah', 'Belitung',
        'Belitung Timur', 'Pangkal Pinang'
    ],
    'Kepulauan Riau': [
        'Bintan', 'Karimun', 'Kepulauan Anambas', 'Lingga', 'Natuna',
        'Batam', 'Tanjung Pinang'
    ],
    'Banten': [
        'Lebak', 'Pandeglang', 'Serang', 'Tangerang', 'Cilegon', 'Serang', 'Tangerang Selatan'
    ],
    'DKI Jakarta': [
        'Kepulauan Seribu', 'Jakarta Barat', 'Jakarta Pusat', 'Jakarta Selatan',
        'Jakarta Timur', 'Jakarta Utara'
    ],
    'Jawa Barat': [
        'Bandung', 'Bandung Barat', 'Bekasi', 'Bogor', 'Ciamis', 'Cianjur',
        'Cirebon', 'Garut', 'Indramayu', 'Karawang', 'Kuningan', 'Majalengka',
        'Purwakarta', 'Subang', 'Sukabumi', 'Sumedang', 'Tasikmalaya', 'Bandung',
        'Banjar', 'Bekasi', 'Bogor', 'Cirebon', 'Cimahi', 'Depok',
        'Sukabumi', 'Tasikmalaya'
    ],
    'Jawa Tengah': [
        'Banjarnegara', 'Banyumas', 'Batang', 'Blora', 'Boyolali', 'Brebes',
        'Cilacap', 'Demak', 'Grobogan', 'Jepara', 'Karanganyar', 'Kebumen',
        'Kendal', 'Klaten', 'Kudus', 'Magelang', 'Pati', 'Pekalongan',
        'Pemalang', 'Purbalingga', 'Purworejo', 'Rembang', 'Semarang',
        'Sragen', 'Sukoharjo', 'Tegal', 'Temanggung', 'Wonogiri', 'Wonosobo',
        'Magelang', 'Pekalongan', 'Salatiga', 'Semarang', 'Surakarta', 'Tegal'
    ],
    'DI Yogyakarta': [
        'Bantul', 'Gunung Kidul', 'Kulon Progo', 'Sleman', 'Yogyakarta'
    ],
    'Jawa Timur': [
        'Bangkalan', 'Banyuwangi', 'Blitar', 'Bojonegoro', 'Bondowoso', 'Gresik',
        'Jember', 'Jombang', 'Kediri', 'Lamongan', 'Lumajang', 'Madiun',
        'Magetan', 'Malang', 'Mojokerto', 'Nganjuk', 'Ngawi', 'Pacitan',
        'Pamekasan', 'Pasuruan', 'Ponorogo', 'Probolinggo', 'Sampang',
        'Sidoarjo', 'Situbondo', 'Sumenep', 'Trenggalek', 'Tuban', 'Tulungagung',
        'Batu', 'Blitar', 'Kediri', 'Madiun', 'Malang', 'Mojokerto',
        'Pasuruan', 'Probolinggo', 'Surabaya'
    ],
    'Bali': [
        'Badung', 'Bangli', 'Buleleng', 'Gianyar', 'Jembrana', 'Karangasem',
        'Klungkung', 'Tabanan', 'Denpasar'
    ],
    'Nusa Tenggara Barat (NTB)': [
        'Bima', 'Dompu', 'Lombok Barat', 'Lombok Tengah', 'Lombok Timur',
        'Lombok Utara', 'Sumbawa', 'Sumbawa Barat', 'Bima', 'Mataram'
    ],
    'Nusa Tenggara Timur (NTT)': [
        'Alor', 'Belu', 'Ende', 'Flores Timur', 'Kupang', 'Lembata', 'Malaka',
        'Manggarai', 'Manggarai Barat', 'Manggarai Timur', 'Ngada', 'Nagekeo', 'Rote Ndao',
        'Sabu Raijua', 'Sikka', 'Sumba Barat', 'Sumba Barat Daya', 'Sumba Tengah',
        'Sumba Timur', 'Timor Tengah Selatan', 'Timor Tengah Utara', 'Kupang'
    ],
    'Kalimantan Barat': [
        'Bengkayang', 'Kapuas Hulu', 'Kayong Utara', 'Ketapang', 'Kubu Raya',
        'Landak', 'Melawi', 'Mempawah', 'Sambas', 'Sanggau', 'Sekadau',
        'Sintang', 'Pontianak', 'Singkawang'
    ],
    'Kalimantan Tengah': [
        'Barito Selatan', 'Barito Timur', 'Barito Utara', 'Gunung Mas', 'Kapuas',
        'Katingan', 'Kotawaringin Barat', 'Kotawaringin Timur', 'Lamandau', 'Murung Raya',
        'Pulang Pisau', 'Sukamara', 'Seruyan', 'Palangka Raya'
    ],
    'Kalimantan Selatan': [
        'Balangan', 'Banjar', 'Barito Kuala', 'Hulu Sungai Selatan', 'Hulu Sungai Tengah',
        'Hulu Sungai Utara', 'Kotabaru', 'Tabalong', 'Tanah Bumbu', 'Tanah Laut',
        'Tapin', 'Banjarbaru', 'Banjarmasin'
    ],
    'Kalimantan Timur': [
        'Berau', 'Kutai Barat', 'Kutai Kartanegara', 'Kutai Timur', 'Mahakam Ulu',
        'Paser', 'Penajam Paser Utara', 'Balikpapan', 'Bontang', 'Samarinda'
    ],
    'Kalimantan Utara': [
        'Bulungan', 'Malinau', 'Nunukan', 'Tana Tidung', 'Tarakan'
    ],
    'Sulawesi Utara': [
        'Bolaang Mongondow', 'Bolaang Mongondow Selatan', 'Bolaang Mongondow Timur',
        'Bolaang Mongondow Utara', 'Kepulauan Sangihe', 'Kepulauan Siau Tagulandang Biaro (Sitaro)',
        'Kepulauan Talaud', 'Minahasa', 'Minahasa Selatan', 'Minahasa Tenggara',
        'Minahasa Utara', 'Bitung', 'Kotamobagu', 'Manado', 'Tomohon'
    ],
    'Sulawesi Tengah': [
        'Banggai', 'Banggai Kepulauan', 'Banggai Laut', 'Buol', 'Donggala',
        'Morowali', 'Morowali Utara', 'Parigi Moutong', 'Poso', 'Sigi',
        'Tojo Una-Una', 'Tolitoli', 'Palu'
    ],
    'Sulawesi Selatan': [
        'Bantaeng', 'Barru', 'Bone', 'Bulukumba', 'Enrekang', 'Gowa',
        'Jeneponto', 'Kepulauan Selayar', 'Luwu', 'Luwu Timur', 'Luwu Utara',
        'Maros', 'Pangkajene Kepulauan', 'Pinrang', 'Sidenreng Rappang', 'Sinjai',
        'Soppeng', 'Takalar', 'Tana Toraja', 'Toraja Utara', 'Wajo', 'Makassar',
        'Palopo', 'Parepare'
    ],
    'Sulawesi Tenggara': [
        'Bombana', 'Buton', 'Buton Selatan', 'Buton Tengah', 'Buton Utara',
        'Kolaka', 'Kolaka Timur', 'Kolaka Utara', 'Konawe', 'Konawe Kepulauan',
        'Konawe Selatan', 'Konawe Utara', 'Muna', 'Muna Barat', 'Wakatobi', 'Bau-Bau',
        'Kendari'
    ],
    'Gorontalo': [
        'Boalemo', 'Bone Bolango', 'Gorontalo', 'Gorontalo Utara', 'Pohuwato', 'Gorontalo'
    ],
    'Sulawesi Barat': [
        'Majene', 'Mamasa', 'Mamuju', 'Mamuju Tengah', 'Pasangkayu', 'Polewali Mandar'
    ],
    'Maluku': [
        'Buru', 'Buru Selatan', 'Kepulauan Aru', 'Maluku Barat Daya', 'Maluku Tengah',
        'Maluku Tenggara', 'Maluku Tenggara Barat', 'Seram Bagian Barat', 'Seram Bagian Timur',
        'Ambon', 'Tual'
    ],
    'Maluku Utara': [
        'Halmahera Barat', 'Halmahera Tengah', 'Halmahera Timur', 'Halmahera Selatan',
        'Halmahera Utara', 'Kepulauan Sula', 'Pulau Morotai', 'Pulau Taliabu', 'Ternate', 'Tidore Kepulauan'
    ],
    'Papua': [
        'Asmat', 'Biak Numfor', 'Boven Digoel', 'Deiyai', 'Dogiyai', 'Intan Jaya',
        'Jayapura', 'Jayawijaya', 'Keerom', 'Lanny Jaya', 'Mamberamo Raya',
        'Mamberamo Tengah', 'Mappi', 'Merauke', 'Mimika', 'Nabire', 'Nduga',
        'Paniai', 'Pegunungan Bintang', 'Puncak', 'Puncak Jaya', 'Sarmi',
        'Supiori', 'Tolikara', 'Waropen', 'Yahukimo', 'Yalimo', 'Jayapura'
    ],
    'Papua Barat': [
        'Fakfak', 'Kaimana', 'Manokwari', 'Manokwari Selatan', 'Maybrat', 'Pegunungan Arfak',
        'Raja Ampat', 'Sorong', 'Sorong Selatan', 'Tambrauw', 'Teluk Bintuni', 'Teluk Wondama',
        'Sorong'
    ]
}

def olah_adv_stok_prov():
    # # Membaca file JSON
    with open('.\\json\\advan_cleaned.json', 'r') as file:
        data = json.load(file)

    # Inisialisasi dictionary untuk menyimpan stok berdasarkan provinsi
    stok_provinsi = {}
    harga_provinsi = {}
    avg_rate_prov = {}
    jual_prov = {}

    # print('Data stok advan per provinsi berhasil disimpan ke file stok_provinsi.json')
    for item in data:
        # Mengambil stok, harga, rate, dan lokasi (kota/kabupaten)
        stok = item.get('Stok', 0)
        temp_lok = item.get('Lokasi', '')
        harga = item.get('Harga', 0)
        rate_prov = item.get('average_rate', 0)
        jual = item.get('Terjual', 0)

        if "Kab. " in temp_lok or "Kota " in temp_lok:
            lokasi = temp_lok[temp_lok.find('. ')+2:]
        else:
            lokasi = item.get('Lokasi', '')

        # Mencari provinsi berdasarkan lokasi
        for provinsi_nama, kota_kabupaten in daftar_provinsi.items():
            if lokasi in kota_kabupaten:
                # Menjumlahkan stok dan menambahkan harga untuk provinsi ini
                if provinsi_nama in stok_provinsi:
                    stok_provinsi[provinsi_nama] += stok
                    harga_provinsi[provinsi_nama].append(harga)
                    jual_prov[provinsi_nama] += jual
                    if rate_prov != None:
                        try:
                            avg_rate_prov[provinsi_nama].append(rate_prov)
                        except:
                            avg_rate_prov[provinsi_nama] = [rate_prov]    
                else:
                    stok_provinsi[provinsi_nama] = stok
                    harga_provinsi[provinsi_nama] = [harga]
                    jual_prov[provinsi_nama] = jual
                    if rate_prov != None:
                        avg_rate_prov[provinsi_nama] = [rate_prov]
                break
        else:
            # Jika lokasi tidak ditemukan dalam daftar provinsi
            stok_provinsi['Tidak Diketahui'] = stok_provinsi.get('Tidak Diketahui', 0) + stok
            
            harga_provinsi['Tidak Diketahui'] = harga_provinsi.get('Tidak Diketahui', [])
            harga_provinsi['Tidak Diketahui'].append(harga)
            
            avg_rate_prov['Tidak Diketahui'] = avg_rate_prov.get('Tidak Diketahui', [])
            avg_rate_prov['Tidak Diketahui'].append(avg_rate_prov)
            
            jual_prov['Tidak Diketahui'] = jual_prov.get('Tidak Diketahui', 0) + jual
            print(lokasi)  # mengecek kota mana yang tidak terdapat di variable provinsi

    # Membuat list dari stok_provinsi dan menghitung rata-rata harga menggunakan mean
    data_provinsi = []
    for provinsi, stok in stok_provinsi.items():
        harga_list = harga_provinsi.get(provinsi, [])
        rate_list = avg_rate_prov.get(provinsi, [])
        rata_rata_harga = mean(harga_list) if harga_list else 0
        rata_rate = mean(rate_list) if rate_list else 0
        terjual = jual_prov.get(provinsi, 0)
        
        data_provinsi.append({
            'provinsi': provinsi,
            'stok': stok,
            'rata_rata_harga': rata_rata_harga,
            'rata_rata_rate': rata_rate,
            'terjual': terjual
        })

    # Menyimpan data ke file JSON baru
    with open('.\\json\\provinsi_advan.json', 'w') as file:
        json.dump(data_provinsi, file, indent=4)

    print('Data stok dan rata-rata harga advan per provinsi berhasil disimpan ke file stok_harga_provinsi_advan.json')

def olah_ax_stok_prov():
    # # Membaca file JSON
    with open('.\\json\\axioo_cleaned.json', 'r') as file:
        data = json.load(file)

    # Inisialisasi dictionary untuk menyimpan stok berdasarkan provinsi
    stok_provinsi = {}
    harga_provinsi = {}
    avg_rate_prov = {}
    jual_prov = {}

    # print('Data stok advan per provinsi berhasil disimpan ke file stok_provinsi.json')
    for item in data:
        # Mengambil stok, harga, rate, dan lokasi (kota/kabupaten)
        stok = item.get('Stok', 0)
        temp_lok = item.get('Lokasi', '')
        harga = item.get('Harga', 0)
        rate_prov = item.get('average_rate', 0)
        jual = item.get('Terjual', 0)

        if "Kab. " in temp_lok or "Kota " in temp_lok:
            lokasi = temp_lok[temp_lok.find('. ')+2:]
        else:
            lokasi = item.get('Lokasi', '')

        # Mencari provinsi berdasarkan lokasi
        for provinsi_nama, kota_kabupaten in daftar_provinsi.items():
            if lokasi in kota_kabupaten:
                # Menjumlahkan stok dan menambahkan harga untuk provinsi ini
                if provinsi_nama in stok_provinsi:
                    stok_provinsi[provinsi_nama] += stok
                    harga_provinsi[provinsi_nama].append(harga)
                    jual_prov[provinsi_nama] += jual
                    if rate_prov != None:
                        try:
                            avg_rate_prov[provinsi_nama].append(rate_prov)
                        except:
                            avg_rate_prov[provinsi_nama] = [rate_prov]    
                else:
                    stok_provinsi[provinsi_nama] = stok
                    harga_provinsi[provinsi_nama] = [harga]
                    jual_prov[provinsi_nama] = jual
                    if rate_prov != None:
                        avg_rate_prov[provinsi_nama] = [rate_prov]
                break
        else:
            # Jika lokasi tidak ditemukan dalam daftar provinsi
            stok_provinsi['Tidak Diketahui'] = stok_provinsi.get('Tidak Diketahui', 0) + stok
            
            harga_provinsi['Tidak Diketahui'] = harga_provinsi.get('Tidak Diketahui', [])
            harga_provinsi['Tidak Diketahui'].append(harga)
            
            avg_rate_prov['Tidak Diketahui'] = avg_rate_prov.get('Tidak Diketahui', [])
            avg_rate_prov['Tidak Diketahui'].append(avg_rate_prov)
            
            jual_prov['Tidak Diketahui'] = jual_prov.get('Tidak Diketahui', 0) + jual
            print(lokasi)  # mengecek kota mana yang tidak terdapat di variable provinsi

    # Membuat list dari stok_provinsi dan menghitung rata-rata harga menggunakan mean
    data_provinsi = []
    for provinsi, stok in stok_provinsi.items():
        harga_list = harga_provinsi.get(provinsi, [])
        rate_list = avg_rate_prov.get(provinsi, [])
        rata_rata_harga = mean(harga_list) if harga_list else 0
        rata_rate = mean(rate_list) if rate_list else 0
        terjual = jual_prov.get(provinsi, 0)
        
        data_provinsi.append({
            'provinsi': provinsi,
            'stok': stok,
            'rata_rata_harga': rata_rata_harga,
            'rata_rata_rate': rata_rate,
            'terjual': terjual
        })

    # Menyimpan data ke file JSON baru
    with open('.\\json\\provinsi_axioo.json', 'w') as file:
        json.dump(data_provinsi, file, indent=4)

    print('Data stok dan rata-rata harga advan per provinsi berhasil disimpan ke file stok_harga_provinsi_axioo.json')

# olah_adv_stok_prov()
olah_ax_stok_prov()