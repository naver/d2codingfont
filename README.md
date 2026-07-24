# D2 Coding
[![Github All Releases](https://img.shields.io/github/downloads/naver/d2-coding-font/total.svg)](https://github.com/naver/d2-coding-font)

[![The D2 Coding specimen page](site/preview.png)](https://naver.github.io/d2-coding-font/)

### Download
   - [Ver 1.3.3 (released 2026-07-25)](https://github.com/naver/d2-coding-font/releases/tag/VER1.3.3)
   - Please uninstall any previously installed version before installing.
   - Older versions are available on the [Releases](https://github.com/naver/d2-coding-font/releases) page.

### Try it first
[**naver.github.io/d2-coding-font**](https://naver.github.io/d2-coding-font/) — a live specimen with an
editable playground, the complete ligature list read out of the font, and three tools for pinning
down a rendering problem before you report it: a size ladder from 8px to 24px, a coverage check
against the real `cmap`, and a report template that captures your settings and environment.

![image](https://user-images.githubusercontent.com/6773678/33355628-997fe52e-d4fb-11e7-9d1a-64c3b2d42de8.png)
      - Runs on Windows, macOS and Linux (Ubuntu), and works with a wide range of development tools.
![image](https://user-images.githubusercontent.com/6773678/33353005-fac0c8ec-d4ee-11e7-8e51-3077c1771144.png)

## About the typeface
D2 Coding is based on Nanum Barun Gothic and was optimised for writing code: it improves legibility
and the distinction between similar looking characters, while keeping the Latin design in harmony
with Hangul. Characters that are easy to confuse while reading code — Latin letters, digits, Hangul
and punctuation alike — were reworked to stay distinguishable. It is a monospaced typeface, so line
and character spacing stay consistent in any development environment.

### Clear
Latin letters, digits and similar looking Hangul symbols were drawn to be easy to tell apart while
reading code. Hinting was tuned so that the design stays crisp between 8 and 18pt.

![1](https://cloud.githubusercontent.com/assets/6773678/19587983/8d1a2304-979d-11e6-8320-4e8f0546e716.JPG)

### Smooth
Hangul is based on Nanum Barun Gothic, so the letterforms stay soft and blend naturally with the
Latin design used for code.

![2](https://cloud.githubusercontent.com/assets/6773678/19587989/9a990fae-979d-11e6-82e8-84316b4da96b.JPG)

### Even
Because it is monospaced, code lines up neatly in any development environment. Line and character
spacing were tuned through an internal beta test with developers to improve the readability of code.

![3](https://cloud.githubusercontent.com/assets/6773678/19587988/9a9821f2-979d-11e6-8708-bd57220c219f.JPG)

### Character coverage
1.3.3 maps 19,966 codepoints over 26,188 glyphs: all 11,172 Hangul syllables, Latin and 332
extended characters, 31 control pictures, and 4,620 CJK Unified Ideographs plus 268 compatibility
ideographs.

Earlier versions of this README said Hanja was not included and would fall back to another font.
That was never true of a released build — 1.0 already carried the same 4,620 ideographs, and they
are drawn full width, so they render from D2Coding rather than from a fallback.

A Hangul syllable is exactly twice the advance width of a Latin character, so Korean comments and
string literals keep source code, tables and box drawing output aligned. Hanja is full width too.

### Ligature build
A separate ligature build adds programming ligatures for common operator sequences such as `=>`,
`!=`, `<=` and `->` through the OpenType `calt` feature. Apart from that OpenType code it is
identical to the standard build: the two share the exact same outlines and metrics.

## Repository layout
```
d2-coding-font
├── OFL.txt                  SIL Open Font License 1.1 (full text)
├── LICENSE.md               the same licence, as it read in the project wiki
├── AUTHORS.txt              copyright holders
├── CONTRIBUTORS.txt         contributors
├── documentation/           font description
├── sources/                 reverse-engineered UFO sources
├── site/                    the specimen page published to GitHub Pages
└── fonts/ttf/               current TTF binaries
```

`site/` is deployed by the `Deploy specimen page` GitHub Actions workflow on every push to
`master`.

The files under `fonts/ttf` are the same binaries that ship inside
`D2Coding-Ver1.3.3-20260725.zip`; only the file names were changed to follow the
`FamilyName-StyleName.ttf` convention.

| File | Font name |
| --- | --- |
| `fonts/ttf/D2Coding-Regular.ttf` | D2Coding Regular |
| `fonts/ttf/D2Coding-Bold.ttf` | D2Coding Bold |
| `fonts/ttf/D2Codingligature-Regular.ttf` | D2Coding ligature Regular |
| `fonts/ttf/D2Codingligature-Bold.ttf` | D2Coding ligature Bold |

TTC bundles and every earlier version are on the
[Releases](https://github.com/naver/d2-coding-font/releases) page. The release archives used to sit
in the repository root as well; they were removed so that the repository holds sources and current
binaries only. Nothing was lost — every archive that was in the root is attached to its release,
under the same file name.

## Sources
The original design sources are no longer available. The typeface was drawn for NAVER by FONTRIX
in 2015, the people who worked on it have since left, and no `.glyphs` or `.ufo` files were kept.
The UFO files under `sources/` were therefore reverse-engineered from the released binaries with
[fontTools](https://github.com/fonttools/fonttools) and
[extractor](https://github.com/robotools/extractor). They carry the quadratic outlines exactly as
they are in the shipped TTFs, so they are a starting point for further work rather than the
original design data. See [sources/README.md](sources/README.md) for details.

## What changed in 1.3.3
Version 1.3.3 is a metadata-only release; no outline, metric or OpenType data was changed.

* The copyright, trademark and vendor URL records still named NHN Corporation. NAVER Corporation
  was spun off from NHN in 2013 and is the copyright holder, so those records now read
  `NAVER Corporation` / `https://www.navercorp.com`.
* The license URL (name ID 14) pointed at `http://dev.naver.com/wiki/nanumfont/…`, which is dead.
  It now points at `https://openfontlicense.org`.

## License
Anyone may use D2 Coding, and anyone may redistribute it under the terms of the SIL Open Font
License.

D2 Coding is released under the OFL (SIL Open Font License), an internationally recognised license
for open fonts. It places no restriction on use, and redistribution is allowed as long as the
license is included — including bundling the font with other software, commercial software
included.

The full license text is in [OFL.txt](OFL.txt), and the same text as it was written in the project
wiki is in [LICENSE.md](LICENSE.md). Until now it lived only in the wiki, which is what made the
license hard to find.
