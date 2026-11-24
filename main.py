import os
import shutil
import sys


def run():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(run())
