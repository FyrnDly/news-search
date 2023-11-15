Program Pencarian Berita
===
Program ini bertujuan untuk mencari berita terkait topik tertentu dari situs berita tertentu dalam rentang waktu tertentu. Program ini melakukan scraping data dari SEO Google dan menyimpannya dalam format excel.

## Informasi Program
- Title:  `Pencarian Berita`
- Authors:  [Fyrn](https://github.com/FyrnDly)

## Library Package
- pandas
- requests 
- beautifulsoup4 
- openpyxl

## Cara Menggunakan
- Buat sebuah [virtual environtment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) untuk menginstall semua library package secara virtual atau lewati, jika dilokal
  ```
  python -m venv myenv
  ```
  Pada Windows
  ```
  myenv\Scripts\activate
  ```
  Pada Linux atau MacOS
  ```
  source myenv/bin/activate
  ```
- Install Semua Library yang dibutuhkan
  ```
  pip install requests beautifulsoup4 pandas openpyxl
  ```
  atau
  ```
  pip install -r requirements.txt
  ```
- Jalankan Program
  ```
  python main.py
  ```

## Contoh Hasil
Program ini akan menghasilkan file excel yang berisi judul, tanggal, author, dan url berita yang terkait dengan topik dan situs berita yang dicari. Selain itu, memberikan summary hasil yang didapatkannya juga pada terminal sebagai berikut

```
Welcome to Program Pencari Berita by Fyrn
https://github.com/FyrnDly
Tulis Topik Berita Anda: Covid-19
Masukkan url/link Situs Berita(tanpa http:// atau https://): detik.com
Masukkan jumlah berita yang ingin diambil: 15
```
Hasil pencarian: Sekitar 47 hasil (0,23 detik)  berita terkait 'Covid-19' pada website detik.com
| Judul Berita | Tanggal | Author | URL Berita |
| ------------ | ------- | ------ | ---------- |
Gejala COVID-19 Varian Pirola, Warga Jabar Waj...  | 4 Sep 2023 | Tidak tersedia | https://www.detik.com/jabar/berita/d-6913044/g... |
| 4 Aturan Klaim Biaya Perawatan Pasien COVID-19...  | 8 Sep 2023 | Tidak tersedia | https://www.detik.com/jatim/berita/d-6920227/4... |
| Berita dan Informasi Obat covid 19 Terkini dan...  | 7 Sep 2023 | Tidak tersedia |           https://www.detik.com/tag/obat-covid_19