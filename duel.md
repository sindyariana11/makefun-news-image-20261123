# Duel varian — NI23 Gelombang 3, Akun 10 (THE FIRST EDITION)

Judul submit: THE FIRST EDITION — Monday 23 November 2026: IRGC Claims Two Patriot Radars Hit in Bahrain

## Tiga varian (satu compose.py, argumen palet/susunan)
- A — abu muda koran, tinta hitam, aksen kuning mustard (palet akun). Strip angka hitam dengan angka kuning.
- B — krem hangat, tinta biru tua, aksen biru. Masthead dan kartu terbaca, tetapi strip angka biru kurang kontras dan kesan korannya lebih lembut.
- C — putih bersih, tinta marun, aksen merah tua. Bersih, tetapi aksen marun bertabrakan dengan chip merah Timur Tengah dan kotak DATE CHECK sehingga hierarki warna lead melemah.

## Penilaian
- Kontras: A tertinggi (tinta hitam di atas abu muda; strip angka hitam-kuning paling menonjol di 300px).
- Keterbacaan 300px: A — masthead, tanggal, judul lead, dan strip angka tetap terbaca jelas; judul 13 kartu grid terbaca sebagai judul tebal yang dapat dibedakan per kartu.
- Kepadatan data: sama di ketiga varian (14 kartu utama + 28 brief ALSO ON = 42 cerita, 6 angka, peta 14 pin, timeline 5 slot, DATE CHECK 6 buangan).

## Pemenang: varian A
Alasan: palet resmi akun (abu muda koran, tinta hitam, mustard), kontras tertinggi, dan satu-satunya varian yang strip angkanya tetap mencolok sesudah dikecilkan.

## Uji 300px
entry.png dikecilkan ke 300×300 (/tmp/ni23g3-akun10-300.png) dan diperiksa visual: masthead "THE FIRST EDITION", tanggal "Monday 23 November 2026", judul lead, dan keenam angka strip masih terbaca; judul kartu grid masih terbaca sebagai baris judul. LULUS.

## Trio lead
Lead akun (pool #2, IRGC klaim radar Patriot Bahrain — atribusi "IRGC claims" di kartu) + pool #43 (Demokrat menang DPR 258–173) + pool #7 (COP31 berakhir tanpa kesepakatan), pilihan builder ini.

## Kenapa lebih kuat dari entry G2 akun ini
Entry G2 akun ini berkonsep "Toko Serba Ada" (lead G2 #34, emas jatuh) — susunan etalase dekoratif. Entry G3 ini halaman depan koran lurus: masthead raksasa, tanggal besar, lead paling besar sebagai kartu #1, teks besar yang terbaca di 300px, 42 cerita terstruktur (kartu bernomor + peta pin + ALSO ON), strip angka yang mengikat kartu, dan kotak DATE CHECK — jauh lebih padat, lebih terbaca, dan lebih setia pada kriteria juri (satu hari bernama, seleksi luas, terbaca, setia, craft).

## Verifikasi teknis
- entry.png: 267102 byte, sha256 6b026f9fdb2b687ffdf05bd581d0c534d8377fb8df905b9bf7a3ad8bdd70d400, IHDR 1024×1024 terverifikasi (struct byte 16–24).
- Margin checker: 13/13 LOLOS.
- main.py dijalankan dua kali dengan MAKEFUN_OUTPUT_DIR berbeda: keluaran byte-identik.
