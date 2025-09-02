import csv
import os

# Lokasi file CSV dan output
CSV_FILE = "mapping_pages.csv"
OUTPUT_DIR = "pages"

# Pastikan folder output ada
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Template HTML untuk setiap siswa
TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ID Digital - {nama}</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f7f9fc;
      margin: 0;
      padding: 20px;
    }}
    .card {{
      max-width: 600px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      text-align: center;
    }}
    .logo {{
      width: 100px;
      margin-bottom: 10px;
    }}
    .foto {{
      width: 150px;
      border-radius: 8px;
      margin: 15px 0;
    }}
    .qrcode {{
      width: 150px;
      margin-top: 15px;
    }}
    .info {{
      text-align: left;
      margin-top: 15px;
    }}
    .info b {{
      display: inline-block;
      width: 120px;
    }}
  </style>
</head>
<body>
  <div class="card">
    <!-- Logo Sekolah -->
    <img src="../assets/logo.png" alt="Logo SMA SKJ JABUNG" class="logo">

    <h2>SMA SKJ JABUNG - MALANG</h2>
    <h3>ID Digital Siswa</h3>

    <!-- Foto Siswa -->
    <img src="../assets/foto/{nisn}.jpg" alt="Foto {nama}" class="foto">

    <!-- Data Siswa -->
    <div class="info">
      <p><b>Nama</b>: {nama}</p>
      <p><b>NISN</b>: {nisn}</p>
      <p><b>NIK</b>: {nik}</p>
      <p><b>Kelas</b>: {kelas}</p>
      <p><b>TTL</b>: {ttl}</p>
      <p><b>Alamat</b>: {alamat}</p>
      <p><b>Tahun Masuk</b>: {tahun_masuk}</p>
    </div>

    <!-- QR Code -->
    <img src="../assets/qrcode/{nisn}.png" alt="QR {nama}" class="qrcode">
    <p>Scan untuk membuka halaman ini</p>
  </div>
</body>
</html>
"""

# Baca data dari CSV
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nisn = row["NISN"]
        nama = row["Nama"]
        nik = row["NIK"]
        kelas = row["Kelas"]
        ttl = row["TTL"]
        alamat = row["Alamat"]
        tahun_masuk = row["TahunMasuk"]

        # Buat konten HTML dari template
        html_content = TEMPLATE.format(
            nisn=nisn,
            nama=nama,
            nik=nik,
            kelas=kelas,
            ttl=ttl,
            alamat=alamat,
            tahun_masuk=tahun_masuk
        )

        # Simpan ke file HTML
        output_path = os.path.join(OUTPUT_DIR, f"{nisn}.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

print("✅ Semua halaman siswa berhasil dibuat di folder 'pages/'")
