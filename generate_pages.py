import csv
import os

# Path file mapping siswa
MAPPING_FILE = "mapping_pages.csv"

# Folder output HTML
OUTPUT_FOLDER = "pages"

# Template HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ID Digital - {nama}</title>
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
    <div class="card">
        <img src="../assets/logo.png" alt="Logo Sekolah" width="100">
        <h2>SMA SKJ JABUNG - MALANG</h2>
        <h3>ID Digital Siswa</h3>
        
        <img src="../assets/foto/{nisn}.jpg" alt="Foto {nama}" width="180"><br><br>
        
        <h2>{nama}</h2>
        <p><b>NISN:</b> {nisn}</p>
        <p><b>NIK:</b> {nik}</p>
        <p><b>Kelas:</b> {kelas}</p>
        <p><b>TTL:</b> {ttl}</p>
        <p><b>Alamat:</b> {alamat}</p>
        <p><b>Tahun Masuk:</b> {tahun}</p>
        
        <p><a href="{drive_link}" target="_blank">Buka file foto (Google Drive)</a></p>
        
        <img src="../assets/qrcode/{nisn}.png" alt="QR {nama}" width="150"><br>
        <p>Scan untuk buka halaman ini</p>
    </div>
</body>
</html>
"""

# Fungsi pembuat halaman
def generate_pages():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    with open(MAPPING_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            html_content = HTML_TEMPLATE.format(
                nama=row['Nama'],
                nisn=row['NISN'],
                nik=row['NIK'],
                kelas=row['Kelas'],
                ttl=row['TTL'],
                alamat=row['Alamat'],
                tahun=row['Tahun Masuk'],
                drive_link=row['DriveLink']
            )

            output_path = os.path.join(OUTPUT_FOLDER, f"{row['NISN']}.html")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"✅ Halaman dibuat: {output_path}")

if __name__ == "__main__":
    generate_pages()
