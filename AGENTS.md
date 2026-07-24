# AGENTS.md

Working notes for coding agents on this repository.

## The repository

D2 Coding is NAVER's monospaced coding font for Korean and Latin, drawn by FONTRIX and
released under the SIL Open Font License 1.1. The layout follows the Google Fonts upstream
convention, and the specimen page at <https://naver.github.io/d2-coding-font/> doubles as
the demo and the place to reproduce rendering problems.

- `fonts/ttf/` holds the four shipped binaries: Regular and Bold, in standard and ligature
  builds. The ligature builds are a strict superset of the standard ones, so one set of
  sources produces both.
- `sources/` holds UFOs reverse-engineered from the shipped TTFs. They are not the original
  design data, and each one is around 130 MB (26,000+ glyphs). Read `sources/README.md`
  before touching them.
- `site/` is the specimen page. Static files with no build step:
  `.github/workflows/pages.yml` publishes the directory to GitHub Pages on every push to
  `master` that touches `site/**`. Regeneration commands are in `site/README.md`.
- `documentation/` holds the article for the Google Fonts submission.

## Git

- The commit identity comes from this clone's local git config. Leave it as it is.
- Commit messages are plain descriptive sentences. No conventional-commit prefixes, and no
  trailers of any kind: no `Co-Authored-By`, no "Generated with" lines.
- The default branch is `master`. The remote uses SSH.

## Writing style

Applies to everything user-facing: the README, site copy, and issue comments.

- English only in committed documentation.
- No em dashes. Write plain sentences.
- Prefer concrete wording over rhetoric. State the actual claim: "fixed width", "one Hangul
  glyph is two Latin columns wide".
- Keep external communication short and humble, and do not state unconfirmed things as fact.

## Practical notes

- README screenshots come from `site/` (`preview.png`, `alignment.png`, `distinction.png`,
  `smooth.png`). Do not link to images hosted outside the repository.
- When `site/og.png` changes, bump the `?v=` on the image URLs in `site/index.html`, and
  keep the declared `og:image:width`/`height` matching the real pixel size. Social sites
  cache the image by URL and trust the declared dimensions.
- After changing the site or the fonts, check the rendering on the live page or a local
  serve of `site/` before reporting the change as done.
- The release procedure is in `RELEASE.md`; `tools/release.py` does the mechanical steps
  (version bump, `CHANGELOG.md` scaffold, site data, release zip).
