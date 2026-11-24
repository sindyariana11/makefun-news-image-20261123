"""THE MORNING RECORD — entrypoint NI23 G4 Akun 10 (@sindyariana115203).

Koran halaman depan satu gambar untuk Senin 23 November 2026: lead
Demokrat DPR 258-173, 13 kartu bernomor, 26 brief ALSO ON, peta titik
berpin, strip angka, dan kotak DATE CHECK. Program ini hanya menyalin
entry.png yang sudah jadi ke direktori keluaran Make Fun — tidak ada
pemrosesan gambar di sini (stdlib only, copy-only).
"""
import hashlib
import os
import shutil
import sys

EXPECTED_BYTES = 214046
EXPECTED_SHA256 = "d1ab3f5d3c539b70db3463a8695c1da90a9b4108d26a36cb4dc3b3378be9aa6f"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    payload = open(source, "rb").read()
    if len(payload) != EXPECTED_BYTES:
        print("ukuran entry.png menyimpang: %d" % len(payload), file=sys.stderr)
        return 1
    if hashlib.sha256(payload).hexdigest() != EXPECTED_SHA256:
        print("sha256 entry.png menyimpang", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    copied = open(target, "rb").read()
    if hashlib.sha256(copied).hexdigest() != EXPECTED_SHA256:
        print("salinan keluaran tidak utuh", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
