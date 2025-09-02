import csv
import os

# Lokasi file input/output
CSV_FILE = "mapping_pages.csv"
PAGES_DIR = "pages"
LOGO_PATH = "../assets/logo.png"
PHOTO_DIR = "../assets/photos"
QRCODE_DIR = "../assets/qrcode"

# Pastikan folder pages ada
os.makedirs(PAGES_DIR, exist_ok=True)

with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nisn = row["NISN"].strip()
        nama = row["Nama lengkap"].strip()
        nik = row["NIK"].strip()
        kelas = row["Kelas"].strip()
        ttl = row["Tempat, Tanggal Lahir"].strip()
        alamat = row["Alamat Rumah"].strip()
        tahun = row["Masuk"].strip()

        # Path foto & qr
        foto_path = f"../assets/photos/{nisn}.jpg"
        qr_path = f"../assets/qrcode/{nisn}.png"

        # Isi halaman HTML
        html_content = f"""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>ID Digital - {nama}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 30px;
            line-height: 1.6;
        }}
        .header {{
            text-align: center;
        }}
        .header img {{
            width: 120px;
        }}
        .info {{
            margin-top: 20px;
        }}
        .info img {{
            border: 1px solid #ccc;
            padding: 5px;
            margin-bottom: 10px;
        }}
        .qr {{
            margin-top: 20px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <img src="{LOGO_PATH}" alt="Logo Sekolah">
        <h2>SMA SKJ JABUNG - MALANG</h2>
        <h3>ID Digital Siswa</h3>
    </div>
    <div class="info">
        <img src="{foto_path}" alt="Foto {nama}" width="150"><br>
        <b>{nama}</b><br>
        <b>NISN:</b> {nisn}<br>
        <b>NIK:</b> {nik}<br>
        <b>Kelas:</b> {kelas}<br>
        <b>TTL:</b> {ttl}<br>
        <b>Alamat:</b> {alamat}<br>
        <b>Tahun Masuk:</b> {tahun}<br>
    </div>
    <div class="qr">
        <img src="{qr_path}" alt="QR {nama}" width="120"><br>
        <small>Scan untuk buka halaman ini</small>
    </div>
</body>
</html>
"""

        # Simpan ke file HTML per siswa
        output_file = os.path.join(PAGES_DIR, f"{nisn}.html")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

print("✅ Semua halaman siswa berhasil digenerate!")
