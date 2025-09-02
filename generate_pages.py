foto_path = f"../assets/photos/{nisn}.png"
qr_path = f"../assets/qrcode/{nisn}.png"

html_content = f"""
<html>
<head>
  <title>ID Digital - {nama}</title>
</head>
<body>
  <div style="text-align:center">
    <img src="../assets/logo.png" width="120"><br>
    <h2>SMA SKJ JABUNG - MALANG</h2>
    <h3>ID Digital Siswa</h3>
  </div>
  <div>
    <img src="{foto_path}" alt="Foto {nama}" width="150"><br>
    <b>{nama}</b><br>
    NISN: {nisn}<br>
    NIK: {nik}<br>
    Kelas: {kelas}<br>
    TTL: {ttl}<br>
    Alamat: {alamat}<br>
    Tahun Masuk: {tahun}<br>
    <br>
    <img src="{qr_path}" alt="QR {nama}" width="120"><br>
    <small>Scan untuk buka halaman ini</small>
  </div>
</body>
</html>
"""
