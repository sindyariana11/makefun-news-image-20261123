# DUEL NI23 G4 - Akun 10 - THE MORNING RECORD
Judul submit: THE MORNING RECORD - Monday 23 November 2026: Democrats Take the House 258-173

## Duel A vs B (render 1024x1024, diperkecil ke 300x300)
- A: grid 3 kolom, kartu 328px lebar, judul 24px, fakta 14px 2 baris penuh
  di dalam kartu. Ukuran 212.105 byte.
- B: grid 4 kolom, kartu 244px lebar; judul membungkus 3 baris, baris
  header kartu sempit (lokasi bertabrakan dengan sumber/status), fakta
  terpotong. Ukuran 201.540 byte.
- Keterbacaan 300px: judul A terbaca sebagai blok teks tegas; B pecah
  menjadi kolom sempit dan headernya bertumpuk.
- PEMENANG: A (lebih terbaca di 300px; B hanya menang ukuran, bukan seri).

## Gerbang Tembak Pengganti vs entry berdiri G3
Lawan: G3 "THE FIRST EDITION", 267.102 byte, sha 6b026f9f..., 13 kartu,
palet abu + muster (data koordinator; repo v3 tidak dibuka).
- Keterbacaan: A memakai 13 kartu besar yang sama lapangnya dengan judul
  24-28px dan fakta 14px yang muat penuh; tidak ada teks meluber keluar
  kartu (cacat render pertama sudah diperbaiki dan diverifikasi visual).
- Perabot: A lengkap dan terverifikasi di gambar - kicker jujur
  "52 reports cross-checked", masthead 66px + tanggal 44px, strip
  harga/cuaca/pasar, strip 8 region berjumlah (total 39 = 13 kartu +
  26 also-on), timeline UTC 8 slot, DAY IN NUMBERS 8 angka, peta titik
  pin bernomor 1-13 + legenda, ALSO ON 26 cerita, DATE CHECK 7 buangan
  bernama + bertanggal, footer HOW SURE 3 baris.
- Kesetiaan: nol klaim sebagai fakta - kartu 3 berjudul "IRGC Claims..."
  berchip CLAIM; kapal Rusia "still burns", bukan tenggelam; Kyiv 14
  hilang dibingkai "Zelenskiy Says"; Demokrat 258-173 dibingkai sebagai
  hasil/hitungan hari itu. DATE CHECK tidak bertabrakan dengan kartu
  mana pun (SpiceJet di also-on = permohonan audit pilot 23 Nov; buangan
  D3 = fundraise 18 Nov, peristiwa berbeda dan dibedakan redaksinya).
- Keluasan: 39 cerita, 8 region, trio konsensus 23 Nov lengkap sebagai
  kartu (Hormuz #2, IRGC Patriot #3, Kyiv #4/#5) + lead akun #43 Demokrat
  sebagai kartu 1 terbesar.
- Ukuran: 212.105 byte vs G3 267.102 byte - A lebih ramping.
- VONIS: LEBIH KUAT dari G3 di semua sumbu terukur.

## Audit nol-batas
- Nol klaim sebagai fakta, nol kontradiksi DATE CHECK, nol teks garbled
  (render final dibaca visual penuh sesudah perbaikan terakhir).
- Uji fakta silang: setiap angka di gambar cocok dengan pool
  (258/173/1992, 720/9d, $3,538/$5,595/-2,41%, 14 hilang, 6 tewas,
  anak 7 tahun, 700.000+, 65,9%, 10.105, 75 distrik, 7 kantong/50 hilang,
  Rs28.000 crore, $5 juta, 16 Des, tanggal buangan 18-22 Nov).

## Berkas final
- entry.png: 212.105 byte, 1024x1024, sha256
  942ffc53a6c1d40f644a21ddbb81ca536719aca9ff23e6506703628784d65e8f
- test_entry.py: LULUS (ukuran, IHDR 1024x1024, semua kata segar ada).
- Hash jangkar: 296c0adc8c7df414276b01ac60a558597ad0660c
- Hash commit staging: 9e55533705b042306212fe708c9521d2d068825c (commit isi; duel.md diperbarui di commit sesudahnya)

## KOREKSI EKOR (24 Nov, koordinator ekor G4 — sebelum submit)
Dua cacat build awal diperbaiki TANPA mengubah konsep/duel:
1. Margin checker membaca 1/13: compose.py gaya bebas tidak terbaca AST
   checker + 4 deck di bawah 2 fakta (kartu 5, 7, 12, 13) + ALSO ON 8px.
   Obat pola armada (sama seperti ekor Ak15/Ak18/F1): compose.py
   direstrukturisasi ke gaya armada (grid/NUMS/TL/BRIEFS/dc/PINS +
   lead()/mini() dengan fb/fr/fsr) dan deck 4 kartu itu diperkaya HANYA
   dengan fakta cerita pool yang sama: #5 menyebut Zelenskiy + Kyiv,
   #7 "Russian-flagged ... Gulf of Finland", #12 atribusi AP,
   #13 Lisbon + Portugal. Deck per kartu sesudah koreksi:
   [6,2,2,2,3,2,3,2,2,5,2,2,2] — 100% >=2 fakta, rata-rata 2,69.
2. Baris fakta kedua beberapa kartu meluber melewati batas bawah kartu
   menimpa pita kartu berikutnya (terlihat di render penuh). Obat: font
   deck grid 14->13px, langkah baris 18->15, offset fakta 9->6 — semua
   baris fakta kini di dalam kartu (diverifikasi visual render penuh).
   Pita ALSO ON digambar ulang full-width pada 10px (5 baris, semua
   brief terbaca); peta titik dipadatkan ke pita yang sama (pin tetap
   13 = jumlah kartu); DATE CHECK tetap 7 buangan bernama.
- Margin checker sesudah koreksi: 13/13 LOLOS (0 GAGAL).
- test_entry.py: LULUS. Uji 300px: masthead + 13 judul terbaca.
- entry.png FINAL: 214.046 byte, 1024x1024, sha256
  d1ab3f5d3c539b70db3463a8695c1da90a9b4108d26a36cb4dc3b3378be9aa6f
- VONIS vs G3 BERDIRI: TETAP LEBIH KUAT — koreksi hanya menambah fakta
  deck, keterbacaan, dan kerapian; tidak ada sumbu yang mundur
  (ukuran 214.046 B tetap < G3 267.102 B).
