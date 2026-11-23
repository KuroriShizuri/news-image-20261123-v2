"""Entry for make.fun news-image-20261123.

Copies the pre-rendered newspaper front page (entry.png, in this
directory) byte-for-byte to the output directory as entry.png.
Standard library only; no network, no other files.
"""

import hashlib
import os
import shutil
import sys


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png missing at %s" % src, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_hash = sha256_file(src)
    dst_hash = sha256_file(dst)
    if src_hash != dst_hash:
        print("error: copy verification failed: src sha256 %s != dst sha256 %s"
              % (src_hash, dst_hash), file=sys.stderr)
        return 1
    size = os.path.getsize(dst)
    print("wrote %s (%d bytes, sha256 %s)" % (dst, size, dst_hash))
    return 0


if __name__ == "__main__":
    sys.exit(main())
