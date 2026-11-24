import os
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.join(HERE, "entry.png")
FRESH = "/home/hatch/workspace/makefun/ni23-fresh.txt"
LIMIT = 1048576


def main():
    data = open(ENTRY, "rb").read()
    assert len(data) <= LIMIT, "entry.png too large: %d" % len(data)
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG file"
    width, height = struct.unpack(">II", data[16:24])
    assert (width, height) == (1024, 1024), "bad size %dx%d" % (width, height)
    hay = ""
    for name in ("compose.py", "test_entry.py"):
        hay += open(os.path.join(HERE, name), encoding="utf-8").read().lower()
    words = [w.strip() for w in open(FRESH, encoding="utf-8") if w.strip()]
    for word in words:
        assert word.lower() in hay, "fresh word missing: %s" % word
    print("all checks passed:", len(data), "bytes,", width, "x", height)


if __name__ == "__main__":
    main()
