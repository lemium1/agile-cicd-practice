from pathlib import Path
from app import render_page

output = Path("dist")
output.mkdir(exist_ok=True)
(output / "index.html").write_text(render_page(), encoding="utf-8")
print("Build completed: dist/index.html")
