from PIL import Image, ImageDraw, ImageFont
import math

def make_meme():
    w, h = 1024, 1024
    img = Image.new('RGB', (w, h))
    grad = Image.new('RGB', (1, 256))
    c0, c1, c2 = (0x0b, 0x10, 0x35), (0x4b, 0x1d, 0x7a), (0xc2, 0x18, 0x7a)
    for y in range(256):
        t = y / 255.0
        if t < 0.5:
            r = int(c0[0] + (c1[0] - c0[0]) * (t * 2))
            g = int(c0[1] + (c1[1] - c0[1]) * (t * 2))
            b = int(c0[2] + (c1[2] - c0[2]) * (t * 2))
        else:
            r = int(c1[0] + (c2[0] - c1[0]) * ((t - 0.5) * 2))
            g = int(c1[1] + (c2[1] - c1[1]) * ((t - 0.5) * 2))
            b = int(c1[2] + (c2[2] - c1[2]) * ((t - 0.5) * 2))
        grad.putpixel((0, y), (r, g, b))
    img = grad.resize((w, h))
    d = ImageDraw.Draw(img)
    horizon = int(h * 0.7)
    skyline = [(100, 80, 200), (320, 120, 180), (550, 60, 220), (800, 100, 190)]
    for x, wt, ht in skyline:
        y0 = horizon - ht
        d.rectangle([x, y0, x + wt, horizon], fill='#12082e')
        for wx in range(x + 10, x + wt - 10, 20):
            for wy in range(y0 + 10, horizon - 10, 25):
                col = '#ffd76a' if (wx * wy) % 7 == 0 else '#59f2ff' if (wx + wy) % 11 == 0 else None
                if col:
                    d.rectangle([wx, wy, wx + 8, wy + 12], fill=col)
    # __C2__
    w, h = img.size
    d = ImageDraw.Draw(img)
    d.polygon([(w * 0.2, h), (w * 0.8, h), (w * 0.65, h * 0.7), (w * 0.35, h * 0.7)], fill='#0a0a14')
    for y in range(int(h * 0.72), h, 20):
        d.line([(w * 0.5, y), (w * 0.5, y + 10)], fill='#ffffaa', width=2)
    bx, by = w * 0.05, h * 0.75
    bw, bh = w * 0.2, h * 0.15
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=10, fill='white')
    cx, cy = bx + bw, by
    for ang in [0, 45, 90]:
        r = 15 if int(ang) % 2 else 25
        d.arc([cx - r, cy - r, cx, cy], 0, 90, fill='#ccc')
    d.line([cx, cy, cx - 20, cy - 20], fill='#ccc', width=1)
    d.line([cx, cy, cx - 30, cy], fill='#ccc', width=1)
    d.line([cx, cy, cx, cy - 30], fill='#ccc', width=1)
    d.ellipse([bx + bw * 0.8, by + bh * 0.4, bx + bw * 0.9, by + bh * 0.6], fill='#333')

    cx, cy = 700, 400
    r = 200
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill='white', outline='black', width=8)
    d.rectangle([cx - r, cy, cx + r, cy + 150], fill='white')
    d.line([(cx - r, cy), (cx - r, cy + 150)], fill='black')
    d.line([(cx + r, cy), (cx + r, cy + 150)], fill='black')
    tr1 = [cx - r, cy + 150, cx - r + 100, cy + 150, cx - r + 50, cy + 210]
    d.polygon(tr1, fill='white', outline='black')
    tr2 = [cx - r + 100, cy + 150, cx - r + 200, cy + 150, cx - r + 150, cy + 210]
    d.polygon(tr2, fill='white', outline='black')
    tr3 = [cx - r + 200, cy + 150, cx + r, cy + 150, cx + r - 50, cy + 210]
    d.polygon(tr3, fill='white', outline='black')
    ey, exs = cy-50, 60
    d.polygon([(cx-exs,ey),(cx-exs+20,ey-20),(cx-exs+40,ey),(cx-exs+20,ey+20)], fill='black')
    d.polygon([(cx+exs-40,ey),(cx+exs-20,ey-20),(cx+exs,ey),(cx+exs-20,ey+20)], fill='black')
    d.rounded_rectangle([w//2-100, h//2+50, w//2+100, h//2+130], radius=15, fill='black')
    d.ellipse([w//2-60, h//2+120, w//2-30, h//2+150], fill='white')
    d.ellipse([w//2+30, h//2+120, w//2+60, h//2+150], fill='white')
    d.ellipse([w//2-65, h//2+75, w//2-55, h//2+85], fill='white')
    d.ellipse([w//2+55, h//2+75, w//2+65, h//2+85], fill='white')
    d.ellipse([w//2-20, h//2+80, w//2-10, h//2+90], fill='magenta')
    d.ellipse([w//2+10, h//2+80, w//2+20, h//2+90], fill='cyan')
    d.ellipse([w//2-5, h//2+100, w//2+5, h//2+110], fill='yellow')
    d.ellipse([w//2-15, h//2+110, w//2-5, h//2+120], fill='white')
    from PIL import ImageFont
    d1 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 72)
    d2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 56)
    lc = w // 2
    t1, t2, t3 = 'BOUGHT A PS5', 'FOR GTA 6', 'PS6 COMES OUT FIRST'  # tuned
    y1 = int(h * 0.08)
    y2 = int(h * 0.18)
    y3 = int(h * 0.86)
    for text, y, font in [(t1, int(h * 0.04), d2), (t2, int(h * 0.11), d1), (t3, y3, d2)]:
        left, top, right, bottom = d.textbbox((0, 0), text, font=font)
        width = right - left
        x = (w - width) / 2
        d.text((x, y), text, font=font, fill='white', stroke_width=4, stroke_fill='black', anchor='lm')
    img.save('meme.png')
    print(img.size)

if __name__ == "__main__":
    make_meme()
