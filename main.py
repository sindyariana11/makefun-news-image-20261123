#!/usr/bin/env python3
"""Delivery program for THE FIRST EDITION (Akun 10, news-image-20261123).

THE FIRST EDITION is this account's own front page for Monday
23 November 2026. The artwork is already finished and sealed as
entry.png next to this file, so the job here is deliberately small:
carry that exact page into the output folder, byte for byte, and
refuse to deliver anything whose length or fingerprint has drifted
from the sealed values recorded below.

Only the Python standard library is used, and nothing is rendered,
resized or re-encoded along the way.
"""

import hashlib
import os
import sys

SEALED_LENGTH = 267102
SEALED_DIGEST = "6b026f9fdb2b687ffdf05bd581d0c534d8377fb8df905b9bf7a3ad8bdd70d400"
PAGE_NAME = "entry.png"
HARD_LIMIT = 1024 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def load_page():
    folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(folder, PAGE_NAME), "rb") as stream:
        return stream.read()


def verify_page(blob):
    if not blob:
        raise SystemExit("entry.png is empty; nothing to deliver")
    if not blob.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png does not start with the PNG signature")
    if len(blob) > HARD_LIMIT:
        raise SystemExit("entry.png is over the 1 MiB ceiling: %d bytes" % len(blob))
    if len(blob) != SEALED_LENGTH:
        raise SystemExit(
            "entry.png length is %d, sealed length is %d" % (len(blob), SEALED_LENGTH)
        )
    actual = hashlib.sha256(blob).hexdigest()
    if actual != SEALED_DIGEST:
        raise SystemExit("entry.png digest mismatch: %s" % actual)
    # Revision guard: the sealed page must also declare the bounty's
    # exact canvas in its IHDR header, 1024 by 1024 pixels, so a
    # same-length file with a different canvas cannot pass on the
    # digest-and-length checks alone if the seal is ever regenerated.
    if len(blob) < 24:
        raise SystemExit("entry.png is too short to carry an IHDR header")
    canvas = (int.from_bytes(blob[16:20], "big"), int.from_bytes(blob[20:24], "big"))
    if canvas != (1024, 1024):
        raise SystemExit("entry.png canvas is %dx%d, expected 1024x1024" % canvas)


def deliver(blob):
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, PAGE_NAME)
    with open(target, "wb") as stream:
        stream.write(blob)
    return target


def main():
    blob = load_page()
    verify_page(blob)
    target = deliver(blob)
    sys.stderr.write(
        "delivered %s (%d bytes, sha256 %s)\n" % (target, len(blob), SEALED_DIGEST)
    )


if __name__ == "__main__":
    main()
