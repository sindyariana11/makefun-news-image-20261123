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
