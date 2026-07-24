# Installs the current D2Coding binaries, standard and ligature builds both, for the
# current user. No administrator rights needed.
#
#   irm https://github.com/naver/d2-coding-font/raw/master/install/install.ps1 | iex
$ErrorActionPreference = "Stop"

$base = "https://github.com/naver/d2-coding-font/raw/master/fonts/ttf"
$fonts = "$env:LOCALAPPDATA\Microsoft\Windows\Fonts"
$reg = "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Fonts"

New-Item -ItemType Directory -Force $fonts | Out-Null
foreach ($name in "D2Coding-Regular", "D2Coding-Bold",
                  "D2Codingligature-Regular", "D2Codingligature-Bold") {
  Write-Host "downloading $name.ttf"
  Invoke-WebRequest "$base/$name.ttf" -OutFile "$fonts\$name.ttf"
  New-ItemProperty -Path $reg -Name "$name (TrueType)" -Value "$fonts\$name.ttf" `
    -PropertyType String -Force | Out-Null
}

Write-Host "Installed into $fonts. Restart your editor or terminal so it picks the fonts up."
