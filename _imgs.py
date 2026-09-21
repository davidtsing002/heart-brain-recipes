import os
from PIL import Image

d = "C:/Users/EDY/WorkBuddy/2026-09-21-18-56-41/recipe-images"
mapping = {
    '五谷杂粮养生碗': 'c1', '山药红枣粥': 'c2', '生姜桂圆红枣茶': 'c3',
    '银耳百合羹': 'c4', '薏米赤小豆粥': 'c5', '绿豆百合汤': 'c6',
    '山楂玫瑰茶': 'c7', '玫瑰花茶': 'c8', '蜂蜜柠檬水': 'c9',
}
for f in os.listdir(d):
    if not f.endswith('.png'):
        continue
    for k, v in mapping.items():
        if k in f:
            src = os.path.join(d, f)
            dst = os.path.join(d, v + '.png')
            if not os.path.exists(dst):
                os.rename(src, dst)
            print('rename', k, '->', v + '.png')

for i in range(1, 10):
    p = os.path.join(d, f'c{i}.png')
    im = Image.open(p).convert('RGB')
    im.thumbnail((900, 900))
    out = os.path.join(d, f'c{i}.webp')
    im.save(out, 'WEBP', quality=82, method=4)
    print('webp c%d' % i, os.path.getsize(out), 'bytes')
