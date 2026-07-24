# Specimen page

The D2Coding specimen and issue reproduction page, served at
<https://naver.github.io/d2-coding-font/>.

`.github/workflows/pages.yml` publishes this directory to GitHub Pages on every push to `master`.
There is nothing to build: the workflow uploads these files as they are.

```
index.html          the page
style.css
app.js              controls, ligature grid, size ladder, coverage check, report template
data.js             generated — ligature list, cmap ranges, glyph counts
fonts/*.woff2       generated — web fonts built from the shipped TTFs
og.png              generated — the card shown when the page is shared
preview.png         the screenshot used in the repository README
tools/build-data.py regenerates data.js and the web fonts
tools/og-card.html  source for og.png
```

## Regenerating the social card

`og.png` is referenced by the `og:image` and `twitter:image` tags, at a fixed 2400x1260 that the
tags declare. Serve this directory over HTTP so the card can load the web fonts, then:

```sh
google-chrome --headless=new --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1200,630 --virtual-time-budget=8000 \
  --screenshot=og.png http://localhost:8000/tools/og-card.html
```

If you change the output size, update `og:image:width` and `og:image:height` in `index.html` to
match — Facebook trusts the declared numbers when it lays the card out before fetching the image.

## Regenerating after a font release

```sh
pip install fonttools brotli uharfbuzz
python tools/build-data.py /path/to/d2-coding-font/fonts/ttf
```

Both web fonts come from the **ligature** build. The standard build is the same font with `calt`
switched off, so the ligature toggle on the page shows both builds from one pair of files. Nothing
in `data.js` is written by hand: the ligature list is discovered from the `GSUB` chaining
contextual rules and then verified with HarfBuzz, and the coverage ranges come from the `cmap`.
