#!/usr/bin/env python3
import argparse
import os
import subprocess
import shutil
from pathlib import Path


def run(cmd: list, cwd: Path):
    print("cd ", cwd, "&&", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(cwd))


parser = argparse.ArgumentParser()
parser.add_argument("--clean", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()


variants = ["dynamic", "dynamic-with-lld", "static", "static-with-lld"]
srcdir = Path(__file__).parent
for variant in variants:
    # builddir = srcdir / (os.uname().sysname + "-" + variant)  # type: Path
    builddir = Path("/exports/users/alr48/postgres") / (os.uname().sysname + "-" + variant) 
    if args.clean and (builddir / "CMakeCache.txt").exists():
        print("rm -rf", builddir)
        shutil.rmtree(str(builddir))
    if not builddir.exists():
        os.makedirs(str(builddir), exist_ok=True)
    run(["cmake-for-cheribsd-cheriabi-" + variant + ".sh", "-GNinja", "-DCMAKE_BUILD_TYPE=Debug", str(srcdir.absolute())], cwd=builddir)
    run(["ninja"], cwd=builddir)

