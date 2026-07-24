#!/usr/bin/env python3
"""Mechanical steps of a D2Coding release. See RELEASE.md for the full procedure.

Usage:
    python3 tools/release.py X.Y.Z [--date YYYYMMDD] [--skip-site] [--skip-dist]

Needs fonttools; the site step also needs brotli and uharfbuzz.
"""

import argparse
import datetime
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TTFS = {
    "regular": ROOT / "fonts/ttf/D2Coding-Regular.ttf",
    "bold": ROOT / "fonts/ttf/D2Coding-Bold.ttf",
    "lig_regular": ROOT / "fonts/ttf/D2Codingligature-Regular.ttf",
    "lig_bold": ROOT / "fonts/ttf/D2Codingligature-Bold.ttf",
}


def check_binaries(version):
    from fontTools.ttLib import TTFont

    missing = [p for p in TTFS.values() if not p.exists()]
    if missing:
        for p in missing:
            print(f"missing: {p}", file=sys.stderr)
        sys.exit(1)
    print("Version records in fonts/ttf; confirm they match", version)
    for path in TTFS.values():
        font = TTFont(path, lazy=True)
        name5 = font["name"].getDebugName(5)
        rev = font["head"].fontRevision
        print(f"  {path.name}: {name5!r} / head.fontRevision {rev:.3f}")


def sub_file(path, pattern, repl):
    text = path.read_text(encoding="utf-8")
    new, n = re.subn(pattern, repl, text)
    if n != 1:
        print(f"WARNING {path.relative_to(ROOT)}: {n} matches for /{pattern}/, expected 1")
    if n:
        path.write_text(new, encoding="utf-8")


def update_versions(version, iso_date):
    sub_file(
        ROOT / "README.md",
        r"\[Ver [0-9.]+ \(released \d{4}-\d{2}-\d{2}\)\]"
        r"\(https://github\.com/naver/d2-coding-font/releases/tag/VER[0-9.]+\)",
        f"[Ver {version} (released {iso_date})]"
        f"(https://github.com/naver/d2-coding-font/releases/tag/VER{version})",
    )
    sub_file(ROOT / "site/index.html", r"Download [0-9.]+</a>", f"Download {version}</a>")
    sub_file(
        ROOT / "site/index.html",
        r"the actual [0-9.]+ ligature binaries",
        f"the actual {version} ligature binaries",
    )
    sub_file(
        ROOT / "site/app.js",
        r"// D2Coding [0-9.]+ - github\.com/naver/d2-coding-font",
        f"// D2Coding {version} - github.com/naver/d2-coding-font",
    )
    sub_file(
        ROOT / "site/app.js",
        r"D2Coding [0-9.]+ \(ligature build, WOFF2\)",
        f"D2Coding {version} (ligature build, WOFF2)",
    )
    print("Version strings updated in README.md, site/index.html and site/app.js")


def update_changelog(version, iso_date):
    path = ROOT / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    if re.search(rf"^## {re.escape(version)} ", text, re.M):
        print(f"CHANGELOG.md already has a {version} section, leaving it alone")
        return
    first = text.index("\n## ")
    entry = f"\n## {version} ({iso_date})\n\nTODO: describe this release.\n"
    path.write_text(text[:first] + entry + text[first:], encoding="utf-8")
    print("Opened a new CHANGELOG.md section; replace the TODO before tagging")


def build_site():
    subprocess.run(
        [sys.executable, "tools/build-data.py", str(ROOT / "fonts/ttf")],
        cwd=ROOT / "site",
        check=True,
    )


def build_ttc(paths, out):
    from fontTools.ttLib import TTCollection, TTFont

    coll = TTCollection()
    coll.fonts = [TTFont(p) for p in paths]
    coll.save(out)


def build_dist(version, date):
    stamp = f"Ver{version}-{date}"
    stage = ROOT / "dist" / f"D2Coding-{stamp}"
    if stage.exists():
        shutil.rmtree(stage)
    std = stage / "D2Coding"
    lig = stage / "D2CodingLigature"
    both = stage / "D2CodingAll"
    for d in (std, lig, both):
        d.mkdir(parents=True)

    shutil.copy(TTFS["regular"], std / f"D2Coding-{stamp}.ttf")
    shutil.copy(TTFS["bold"], std / f"D2CodingBold-{stamp}.ttf")
    shutil.copy(TTFS["lig_regular"], lig / f"D2Coding-{stamp}-ligature.ttf")
    shutil.copy(TTFS["lig_bold"], lig / f"D2CodingBold-{stamp}-ligature.ttf")
    build_ttc([TTFS["regular"], TTFS["bold"]], std / f"D2Coding-{stamp}.ttc")
    build_ttc([TTFS["lig_regular"], TTFS["lig_bold"]], lig / f"D2Coding-{stamp}-ligature.ttc")
    build_ttc(
        [TTFS["regular"], TTFS["bold"], TTFS["lig_regular"], TTFS["lig_bold"]],
        both / f"D2Coding-{stamp}-all.ttc",
    )
    shutil.copy(ROOT / "OFL.txt", stage / "OFL.txt")

    zip_path = ROOT / "dist" / f"D2Coding-{stamp}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(stage.rglob("*")):
            z.write(p, p.relative_to(stage))
    shutil.rmtree(stage)
    print(f"Built {zip_path.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="version number, e.g. 1.3.4")
    parser.add_argument("--date", default=datetime.date.today().strftime("%Y%m%d"),
                        help="release date as YYYYMMDD (default: today)")
    parser.add_argument("--skip-site", action="store_true",
                        help="do not regenerate site/data.js and the web fonts")
    parser.add_argument("--skip-dist", action="store_true",
                        help="do not build the release zip")
    args = parser.parse_args()

    if not re.fullmatch(r"\d+(\.\d+)+", args.version):
        parser.error(f"{args.version!r} does not look like a version number")
    if not re.fullmatch(r"\d{8}", args.date):
        parser.error("--date must be YYYYMMDD")
    iso_date = f"{args.date[:4]}-{args.date[4:6]}-{args.date[6:]}"

    check_binaries(args.version)
    update_versions(args.version, iso_date)
    update_changelog(args.version, iso_date)
    if not args.skip_site:
        build_site()
    if not args.skip_dist:
        build_dist(args.version, args.date)

    print()
    print("Done. What is left (details in RELEASE.md):")
    print("  1. replace the TODO in CHANGELOG.md")
    print("  2. check the coverage numbers in README.md and the captures in site/")
    print("  3. commit, push, and wait for the Pages deploy")
    print(f"  4. git tag VER{args.version} && git push origin VER{args.version}")
    print(f"  5. gh release create VER{args.version} dist/D2Coding-Ver{args.version}-{args.date}.zip")


if __name__ == "__main__":
    main()
