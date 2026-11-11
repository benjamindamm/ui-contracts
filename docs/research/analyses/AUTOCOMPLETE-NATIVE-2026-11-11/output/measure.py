from collections import Counter
from hashlib import sha256
from itertools import groupby
from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops

root = Path(__file__).resolve().parents[1]
colors = {k: tuple(bytes.fromhex(v)) for k,v in {
    'focus':'2563eb', 'highlight':'eaf2ff', 'text':'172b4d', 'disabled':'94a3b8',
    'muted':'64748b', 'surface':'ffffff', 'closed-border':'cbd5e1', 'error':'b91c1c'}.items()}

def runs(sequence):
    start = 0
    for value, group in groupby(sequence):
        end = start + sum(1 for _ in group)
        yield start, end, value
        start = end

def box_color(image, rgb, region):
    crop = image.crop(region)
    # Intersect exact equality masks per channel to avoid treating other colours as matches.
    masks = [channel.point(lambda x: 255 if x == val else 0) for channel, val in zip(crop.split(), rgb)]
    mask = ImageChops.multiply(ImageChops.multiply(*masks[:2]), masks[2])
    box = mask.getbbox()
    return (box and tuple(v+region[i % 2] for i,v in enumerate(box)), mask.histogram()[255])

for platform, scale, regions in [
    ('ios', 3, [(120,340,1085,400),(120,425,1085,559),(120,570,1085,1065),(120,1065,1085,1135)]),
    ('android', 420/160, [(118,179,962,232),(118,252,962,370),(118,385,962,817),(118,827,962,885)]),
]:
    print(platform, 'px/logical unit', scale)
    image = Image.open(root/'output'/f'{platform}-active.png').convert('RGB')
    reference = Image.open(root/'input/deliveries'/platform/'screenshots/active.png').convert('RGB')
    for zone, region in zip(('label','field','popup','status'),regions):
        print(zone, 'region', region, 'diff bbox vs delivered', ImageChops.difference(image.crop(region),reference.crop(region)).getbbox())
        for name in {'label':['text'],'field':['focus','surface','muted'],'popup':['highlight','text','disabled','surface'],'status':['muted']}[zone]:
            print(name, box_color(image, colors[name], region))
    focus_box = box_color(image, colors['focus'], regions[1])[0]
    active_box = box_color(image, colors['highlight'], regions[2])[0]
    l,t,r,b=focus_box
    middle=image.width//2
    print('width, field height, row height', (r-l)/scale, (b-t)/scale, (active_box[3]-active_box[1])/scale)
    top_border=[x for x in range(l,r) if image.getpixel((x,t)) == colors['focus']]
    print('field top border horizontal inset in px (raster radius proxy)',top_border[0]-l,r-1-top_border[-1])
    print('centre pixels near popup top and bottom, run lengths, Y absolute')
    for start,end in [(active_box[1]-int(37*scale), active_box[1]-int(26*scale)), (active_box[1]+int(125*scale),active_box[1]+int(140*scale))]:
        print([(a+start,b+start,v) for a,b,v in runs(image.getpixel((middle,y)) for y in range(start,end))])
    for st, c in [('closed','closed-border'),('error','error')]:
        shot=Image.open(root/'output'/f'{platform}-{st}.png').convert('RGB')
        print(st, box_color(shot, colors[c], (l,t,r,regions[3][3])))
    print()

for rel in ['input/acceptance.md','input/reviewer.md','input/manifest.json','input/sources/tokens.json',
            *[str(p.relative_to(root)) for p in sorted((root/'input/sources/components').glob('*/*'))],
            *[str(p.relative_to(root)) for p in sorted((root/'input/deliveries').glob('ios/Autocomplete.app/**/*')) if p.is_file()],
            'input/deliveries/android/Autocomplete.apk','input/deliveries/android/screenshots/active.png',
            'input/deliveries/ios/screenshots/active.png']:
    print(sha256((root/rel).read_bytes()).hexdigest(), rel)
