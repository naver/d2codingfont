#!/bin/sh
# Installs the current D2Coding binaries, standard and ligature builds both, for the
# current user. Linux puts them into ~/.local/share/fonts, macOS into ~/Library/Fonts.
#
#   curl -fsSL https://github.com/naver/d2-coding-font/raw/master/install/install.sh | sh
set -eu

BASE="https://github.com/naver/d2-coding-font/raw/master/fonts/ttf"
FILES="D2Coding-Regular.ttf D2Coding-Bold.ttf D2Codingligature-Regular.ttf D2Codingligature-Bold.ttf"

case "$(uname)" in
  Darwin) DIR="$HOME/Library/Fonts" ;;
  *)      DIR="$HOME/.local/share/fonts" ;;
esac

mkdir -p "$DIR"
for f in $FILES; do
  echo "downloading $f"
  curl -fsSL "$BASE/$f" -o "$DIR/$f"
done

if command -v fc-cache >/dev/null 2>&1; then
  fc-cache -f
fi

echo "Installed into $DIR. Restart your editor or terminal so it picks the fonts up."
