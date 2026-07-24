# Release procedure

How a new version of D2Coding is published. `tools/release.py` does the mechanical steps;
the steps that need judgment stay manual.

## 1. Update the binaries

Put the four new TTFs into `fonts/ttf/` under the existing names:

```
D2Coding-Regular.ttf           D2Coding-Bold.ttf
D2Codingligature-Regular.ttf   D2Codingligature-Bold.ttf
```

## 2. Run the release script

```sh
pip install fonttools brotli uharfbuzz
python3 tools/release.py X.Y.Z
```

The script, in order:

- prints the version records inside the four binaries, so you can confirm they match
  `X.Y.Z` before anything is published
- bumps the version in `README.md` (download link), `site/index.html` (download button,
  hero note) and `site/app.js` (sample header, report template)
- opens a dated `## X.Y.Z` section at the top of `CHANGELOG.md` with a TODO body
- regenerates `site/data.js` and the WOFF2 web fonts from the new binaries
- builds `dist/D2Coding-VerX.Y.Z-YYYYMMDD.zip` in the same layout as previous releases:
  `D2Coding/`, `D2CodingLigature/` and `D2CodingAll/`, with the TTCs assembled from the
  four TTFs, plus `OFL.txt`

`--date YYYYMMDD` uses a date other than today; `--skip-site` and `--skip-dist` leave
those steps out.

## 3. Write the changelog

Replace the TODO in `CHANGELOG.md`: plain sentences, and link the issues that were fixed.

## 4. Check what the script cannot know

- The "Character coverage" numbers in `README.md`, if glyphs were added or removed. The
  new counts are at the top of the regenerated `site/data.js`.
- The captures in `site/` (`preview.png`, `alignment.png`, `distinction.png`,
  `smooth.png`) and the social card `og.png`, if letterforms changed. Regeneration
  commands are in `site/README.md`; remember the `?v=` bump when `og.png` changes.

## 5. Commit and verify

Commit and push to `master`, then wait for the `Deploy specimen page` workflow. On
<https://naver.github.io/d2-coding-font/> the hero stats and the ligature list come
straight from the regenerated `data.js`, so wrong numbers there mean step 2 was skipped.

## 6. Tag and publish

```sh
git tag VERX.Y.Z
git push origin VERX.Y.Z
gh release create VERX.Y.Z dist/D2Coding-VerX.Y.Z-YYYYMMDD.zip \
  --title "D2Coding Ver X.Y.Z" --notes-file notes.md
```

Base the release notes on the CHANGELOG entry, and keep the reminder to uninstall any
previously installed version before installing the new one.
