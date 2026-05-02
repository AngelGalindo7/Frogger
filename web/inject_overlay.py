"""Inject overlay assets into pygbag-generated build/web/index.html."""
import shutil
from pathlib import Path

BUILD = Path("build/web")
SRC = Path("web")

for name in ("overlay.css", "overlay.js", "overlay.html"):
    shutil.copy(SRC / name, BUILD / name)

index = BUILD / "index.html"
html = index.read_text(encoding="utf-8")

overlay_html = (SRC / "overlay.html").read_text(encoding="utf-8")
link_tag = '<link rel="stylesheet" href="overlay.css">'
script_tag = '<script src="overlay.js"></script>'

if link_tag not in html:
    html = html.replace("</head>", f"  {link_tag}\n</head>", 1)
if "<!-- overlay-inject -->" not in html:
    marker = "<!-- overlay-inject -->\n"
    html = html.replace("<body>", f"<body>\n{marker}{overlay_html}\n", 1)
if script_tag not in html:
    html = html.replace("</body>", f"  {script_tag}\n</body>", 1)

index.write_text(html, encoding="utf-8")
print("overlay injected into", index)
