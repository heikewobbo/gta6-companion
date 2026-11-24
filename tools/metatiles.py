import os, sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
for z in range(0, 6):
    files = os.listdir(f"{src}/{z}")
    tiles = {}
    for f in files:
        _, y, x = f[:-4].split(",")
        tiles[(int(x), int(y))] = f
    meta = {}
    for (x, y) in tiles:
        meta.setdefault((x // 4, y // 4), []).append((x, y))
    os.makedirs(f"{dst}/{z}", exist_ok=True)
    for (mx, my), lst in meta.items():
        im = Image.new("RGB", (1024, 1024), (47, 144, 176))
        for (x, y) in lst:
            t = Image.open(f"{src}/{z}/{tiles[(x, y)]}").convert("RGB")
            im.paste(t, ((x - mx * 4) * 256, (y - my * 4) * 256))
        im.save(f"{dst}/{z}/{mx}_{my}.jpg", quality=78, optimize=True)
    print(z, len(meta))
