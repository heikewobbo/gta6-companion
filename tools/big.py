import os, sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
for z in (4, 5):
    os.makedirs(f"{dst}/{z}", exist_ok=True)
    groups = {}
    for f in os.listdir(f"{src}/{z}"):
        x, y = map(int, f[:-4].split("_")); groups.setdefault((x//2, y//2), []).append((x, y, f))
    for (bx, by), lst in groups.items():
        im = Image.new("RGB", (2048, 2048), (47, 144, 176))
        for x, y, f in lst: im.paste(Image.open(f"{src}/{z}/{f}"), ((x-bx*2)*1024, (y-by*2)*1024))
        im.save(f"{dst}/{z}/{bx}_{by}.jpg", quality=76, optimize=True)
    print(z, len(groups))
