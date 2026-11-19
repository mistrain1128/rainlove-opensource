"""Instantiate static weights from the installed Noto Serif CJK variable fonts."""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "fonts"
OUT.mkdir(exist_ok=True)
FONTS = Path(r"C:\Windows\Fonts")

for src, weight, name in [
    ("NotoSerifJP-VF.ttf", 500, "NotoSerifJP-Medium.ttf"),
    ("NotoSerifSC-VF.ttf", 400, "NotoSerifSC-Regular.ttf"),
]:
    font = TTFont(FONTS / src)
    axes = {a.axisTag: (a.minValue, a.defaultValue, a.maxValue) for a in font["fvar"].axes}
    print(src, axes)
    instancer.instantiateVariableFont(font, {"wght": weight}, inplace=True)
    font.save(OUT / name)
    print("wrote", name)