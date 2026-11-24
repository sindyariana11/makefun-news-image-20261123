#!/usr/bin/env python3
"""THE FIRST EDITION - entry program for Akun 10 (news-image-20261123).

A straight newspaper front page for Monday 23 November 2026, drawn by
this account alone: 42 stories, lead = IRGC claims two Patriot radars
hit in Bahrain (attributed). This program is stdlib-only and copy-only:
it copies the finished entry.png beside it into the output directory
and refuses to run if the image size or digest has changed.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 267102
EXPECTED_SHA256 = "6b026f9fdb2b687ffdf05bd581d0c534d8377fb8df905b9bf7a3ad8bdd70d400"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def read_entry():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png"), "rb") as handle:
        return handle.read()


def check_image(data):
    if len(data) == 0:
        sys.exit("entry.png is empty")
    if data[:8] != PNG_MAGIC:
        sys.exit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        sys.exit("entry.png exceeds 1 MiB: %d bytes" % len(data))
    if len(data) != EXPECTED_BYTES:
        sys.exit("entry.png size changed: %d, expected %d" % (len(data), EXPECTED_BYTES))
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        sys.exit("entry.png sha256 does not match the recorded digest")


def check_dimensions(data):
    """Second, independent guard added on revision: the PNG IHDR must
    declare exactly 1024 x 1024 pixels, the sealed gate for this bounty,
    so a resized or padded image can never slip through on size alone."""
    if len(data) < 24:
        sys.exit("entry.png too short to hold an IHDR header")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if (width, height) != (1024, 1024):
        sys.exit("entry.png dimensions are %dx%d, expected 1024x1024" % (width, height))


def main():
    data = read_entry()
    check_image(data)
    check_dimensions(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as handle:
        handle.write(data)
    sys.stderr.write("entry.png: %d bytes sha256=%s\n" % (len(data), EXPECTED_SHA256))


if __name__ == "__main__":
    main()
