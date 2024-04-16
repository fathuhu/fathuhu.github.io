import requests
import json
import datetime
from bs4 import BeautifulSoup

# request to the website
page = requests.get('https://www.republika.co.id/')

# Extract the content to object beautiful soup
obj = BeautifulSoup(page.text, 'html.parser')

# Mendapatkan waktu saat ini
waktu_sekarang = datetime.datetime.now()

# Format waktu sesuai keinginan (misalnya, YYYY-MM-DD HH:MM:SS)
format_waktu = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")

# Baca data yang sudah ada dari file JSON
try:
    with open("headline.json", "r") as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = []

data = []


for headline in obj.find_all('div', class_='col-md-9'):
    judul = headline.find('h3').text
    kd = headline.find('div', class_='date').text.lstrip().strip()
    kdStrip = kd.split("-")
    kategori = kdStrip[0]
    tanggal = kdStrip[1]
    data.append({
        "judul": judul,
        "kategori": kategori,
        "tanggal": tanggal,
        "waktuScrape": format_waktu
    })

# Tambahkan data baru ke dalam data yang sudah ada
existing_data.extend(data)

# Tulis kembali data ke dalam file JSON tanpa menghapus yang sudah ada
with open("headline.json", "w") as f:
    json.dump(existing_data, f, indent=2)