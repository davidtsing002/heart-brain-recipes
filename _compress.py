from PIL import Image
import os
src = "recipe-images"
total = 0
for i in range(1, 11):
    im = Image.open(f"{src}/r{i}.png").convert("RGB")
    w, h = im.size
    mx = 900
    if max(w, h) > mx:
        r = mx / max(w, h)
        im = im.resize((int(round(w * r)), int(round(h * r))))
    out = f"{src}/r{i}.webp"
    im.save(out, "WEBP", quality=80)
    s = os.path.getsize(out)
    total += s
    print(f"r{i}.webp  {w}x{h} -> {s//1024}KB")
print("total webp:", total // 1024, "KB")
