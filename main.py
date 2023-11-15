import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def slug(text):
    slug = text.lower()
    slug = re.sub(r'\s+', '+', slug)
    slug = re.sub(r'[^\w\+]', '', slug)
    return slug

def slug_file(text):
    slug = text.lower()
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'[^\w\-]', '', slug)
    return slug

def get_full_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title.string

def cari_berita(topik, situs, tanggal_awal, tanggal_akhir,num):
    url = f"https://www.google.com/search?q={slug(topik)}+site%3Ahttps%3A%2F%2F{situs}+before%3A{tanggal_akhir}+after%3A{tanggal_awal}&num={num}"
    # Untuk menggunakan browser linux
    # headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"}
    
    # Untuk menggunakan browser windows
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    berita = []
    for hasil in soup.find_all('div', class_='g'):
        link = hasil.find('a')['href']
        judul = get_full_title(link)
        for span in hasil.find_all('span', class_='lhLbod'):
            tanggal = span.find('span').text
        try:
            author = hasil.find('div', class_='slp').text
        except AttributeError:
            author = 'Tidak tersedia'
        berita.append([judul, tanggal, author, link])

    df = pd.DataFrame(berita, columns=['Judul Berita', 'Tanggal', 'Author', 'URL Berita'])
    df.to_excel(f'{slug_file(topik)}_{situs}.xlsx', index=False)
    
    print(f"Hasil pencarian: {soup.find(id='result-stats').text} berita terkait '{topik}' pada website {situs}")
    print(df.head(10))

def Check():
    while True:
        check = input('Jalankan Kembali Program[y/n]: ').lower()
        if check == 'y' :
            return True
        elif check == 'n':
            return False
        else:
            print("Masukkan Ulang")

print("Welcome to Program Pencari Berita by Fyrn")
print("https://github.com/FyrnDly")
program = True
while program:
    try:
        topik = input('Tulis Topik Berita Anda: ')
        site = input('Masukkan url/link Situs Berita(tanpa http:// atau https://): ')
        first_date = input('Masukkan Tanggal Pencarian Awal(YYYY-MM-DD): ')
        end_date = input('Masukkan Tanggal Pencarian Akhir(YYYY-MM-DD): ')
        while True:
            try:
                jumlah_berita = int(input('Masukkan jumlah berita yang ingin diambil: '))
                break
            except:
                print("Masukkan Angka")
        cari_berita(topik, site, first_date, end_date, jumlah_berita)
        program = Check()
    except KeyboardInterrupt:
        break
    
print("\nProgram Berakhir \n-terimakasih by fyrn")
time.sleep(3)