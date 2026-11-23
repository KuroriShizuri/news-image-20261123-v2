"""Entry for make.fun news-image-20261123.

Copies the pre-rendered newspaper front page (entry.png, in this
directory) byte-for-byte to the output directory as entry.png.
Standard library only; no network, no other files.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print("wrote %s (%d bytes)" % (dst, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
